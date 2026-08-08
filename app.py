# Version 1.5.6: タイムライン黄色測定マークを加熱60分後の予定時刻へ統一
# Version 1.5.5: アラート経過時間を時間・分表示、監視開始後のボタン文言を簡略化
# Version 1.5.4: 初回MFR測定を加熱60分後へ修正・通知タイミング再確認
# Version 1.5.3: 次回測定までの残り時間を時間・分表示へ変更
# Version 1.5.2: UI表記をアラート／通知へ統一
# Version 1.5.1: 運用ブラウザー表記をEdgeへ統一
# Version 1.5.0: 親画面常駐エンジンで確認まで通知音を繰り返す
# Version 1.4.9: 確認ボタン押下まで通知音を確実に繰り返す
# Version 1.4.8: 通知欄の詳細表示を非表示・ボタン文言を固定
# Version 1.4.7: 通知音をWeb Audio API直接生成方式へ変更
# Version 1.4.6: 通知音診断とブラウザー再生処理を強化
# Version 1.4.5: 通知音キャッシュ・参照先・ブラウザーAudioを修正
# Version 1.4.4: 通知音をクリスタルライズへ変更
# Version 1.4.3: アプリ画面のLot表記統一
# Version 1.4.2: EcoNavi金額ラベル固定サイズ対応（小額でも18px表示）
# Version 1.4.1: EcoNaviデフォルト値（電気25円、修繕費0円、周期0時間）
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta, time as dt_time
import pickle
import os
import base64
import json
import urllib.request
import io
import math
import mimetypes
import hashlib
import struct
import wave
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components  # ★この1行を追加

# --- GitHub保存・読み込みロジック ---
# QRシステムと同じリポジトリに「mfr_products.json」という名前でマスターを保存します
GITHUB_REPO = "equipment-portal/qr-manager"
GITHUB_TOKEN = st.secrets.get("github_token", "")

def load_products_from_github():
    if not GITHUB_TOKEN: return None
    try:
        api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/mfr_products.json"
        req = urllib.request.Request(api_url)
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
        with urllib.request.urlopen(req) as res:
            data = json.loads(res.read().decode("utf-8"))
            content = base64.b64decode(data["content"]).decode("utf-8")
            return json.loads(content)
    except Exception:
        return None

def save_products_to_github(products_dict):
    if not GITHUB_TOKEN: return
    try:
        file_name = "mfr_products.json"
        api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{file_name}"
        
        sha = None
        try:
            req_check = urllib.request.Request(api_url)
            req_check.add_header("Authorization", f"token {GITHUB_TOKEN}")
            with urllib.request.urlopen(req_check) as res:
                sha = json.loads(res.read().decode("utf-8"))["sha"]
        except: pass
        
        encoded = base64.b64encode(json.dumps(products_dict, ensure_ascii=False, indent=2).encode("utf-8")).decode("utf-8")
        payload = {"message": "Update MFR Products Master", "content": encoded, "branch": "main"}
        if sha: payload["sha"] = sha
        
        req = urllib.request.Request(api_url, data=json.dumps(payload).encode("utf-8"), method="PUT")
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
        req.add_header("Content-Type", "application/json")
        urllib.request.urlopen(req)
    except Exception as e:
        print("GitHubセーブエラー:", e)

# ページ設定
logo_path = "logo.png" 
icon_path = "icon.ico" 
st.set_page_config(page_title="MFR電源管理システム", page_icon=icon_path, layout="wide")

# 10秒ごとに自動更新（Excelの後ろでも通知時刻を早く検出）
AUTO_REFRESH_MS = 10_000
st_autorefresh(interval=AUTO_REFRESH_MS, key="data_refresh")

# --- データの保存と読み込み ---
STATE_FILE = "mfr_state.pkl"

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "rb") as f:
                return pickle.load(f)
        except Exception:
            pass
    return None

def save_state():
    state_to_save = {
        'jobs': st.session_state.jobs,
        'last_inspection_date': st.session_state.last_inspection_date,
        'products': st.session_state.products,
        # 作業者が［確認しました］を押した通知だけを保存
        'acknowledged_alerts': st.session_state.acknowledged_alerts,
        # 実際に測定・点検が完了した10分後の電源OFF通知
        'pending_power_off_due': st.session_state.pending_power_off_due
    }
    with open(STATE_FILE, "wb") as f:
        pickle.dump(state_to_save, f)

def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# --- Edge通知・チャイム音 ---
# 通知音は必ずこのプログラムと同じフォルダーから読み込みます。
# 旧版の alert_chime.wav を誤って読み込まないよう、固有名を使用します。
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ALERT_SOUND_FILE = os.path.join(
    SCRIPT_DIR,
    "alert_crystal_rise.wav",
)
ALERT_SOUND_NAME = "クリスタルライズ"
ALERT_SOUND_VERSION = "crystal_rise_parent_engine_1_5_0"

# 未確認中のWindows通知を再表示する間隔。
# Excelを前面で使用していても気づきやすいよう、30秒ごとに再通知します。
WINDOWS_NOTIFICATION_REPEAT_MS = 30_000

# 生産スタート時をMFR加熱開始時刻とし、初回測定は60分後以降にする。
MFR_WARMUP_MINUTES = 60


def _build_chime_wav() -> bytes:
    """
    クリスタルライズ通知音をプログラム内で生成する。

    同じフォルダーに alert_chime.wav がある場合は外部ファイルを優先し、
    ファイルがない場合でも、明るく高級感のある上昇チャイムを生成する。
    """
    sample_rate = 44_100
    duration_seconds = 3.6
    frame_count = int(sample_rate * duration_seconds)

    # C5 → E5 → G5 → C6へ上昇し、最後に高音のきらめきを加える。
    tone_events = [
        # 開始秒, 周波数, 長さ, 音量, 明るさ
        (0.00, 523.25, 1.15, 0.52, 1.25),   # C5
        (0.20, 659.25, 1.15, 0.56, 1.25),   # E5
        (0.40, 783.99, 1.15, 0.60, 1.25),   # G5
        (0.65, 1046.50, 1.15, 0.66, 1.25),  # C6
        (0.88, 1567.98, 0.55, 0.20, 1.40),  # G6 sparkle
    ]

    mixed = [0.0] * frame_count

    for start_seconds, frequency, tone_duration, volume, brightness in tone_events:
        start_frame = int(start_seconds * sample_rate)
        tone_frames = int(tone_duration * sample_rate)

        for i in range(tone_frames):
            output_index = start_frame + i
            if output_index >= frame_count:
                break

            t = i / sample_rate

            # 最初は素早く立ち上がり、ベルのように自然に減衰する。
            attack = min(1.0, t / 0.008)
            base_decay = math.exp(-3.45 * t / max(tone_duration, 0.05))

            # 基音と複数の倍音を混ぜ、透明感のあるベル音にする。
            raw = (
                1.00
                * math.sin(2 * math.pi * frequency * t)
                * base_decay
                + 0.36
                * brightness
                * math.sin(2 * math.pi * frequency * 2.01 * t)
                * math.exp(-3.70 * t / max(tone_duration, 0.05))
                + 0.18
                * brightness
                * math.sin(2 * math.pi * frequency * 3.97 * t)
                * math.exp(-4.20 * t / max(tone_duration, 0.05))
                + 0.08
                * brightness
                * math.sin(2 * math.pi * frequency * 6.10 * t)
                * math.exp(-4.75 * t / max(tone_duration, 0.05))
            )

            mixed[output_index] += raw * attack * volume

    # 複数音を重ねても音割れしないよう、全体を正規化する。
    max_level = max((abs(value) for value in mixed), default=1.0)
    peak_amplitude = 28_000
    scale = peak_amplitude / max(max_level, 1e-9)

    frames = bytearray()
    for value in mixed:
        sample = int(value * scale)
        sample = max(-32_768, min(32_767, sample))
        frames.extend(struct.pack("<h", sample))

    buffer = io.BytesIO()
    with wave.open(buffer, "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(bytes(frames))

    return buffer.getvalue()


def get_alert_sound_file_mtime_ns() -> int:
    """通知音ファイルの更新時刻を返し、差し替え時にキャッシュを更新する。"""
    try:
        return os.stat(ALERT_SOUND_FILE).st_mtime_ns
    except OSError:
        return 0


@st.cache_data(show_spinner=False)
def get_alert_sound_data_url(
    sound_version: str,
    sound_file_mtime_ns: int,
):
    """
    通知音をData URLへ変換する。

    sound_versionと更新時刻をキャッシュキーに含めることで、
    コード更新後も旧通知音が残る問題を防止する。
    """
    # 引数はキャッシュ更新に使用する。
    _ = sound_version, sound_file_mtime_ns

    if os.path.exists(ALERT_SOUND_FILE):
        mime_type = (
            mimetypes.guess_type(ALERT_SOUND_FILE)[0]
            or "audio/wav"
        )
        with open(ALERT_SOUND_FILE, "rb") as sound_file:
            encoded = base64.b64encode(sound_file.read()).decode("ascii")
        return f"data:{mime_type};base64,{encoded}"

    encoded = base64.b64encode(_build_chime_wav()).decode("ascii")
    return f"data:audio/wav;base64,{encoded}"


def get_current_alert_sound_data_url():
    """常に現在の音色バージョンとファイル更新時刻で音声を取得する。"""
    return get_alert_sound_data_url(
        ALERT_SOUND_VERSION,
        get_alert_sound_file_mtime_ns(),
    )


def get_alert_sound_diagnostics():
    """現在使用する通知音の読み込み情報を返す。"""
    if os.path.exists(ALERT_SOUND_FILE):
        with open(ALERT_SOUND_FILE, "rb") as sound_file:
            sound_bytes = sound_file.read()
        source_name = os.path.basename(ALERT_SOUND_FILE)
        source_type = "外部WAVファイル"
    else:
        sound_bytes = _build_chime_wav()
        source_name = "プログラム内生成音"
        source_type = "内部生成"

    return {
        "bytes": sound_bytes,
        "name": source_name,
        "type": source_type,
        "size": len(sound_bytes),
        "hash": hashlib.sha256(sound_bytes).hexdigest(),
    }


def render_monitor_activation():
    """
    始業時にクリックして、通知音とWindows通知を有効にする。

    通知音エンジンはStreamlitのiframe内ではなく、
    親のEdge画面へscriptとして直接設置する。
    これにより10秒ごとの自動更新後も繰り返しタイマーを維持する。
    """
    sound_name_js = json.dumps(ALERT_SOUND_NAME, ensure_ascii=False)
    sound_version_js = json.dumps(ALERT_SOUND_VERSION)

    parent_engine_code = r"""
(() => {
  const w = window;
  const VERSION = "__MFR_SOUND_VERSION__";

  const previous = w.__mfrCrystalEngine;
  if (previous && previous.version === VERSION) {
    return;
  }

  if (previous && typeof previous.stopAll === "function") {
    try {
      previous.stopAll();
    } catch (error) {}
  }

  const state = {
    context: null,
    timer: null,
    watchdog: null,
    alertId: null,
    sources: [],
    lastPlayAt: 0
  };

  function getAudioContext() {
    const AudioContextClass =
      w.AudioContext || w.webkitAudioContext;

    if (!AudioContextClass) {
      throw new Error(
        "このブラウザーはWeb Audio APIに対応していません。"
      );
    }

    if (
      !state.context
      || state.context.state === "closed"
    ) {
      state.context = new AudioContextClass();
    }

    return state.context;
  }

  function stopSources() {
    for (const oscillator of state.sources) {
      try {
        oscillator.stop();
      } catch (error) {}
    }
    state.sources = [];
  }

  async function playOnce() {
    const audioContext = getAudioContext();

    if (audioContext.state === "suspended") {
      await audioContext.resume();
    }

    const now = audioContext.currentTime + 0.03;

    const compressor =
      audioContext.createDynamicsCompressor();
    compressor.threshold.setValueAtTime(-18, now);
    compressor.knee.setValueAtTime(14, now);
    compressor.ratio.setValueAtTime(5, now);
    compressor.attack.setValueAtTime(0.003, now);
    compressor.release.setValueAtTime(0.30, now);
    compressor.connect(audioContext.destination);

    const master = audioContext.createGain();
    master.gain.setValueAtTime(0.78, now);
    master.connect(compressor);

    // クリスタルライズ：C5 → E5 → G5 → C6
    const events = [
      {start: 0.00, frequency: 523.25, duration: 1.15, level: 0.62},
      {start: 0.20, frequency: 659.25, duration: 1.15, level: 0.66},
      {start: 0.40, frequency: 783.99, duration: 1.15, level: 0.70},
      {start: 0.65, frequency: 1046.50, duration: 1.15, level: 0.76},
      {start: 0.88, frequency: 1567.98, duration: 0.55, level: 0.30}
    ];

    const partials = [
      {multiple: 1.00, level: 1.00},
      {multiple: 2.01, level: 0.34},
      {multiple: 3.97, level: 0.15},
      {multiple: 6.10, level: 0.055}
    ];

    for (const event of events) {
      const eventStart = now + event.start;
      const eventEnd = eventStart + event.duration;

      for (const partial of partials) {
        const oscillator =
          audioContext.createOscillator();
        const gain = audioContext.createGain();

        oscillator.type = "sine";
        oscillator.frequency.setValueAtTime(
          event.frequency * partial.multiple,
          eventStart
        );

        const peak = Math.max(
          0.0002,
          event.level * partial.level * 0.18
        );

        gain.gain.setValueAtTime(0.0001, eventStart);
        gain.gain.exponentialRampToValueAtTime(
          peak,
          eventStart + 0.010
        );
        gain.gain.exponentialRampToValueAtTime(
          0.0001,
          eventEnd
        );

        oscillator.connect(gain);
        gain.connect(master);

        state.sources.push(oscillator);

        oscillator.onended = () => {
          state.sources = state.sources.filter(
            item => item !== oscillator
          );
        };

        oscillator.start(eventStart);
        oscillator.stop(eventEnd + 0.03);
      }
    }

    state.lastPlayAt = Date.now();
    return audioContext.state;
  }

  function stopLoop(clearStorage = true) {
    if (state.timer) {
      w.clearInterval(state.timer);
      state.timer = null;
    }

    if (state.watchdog) {
      w.clearInterval(state.watchdog);
      state.watchdog = null;
    }

    state.alertId = null;
    state.lastPlayAt = 0;
    stopSources();

    if (clearStorage) {
      w.localStorage.removeItem(
        "mfr_active_alert_id"
      );
      w.localStorage.removeItem(
        "mfr_alarm_loop_enabled"
      );
    }
  }

  async function startLoop(alertId) {
    if (!alertId) return;

    const storedAlertId =
      w.localStorage.getItem(
        "mfr_active_alert_id"
      );

    if (
      state.timer
      && state.alertId === alertId
      && storedAlertId === alertId
    ) {
      return;
    }

    stopLoop(false);

    state.alertId = alertId;
    w.localStorage.setItem(
      "mfr_active_alert_id",
      alertId
    );
    w.localStorage.setItem(
      "mfr_alarm_loop_enabled",
      "1"
    );

    const playIfActive = async () => {
      const activeAlertId =
        w.localStorage.getItem(
          "mfr_active_alert_id"
        );
      const loopEnabled =
        w.localStorage.getItem(
          "mfr_alarm_loop_enabled"
        ) === "1";

      if (
        !loopEnabled
        || activeAlertId !== alertId
        || state.alertId !== alertId
      ) {
        stopLoop(false);
        return;
      }

      try {
        await playOnce();
        w.localStorage.removeItem(
          "mfr_audio_error"
        );
      } catch (error) {
        w.localStorage.setItem(
          "mfr_audio_error",
          `${error?.name || "AudioError"}: `
          + `${error?.message || String(error)}`
        );
      }
    };

    // アラート発生時に直ちに1回鳴らす。
    await playIfActive();

    // 確認ボタンを押すまで4.2秒ごとに繰り返す。
    state.timer = w.setInterval(
      playIfActive,
      4200
    );

    // タイマーが停止した場合の復旧監視。
    state.watchdog = w.setInterval(() => {
      const activeAlertId =
        w.localStorage.getItem(
          "mfr_active_alert_id"
        );
      const loopEnabled =
        w.localStorage.getItem(
          "mfr_alarm_loop_enabled"
        ) === "1";
      const elapsed =
        Date.now() - (state.lastPlayAt || 0);

      if (
        loopEnabled
        && activeAlertId === alertId
        && state.alertId === alertId
        && elapsed >= 5200
      ) {
        playIfActive();
      }
    }, 1000);
  }

  async function activate() {
    const contextState = await playOnce();

    const activeAlertId =
      w.localStorage.getItem(
        "mfr_active_alert_id"
      );
    const loopEnabled =
      w.localStorage.getItem(
        "mfr_alarm_loop_enabled"
      ) === "1";

    // 既にアラートが出ている状態で監視開始を押した場合は、
    // テスト音の後からアラート音ループを再開する。
    if (loopEnabled && activeAlertId) {
      w.setTimeout(() => {
        startLoop(activeAlertId);
      }, 4200);
    }

    return contextState;
  }

  function stopAll() {
    stopLoop(true);
  }

  w.__mfrCrystalEngine = {
    version: VERSION,
    activate,
    playOnce,
    startLoop,
    stopAll,
    getState: () => ({
      alertId: state.alertId,
      timerActive: Boolean(state.timer),
      contextState:
        state.context
        ? state.context.state
        : "not-created"
    })
  };
})();
"""
    parent_engine_code = parent_engine_code.replace(
        "__MFR_SOUND_VERSION__",
        ALERT_SOUND_VERSION,
    )
    parent_engine_code_js = json.dumps(parent_engine_code)

    html = f"""
    <div style="font-family:Meiryo,sans-serif;border:2px solid #2563eb;
                border-radius:10px;padding:12px;background:#eff6ff;">
      <button id="mfr-enable" style="width:100%;padding:12px;font-size:17px;
              font-weight:bold;color:white;background:#1d4ed8;border:0;
              border-radius:8px;cursor:pointer;">
        起動時に必ず押してください。監視開始、チャイム音・Windows通知テスト
      </button>

      <div id="mfr-status" style="display:none;margin-top:8px;
              font-size:14px;font-weight:bold;color:#b91c1c;
              white-space:pre-wrap;"></div>
    </div>

    <script>
    (() => {{
      const parentWindow = window.parent;
      const button = document.getElementById("mfr-enable");
      const status = document.getElementById("mfr-status");
      const soundName = {sound_name_js};
      const soundVersion = {sound_version_js};
      const engineCode = {parent_engine_code_js};
      const engineScriptId = "mfr-crystal-parent-engine";

      function showError(message) {{
        status.textContent = message;
        status.style.display = "block";
      }}

      function hideStatus() {{
        status.textContent = "";
        status.style.display = "none";
      }}

      function installParentEngine() {{
        const currentEngine =
          parentWindow.__mfrCrystalEngine;
        const currentScript =
          parentWindow.document.getElementById(
            engineScriptId
          );

        if (
          currentEngine
          && currentEngine.version === soundVersion
        ) {{
          return;
        }}

        if (currentScript) {{
          currentScript.remove();
        }}

        const script =
          parentWindow.document.createElement("script");
        script.id = engineScriptId;
        script.dataset.version = soundVersion;
        script.textContent = engineCode;
        parentWindow.document.head.appendChild(script);
      }}

      button.addEventListener("click", async () => {{
        try {{
          hideStatus();
          installParentEngine();

          parentWindow.localStorage.setItem(
            "mfr_monitor_enabled",
            "1"
          );
          parentWindow.localStorage.setItem(
            "mfr_alert_sound_version",
            soundVersion
          );

          let permission = "unsupported";
          if ("Notification" in parentWindow) {{
            permission =
              parentWindow.Notification.permission;

            if (permission === "default") {{
              permission =
                await parentWindow.Notification
                  .requestPermission();
            }}
          }}

          await parentWindow
            .__mfrCrystalEngine
            .activate();

          if (permission === "granted") {{
            const notification =
              new parentWindow.Notification(
                "MFR通知テスト",
                {{
                  body:
                    `通知音「${{soundName}}」と`
                    + "Windows通知の準備が完了しました。",
                  tag: "mfr-notification-test",
                  requireInteraction: true
                }}
              );

            notification.onclick = () => {{
              parentWindow.focus();
              notification.close();
            }};
          }}

          hideStatus();
          button.textContent = "監視開始、チャイム音・Windows通知テスト";
          button.style.background = "#15803d";

        }} catch (error) {{
          showError(
            "⚠️ 通知音を再生できませんでした。\\n"
            + `エラー：${{error?.name || "UnknownError"}}\\n`
            + `${{error?.message || String(error)}}`
          );
          button.style.background = "#b91c1c";
        }}
      }});

      installParentEngine();
    }})();
    </script>
    """

    components.html(html, height=105, scrolling=False)



def start_browser_alarm(alert_id, title, body):
    """
    親のEdge画面に設置した通知音エンジンへ、
    確認されるまでの繰り返し再生を依頼する。
    """
    alert_id_json = json.dumps(alert_id, ensure_ascii=False)
    title_json = json.dumps(title, ensure_ascii=False)
    body_json = json.dumps(body, ensure_ascii=False)
    repeat_ms = int(WINDOWS_NOTIFICATION_REPEAT_MS)

    launcher_code = f"""
(() => {{
  const alertId = {alert_id_json};
  const title = {title_json};
  const body = {body_json};
  const repeatMs = {repeat_ms};

  localStorage.setItem(
    "mfr_active_alert_id",
    alertId
  );
  localStorage.setItem(
    "mfr_alarm_loop_enabled",
    "1"
  );

  let attempts = 0;

  const startWhenReady = () => {{
    attempts += 1;

    if (
      window.__mfrCrystalEngine
      && typeof window.__mfrCrystalEngine.startLoop
        === "function"
    ) {{
      window.__mfrCrystalEngine
        .startLoop(alertId)
        .catch((error) => {{
          localStorage.setItem(
            "mfr_audio_error",
            `${{error?.name || "AudioError"}}: `
            + `${{error?.message || String(error)}}`
          );
        }});
      return;
    }}

    if (attempts < 30) {{
      window.setTimeout(
        startWhenReady,
        200
      );
    }} else {{
      localStorage.setItem(
        "mfr_audio_error",
        "通知音エンジンを開始できませんでした。"
      );
    }}
  }};

  startWhenReady();

  const notifyTimeKey =
    "mfr_notify_time_" + alertId;
  const lastNotifyTime = Number(
    localStorage.getItem(notifyTimeKey) || "0"
  );
  const currentTime = Date.now();

  if (
    currentTime - lastNotifyTime >= repeatMs
    && "Notification" in window
    && Notification.permission === "granted"
  ) {{
    if (window.__mfrNotification) {{
      try {{
        window.__mfrNotification.close();
      }} catch (error) {{}}
    }}

    const notification =
      new Notification(title, {{
        body:
          body
          + "\\n未確認のため再通知しています。",
        tag: "mfr-" + alertId,
        requireInteraction: true,
        renotify: true,
        timestamp: currentTime
      }});

    notification.onclick = () => {{
      window.focus();
      notification.close();
    }};

    window.__mfrNotification = notification;
    localStorage.setItem(
      notifyTimeKey,
      String(currentTime)
    );
  }}
}})();
"""
    launcher_code_js = json.dumps(launcher_code)

    html = f"""
    <script>
    (() => {{
      const parentWindow = window.parent;
      const launcherCode = {launcher_code_js};
      const launcher =
        parentWindow.document.createElement("script");

      launcher.textContent = launcherCode;
      parentWindow.document.head.appendChild(launcher);
      launcher.remove();
    }})();
    </script>
    """

    components.html(html, height=0, width=0)



def stop_browser_alarm():
    stop_code = r"""
(() => {
  localStorage.removeItem(
    "mfr_active_alert_id"
  );
  localStorage.removeItem(
    "mfr_alarm_loop_enabled"
  );

  if (
    window.__mfrCrystalEngine
    && typeof window.__mfrCrystalEngine.stopAll
      === "function"
  ) {
    window.__mfrCrystalEngine.stopAll();
  }

  if (window.__mfrNotification) {
    try {
      window.__mfrNotification.close();
    } catch (error) {}
    window.__mfrNotification = null;
  }
})();
"""
    stop_code_js = json.dumps(stop_code)

    html = f"""
    <script>
    (() => {{
      const parentWindow = window.parent;
      const stopCode = {stop_code_js};
      const stopper =
        parentWindow.document.createElement("script");

      stopper.textContent = stopCode;
      parentWindow.document.head.appendChild(stopper);
      stopper.remove();
    }})();
    </script>
    """

    components.html(html, height=0, width=0)



def get_measurement_text(num_targets, current_target_qty, targets):
    if num_targets == 2:
        if current_target_qty == targets[0]: return '始'
        if current_target_qty == targets[1]: return '終'
    elif num_targets == 3:
        if current_target_qty == targets[0]: return '始'
        if current_target_qty == targets[1]: return '中'
        if current_target_qty == targets[2]: return '終'
    return str(current_target_qty)


def format_remaining_time(minutes):
    """残り時間を読みやすい「○時間○分」形式へ変換する。"""
    total_minutes = max(0, int(minutes))
    hours, mins = divmod(total_minutes, 60)

    if hours > 0 and mins > 0:
        return f"{hours}時間{mins}分"
    if hours > 0:
        return f"{hours}時間"
    return f"{mins}分"


# --- CSS設定 ---
st.markdown(
    """
    <style>
    /* 文字サイズのアンバランスを解消する超・強力なフォント統一（全要素に強制適用） */
    * {
        font-family: "Meiryo", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif !important;
    }
    
    /* サイドバーの矢印（keyboard...）などを絶対に文字化けさせない最強のシールド */
    .material-symbols-rounded, .material-icons, [data-testid="collapsedControl"] *, [data-testid*="Icon"], svg, i {
        font-family: "Material Symbols Rounded", "Material Icons", sans-serif !important;
        font-style: normal !important;
        font-weight: 400 !important;
    }
    
    /* MFR専用のステータスヘッダー（※QRシステムではこのブロックはなくてもOKですが、あっても無害です） */
    .mfr-status-header {
        font-size: 1.25rem !important; 
        font-weight: bold !important; 
        margin-top: 10px !important;
        margin-bottom: 5px !important;
    }

    .stButton button { width: 100%; border-radius: 5px; }

    .mfr-active-alert {
        background: #b91c1c;
        color: white;
        border: 5px solid #7f1d1d;
        border-radius: 14px;
        padding: 22px;
        margin: 14px 0 10px 0;
        text-align: center;
        animation: mfr-pulse 1.2s infinite alternate;
    }

    @keyframes mfr-pulse {
        from { box-shadow: 0 0 0 rgba(185, 28, 28, 0.2); }
        to   { box-shadow: 0 0 28px rgba(185, 28, 28, 0.85); }
    }
    
    /* 天井の余白設定 */
    .block-container { padding-top: 3.0rem !important; }
    
    /* サイドバーのボタン改行はみ出し修正（高さを自動調整し、改行を許容する） */
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0.3rem !important; }
    [data-testid="stSidebar"] button { 
        padding: 6px 10px !important; 
        height: auto !important; 
        min-height: 35px !important; 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        line-height: 1.4 !important;
        white-space: normal !important;
    }
    
    #MainMenu {visibility: hidden;} footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 初期設定・状態管理 ---
if 'initialized' not in st.session_state:
    saved_state = load_state()
    gh_products = load_products_from_github() # ★起動時にGitHubからマスターを取得！

    if saved_state:
        st.session_state.jobs = saved_state['jobs']
        st.session_state.last_inspection_date = saved_state['last_inspection_date']
        st.session_state.acknowledged_alerts = saved_state.get('acknowledged_alerts', [])
        st.session_state.pending_power_off_due = saved_state.get('pending_power_off_due')
        # ★GitHubのデータがあれば最優先、なければローカルデータ
        st.session_state.products = gh_products if gh_products is not None else saved_state.get('products', {})
    else:
        st.session_state.jobs = {'100t': None, '450t': None, '550t': None}
        st.session_state.last_inspection_date = None
        st.session_state.acknowledged_alerts = []
        st.session_state.pending_power_off_due = None
        default_products = {
            'サンプル製品A': {'machine': '100t', 'qty': 500, 'cycle': 60.0, 'measurements': 2},
            'サンプル製品B': {'machine': '450t', 'qty': 1000, 'cycle': 30.0, 'measurements': 3}
        }
        st.session_state.products = gh_products if gh_products is not None else default_products
        
    # 既存保存データにも安定したジョブIDを追加（通知IDが毎回変わるのを防止）
    for machine_name, saved_job in st.session_state.jobs.items():
        if saved_job is None:
            continue

        if not saved_job.get('job_id'):
            anchor = saved_job.get(
                'last_update',
                datetime.utcnow() + timedelta(hours=9)
            )
            if not isinstance(anchor, datetime):
                anchor = datetime.utcnow() + timedelta(hours=9)
            saved_job['job_id'] = (
                f"{machine_name}_{anchor.strftime('%Y%m%d%H%M%S')}"
            )

        # V1.5.4以前に開始した生産データにも加熱60分条件を補完する。
        # まだMFR測定を1回も完了していないLotだけを対象にする。
        if 'heat_ready_at' not in saved_job:
            if not saved_job.get('completed'):
                heat_anchor = saved_job.get('last_update')
                if not isinstance(heat_anchor, datetime):
                    heat_anchor = datetime.utcnow() + timedelta(hours=9)

                saved_job['heat_ready_at'] = (
                    heat_anchor
                    + timedelta(minutes=MFR_WARMUP_MINUTES)
                )
            else:
                # 「始」測定済みなら初回加熱待ちは不要。
                saved_job['heat_ready_at'] = None

    st.session_state.initialized = True
    st.session_state.inspection_dialog_shown = False

# コード更新中も既存ブラウザーセッションを安全に引き継ぐ
if 'acknowledged_alerts' not in st.session_state:
    st.session_state.acknowledged_alerts = []
if 'pending_power_off_due' not in st.session_state:
    st.session_state.pending_power_off_due = None

# --- UI：サイドバー ---
with st.sidebar:
    st.header("⚙️ システム管理")
        
    st.subheader("📦 製品マスター管理")
    with st.expander("製品の登録・編集・削除", expanded=False):
        # 1. 編集対象の選択（新規か既存か）
        product_options = ["✨ 新規登録"] + list(st.session_state.products.keys())
        selected_prod = st.selectbox("📝 編集する製品を選択 (または新規登録)", product_options)

        # 2. 選択された製品のデータを読み込む
        if selected_prod == "✨ 新規登録":
            def_name = ""
            def_machine_idx = 0
            def_qty = 100
            def_cycle = 30.0
            def_meas_idx = 0
        else:
            def_name = selected_prod
            p_info = st.session_state.products[selected_prod]
            
            # エラー防止：古いデータに machine がない場合は 100t にする
            m_val = p_info.get('machine', '100t')
            def_machine_idx = ["100t", "450t", "550t"].index(m_val) if m_val in ["100t", "450t", "550t"] else 0
            
            def_qty = p_info.get('qty', 100)
            def_cycle = float(p_info.get('cycle', 30.0))
            def_meas_idx = 0 if p_info.get('measurements', 2) == 2 else 1

        # 3. 入力フォーム（初期値に呼び出したデータをセット）
        with st.form("product_form"):
            p_name = st.text_input("製品名", value=def_name)
            p_machine = st.selectbox("対象の成型機", ["100t", "450t", "550t"], index=def_machine_idx)
            p_qty = st.number_input("生産数", min_value=1, value=def_qty)
            p_cycle = st.number_input("サイクルタイム(秒)", min_value=0.1, value=def_cycle, step=0.1)
            p_meas = st.radio("MFR測定回数", options=[2, 3], index=def_meas_idx, format_func=lambda x: "2回 (初め・終わり)" if x==2 else "3回 (初め・中・終わり)")
            
            submit_btn = st.form_submit_button("💾 登録・更新（クラウド同期）")
            if submit_btn and p_name:
                # 既存製品の名前を変更（リネーム）した場合は、古い名前のデータを消して重複を防ぐ
                if selected_prod != "✨ 新規登録" and p_name != selected_prod:
                    del st.session_state.products[selected_prod]
                    
                st.session_state.products[p_name] = {'machine': p_machine, 'qty': p_qty, 'cycle': p_cycle, 'measurements': p_meas}
                save_state()
                save_products_to_github(st.session_state.products) # ★GitHubに自動バックアップ！
                
                st.success(f"「{p_name} ({p_machine})」をクラウドに登録・更新しました！")
                st.rerun()
        
        # 4. 削除ツール
        st.markdown("---")
        if st.session_state.products:
            del_name = st.selectbox("削除する製品を選択", list(st.session_state.products.keys()), key="del_prod_sel")
            if st.button("🗑️ 選択した製品を削除（クラウド同期）"):
                del st.session_state.products[del_name]
                save_state()
                save_products_to_github(st.session_state.products) # ★削除もGitHubに同期！
                
                st.success(f"「{del_name}」をクラウドから削除しました。")
                st.rerun()

    st.markdown("---")
    st.subheader("🔧 リセット・テスト用ツール")
    if st.button("🔄 すべての成型機の状態をリセット"):
        st.session_state.jobs = {'100t': None, '450t': None, '550t': None}
        st.session_state.pending_power_off_due = None
        save_state(); st.rerun()
        
    if st.button("🔄 今日の点検状態を未実施に戻す"):
        st.session_state.last_inspection_date = None; st.session_state.inspection_dialog_shown = False
        save_state(); st.rerun()

    if st.button("🔕 通知の確認履歴をリセット（テスト用）"):
        st.session_state.acknowledged_alerts = []
        save_state(); st.rerun()

# --- 事前計算ロジック ---
now = (datetime.utcnow() + timedelta(hours=9))
today_date = now.date()

def calculate_planned_measurement_time(job, target):
    """
    未完了のMFR測定予定時刻を一元計算する。

    生産数・サイクルタイムから求めた時刻が早くても、
    生産スタートから60分の加熱完了時刻より前にはしない。
    通知、電源スケジュール、タイムラインの黄色◆で共通使用する。
    """
    if job is None or job.get('status') != 'Running':
        return None

    remaining_qty = target - job['current_qty']

    if remaining_qty <= 0:
        est_time = job['last_update']
    else:
        est_time = (
            job['last_update']
            + timedelta(
                seconds=remaining_qty * job['cycle_time']
            )
        )

    heat_ready_at = job.get('heat_ready_at')
    if (
        isinstance(heat_ready_at, datetime)
        and est_time < heat_ready_at
    ):
        est_time = heat_ready_at

    return est_time


def calculate_upcoming_measurements():
    upcoming = []
    max_date = today_date 
    
    for machine, job in st.session_state.jobs.items():
        if job is None or job['status'] == 'Completed': continue
        for target in job['targets']:
            if target not in job['completed']:
                if job['status'] == 'Running':
                    est_time = calculate_planned_measurement_time(
                        job,
                        target,
                    )
                elif job['status'] == 'Paused':
                    est_time = None 
                
                upcoming.append({
                    'machine': machine, 'target_qty': target, 'est_time': est_time,
                    'status': job['status'], 'Targets': job['targets']
                })
                if est_time and est_time.date() > max_date:
                    max_date = est_time.date()
    
    # 日常点検の予定を自動追加
    for i in range((max_date - today_date).days + 1):
        d = today_date + timedelta(days=i)
        if d == today_date and st.session_state.last_inspection_date == today_date:
            continue
        is_monday_d = (d.weekday() == 0)
        insp_time = datetime(d.year, d.month, d.day, 8 if is_monday_d else 7, 0, 0)
        est_time_insp = insp_time
        upcoming.append({
            'machine': '日常点検(A勤)', 'target_qty': '日常点検',
            'est_time': est_time_insp, 'status': 'Planned', 'Targets': ['日常点検']
        })

    valid_upcoming = [x for x in upcoming if x['est_time'] is not None]
    valid_upcoming.sort(key=lambda x: x['est_time'])
    return valid_upcoming, upcoming

valid_upcoming, all_upcoming = calculate_upcoming_measurements()

on_blocks = []
if valid_upcoming:
    current_start = valid_upcoming[0]['est_time'] - timedelta(minutes=60)
    current_end = valid_upcoming[0]['est_time']
    for i in range(1, len(valid_upcoming)):
        next_measure = valid_upcoming[i]['est_time']
        gap_minutes = (next_measure - current_end).total_seconds() / 60
        if gap_minutes >= 90:
            on_blocks.append((current_start, current_end + timedelta(minutes=10)))
            current_start = next_measure - timedelta(minutes=60)
            current_end = next_measure
        else:
            current_end = next_measure
    on_blocks.append((current_start, current_end + timedelta(minutes=10)))

# --- アラーム・ダイアログ通知 ---
# 「表示しただけ」では消さず、作業者が［確認しました］を押すまで active_alerts に残します。
active_alerts = []

is_monday = (today_date.weekday() == 0)
inspection_start_hour = 8 if is_monday else 7
inspection_start_time = datetime.combine(today_date, dt_time(inspection_start_hour, 0, 0))
inspection_end_time = datetime.combine(today_date, dt_time(10, 0, 0))

# 1. 日常点検（10時を過ぎても自動完了にはしない）
if st.session_state.last_inspection_date != today_date and now >= inspection_start_time:
    inspection_alert_id = f"INSP_{today_date.strftime('%Y%m%d')}"
    if inspection_alert_id not in st.session_state.acknowledged_alerts:
        active_alerts.append({
            "id": inspection_alert_id,
            "due": inspection_start_time,
            "title": "📋 日常点検アラート",
            "message": f"本日の日常点検が未完了です。予定時刻は {inspection_start_time.strftime('%H:%M')} です。",
            "kind": "inspection",
        })

# 2. MFR測定（予定時刻になったら、確認されるまでアラートを継続）
for pt in valid_upcoming:
    if pt['machine'] == '日常点検(A勤)':
        continue

    m_time = pt['est_time']
    if m_time <= now:
        job = st.session_state.jobs.get(pt['machine'])
        if job is None:
            continue

        meas_text = get_measurement_text(len(pt['Targets']), pt['target_qty'], pt['Targets'])
        job_id = job.get('job_id', pt['machine'])
        alert_id_meas = f"MEAS_{job_id}_{pt['target_qty']}"

        if alert_id_meas not in st.session_state.acknowledged_alerts:
            active_alerts.append({
                "id": alert_id_meas,
                "due": m_time,
                "title": "🎯 MFR測定アラート",
                "message": (
                    f"{pt['machine']} 成型機（{meas_text}）のMFR測定時刻です。"
                    f" 予定時刻：{m_time.strftime('%m/%d %H:%M')}"
                ),
                "kind": "measurement",
            })

# 3. 電源ON・OFF
# on_blocks の終了時刻には、最終測定後10分の冷却時間を含めています。
for b_start, b_off in on_blocks:
    target_tasks = [
        x['machine'] for x in valid_upcoming
        if x['est_time'] is not None and b_start <= x['est_time'] <= b_off
    ]
    target_machine = target_tasks[0] if target_tasks else "成型機"

    # 対象作業が未完了なら、電源ON予定を過ぎてもアラートを維持する。
    if b_start <= now:
        alert_id_on = f"ON_{b_start.strftime('%Y%m%d_%H%M')}"
        if alert_id_on not in st.session_state.acknowledged_alerts:
            first_measure_time = b_start + timedelta(minutes=60)
            active_alerts.append({
                "id": alert_id_on,
                "due": b_start,
                "title": "🔥 MFR電源ONアラート",
                "message": (
                    f"MFR測定器の電源をONにしてください。"
                    f" 対象：{target_machine}／最初の予定：{first_measure_time.strftime('%m/%d %H:%M')}"
                ),
                "kind": "power_on",
            })

# 4. 実際の測定・点検完了から10分後の電源OFF
pending_off_due = st.session_state.pending_power_off_due
if pending_off_due is not None:
    # 未完了の測定が90分以内に残る場合は、電源を維持するためOFF予約を取り消す
    completion_time = pending_off_due - timedelta(minutes=10)
    keep_power_on = any(
        item['est_time'] is not None
        and item['est_time'] <= completion_time + timedelta(minutes=90)
        for item in valid_upcoming
    )

    if keep_power_on:
        st.session_state.pending_power_off_due = None
        save_state()
    elif now >= pending_off_due:
        alert_id_off = f"OFF_ACTUAL_{pending_off_due.strftime('%Y%m%d_%H%M')}"
        if alert_id_off not in st.session_state.acknowledged_alerts:
            active_alerts.append({
                "id": alert_id_off,
                "due": pending_off_due,
                "title": "💤 MFR電源OFFアラート",
                "message": (
                    f"最後の測定・点検完了から10分経過しました。"
                    f"MFR測定器の電源をOFFにしてください。"
                    f" 予定時刻：{pending_off_due.strftime('%m/%d %H:%M')}"
                ),
                "kind": "power_off",
            })

active_alerts.sort(key=lambda item: item["due"])


# --- UI：ヘッダー（QRシステムと同じサイズ感に統一） ---
try:
    logo_base64 = get_image_base64(logo_path)
    logo_html = f"""
    <div style="display: flex; align-items: flex-end; margin-bottom: 1rem;">
        <img src="data:image/png;base64,{logo_base64}" height="100" style="margin-right: 15px; flex-shrink: 0;">
        <span style="font-size: calc(1.4rem + 1.2vw); font-weight: 700; line-height: 1.0; color: #1f2937;">MFRスマート電源管理システム</span>
    </div>
    """
    st.markdown(logo_html, unsafe_allow_html=True)
except:
    st.title("MFRスマート電源管理システム")

st.write(f"現在時刻: **{now.strftime('%Y/%m/%d %H:%M:%S')}** (10秒ごとに自動更新中 🔄)")

st.subheader("🔔 Edge通知・アラート音")

render_monitor_activation()

if active_alerts:
    primary_alert = active_alerts[0]
    start_browser_alarm(
        primary_alert["id"],
        primary_alert["title"],
        primary_alert["message"],
    )

    overdue_minutes = max(
        0,
        int((now - primary_alert["due"]).total_seconds() // 60),
    )
    overdue_time_text = format_remaining_time(overdue_minutes)
    st.markdown(
        f"""
        <div class="mfr-active-alert">
            <div style="font-size:1.7rem;font-weight:800;">{primary_alert["title"]}</div>
            <div style="font-size:1.25rem;margin-top:8px;">{primary_alert["message"]}</div>
            <div style="font-size:1rem;margin-top:8px;">予定から {overdue_time_text} 経過</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button(
        "✅ 確認しました（通知音を停止）",
        key=f"ack_{primary_alert['id']}",
        type="primary",
    ):
        st.session_state.acknowledged_alerts.append(primary_alert["id"])
        if primary_alert["kind"] == "power_off":
            st.session_state.pending_power_off_due = None
        save_state()
        stop_browser_alarm()
        st.rerun()

    if len(active_alerts) > 1:
        with st.expander(f"ほかに未確認の通知が {len(active_alerts) - 1} 件あります"):
            for pending in active_alerts[1:]:
                st.write(
                    f"・{pending['due'].strftime('%m/%d %H:%M')} "
                    f"{pending['title']}：{pending['message']}"
                )
else:
    stop_browser_alarm()
    st.success("✅ 現在、未確認のアラートはありません。")

st.caption("※シフト開始時に青いボタンを1回押してください。Edgeは閉じず、Excelの後ろで開いたままにします。")
st.markdown("---")

# --- MFR電源ステータス ---
st.header("💡 MFR測定器 電源ステータス") # ★ headerに格上げ
is_monday = (today_date.weekday() == 0)

inspection_start_time = datetime.combine(today_date, dt_time(8 if is_monday else 7, 0, 0))
inspection_end_time = datetime.combine(today_date, dt_time(10, 0, 0))

if st.session_state.last_inspection_date == today_date:
    st.success("✅ 本日の日常点検は完了しています。")
else:
    if now >= inspection_start_time:
        if is_monday:
            st.error("⚠️ 【至急】本日の日常点検が未完了です！ MFR電源をONにして点検を実施してください。（月曜は朝8:00）")
        else:
            st.error("⚠️ 【至急】本日の日常点検が未完了です！ MFR電源をONにして点検を実施してください。（火〜日は朝7:00）")
        if st.button("📝 点検が終わったので完了を記録する"):
            st.session_state.last_inspection_date = today_date
            st.session_state.pending_power_off_due = now + timedelta(minutes=10)
            save_state()
            st.rerun()
    else:
        if is_monday:
            st.warning("📋 本日の日常点検が未完了です。（月曜は朝8:00開始）")
        else:
            st.warning("📋 本日の日常点検が未完了です。（火〜日は朝7:00開始）")

st.markdown("---")

if not valid_upcoming:
    st.success("💤 **電源OFF推奨** (現在、稼働中で測定予定のジョブはありません)")
else:
    next_measure = valid_upcoming[0]
    time_diff = next_measure['est_time'] - now
    minutes_until = time_diff.total_seconds() / 60
    
    if next_measure['target_qty'] == '日常点検': meas_text = '日常点検'
    else: meas_text = f"{get_measurement_text(len(next_measure['Targets']), next_measure['target_qty'], next_measure['Targets'])}の測定"

    remaining_time_text = format_remaining_time(minutes_until)

    if minutes_until <= 60:
        st.error(
            f"🔥 **電源ON（加熱開始・維持）** "
            f"\n\n次回の測定まで約 {remaining_time_text} です。 "
            f"({next_measure['machine']}の{meas_text})"
        )
    elif minutes_until >= 90:
        st.success(
            f"💤 **電源OFF推奨（待機）** "
            f"\n\n次回の測定まで約 {remaining_time_text} あります。"
            "ゆっくり冷まして設備負担を軽減してください。"
        )
    else:
        st.warning(
            f"⚠️ **まもなくON（待機）** "
            f"\n\n次回の測定まで約 {remaining_time_text} です。"
            "現在はOFFのままで問題ありません。"
        )
st.markdown("---")

# --- UI：成型機コントロールパネル ---
cols_top = st.columns(3)
machine_data = {}

for idx, machine in enumerate(['100t', '450t', '550t']):
    with cols_top[idx]:
        st.header(f"⚙️ {machine} 成型機")
        job = st.session_state.jobs[machine]
        est_current = 0
        
        if job is None:
            # ★その成型機用に登録された製品だけを抽出（※機種設定がない古いデータは全成型機に表示してエラー回避）
            machine_products = [p_name for p_name, p_info in st.session_state.products.items() if p_info.get('machine', machine) == machine]
            
            if not machine_products:
                st.warning(f"⚠️ サイドバーから {machine} 用の製品マスターを登録してください。")
            else:
                product_name = st.selectbox("製品名を選択", machine_products, key=f"prod_sel_{machine}")
                prod_info = st.session_state.products[product_name]
                total_qty, cycle_time, meas_count = prod_info['qty'], prod_info['cycle'], prod_info['measurements']
                
                st.info(f"📊 **設定呼び出し:** 生産数 {total_qty}個 / サイクル {cycle_time}秒 / 測定 {meas_count}回")
                
                if meas_count == 2: targets = [1, total_qty]
                else: targets = [1, total_qty] if total_qty <= 2 else [1, total_qty // 2, total_qty]
                
                st.markdown("💡 **途中開始の場合の設定**")
                current_qty = st.number_input("現在の生産数 (0からなら0のまま)", min_value=0, max_value=int(total_qty), value=0, step=1, key=f"cur_{machine}")
                default_completed = [t for t in targets if t <= current_qty]
                completed = st.multiselect("既に測定済みのポイント", options=targets, default=default_completed, format_func=lambda x: f"{x}個目", key=f"comp_sel_{machine}")

                if st.button("▶️ 生産スタート", key=f"start_btn_{machine}"):
                    start_timestamp = datetime.utcnow() + timedelta(hours=9)
                    st.session_state.jobs[machine] = {
                        'job_id': f"{machine}_{start_timestamp.strftime('%Y%m%d%H%M%S')}",
                        'product_name': product_name,
                        'total_qty': total_qty,
                        'cycle_time': cycle_time,
                        'current_qty': current_qty,
                        'last_update': start_timestamp,
                        # 生産スタート＝MFR加熱開始。
                        # 初回MFR測定は必ず60分後以降。
                        'heat_ready_at': (
                            start_timestamp
                            + timedelta(minutes=MFR_WARMUP_MINUTES)
                        ),
                        'targets': targets,
                        'completed': completed,
                        'status': 'Running'
                    }
                    save_state(); st.rerun()
        else:
            status_color = "🟢" if job['status'] == 'Running' else ("🟡" if job['status'] == 'Paused' else "✅")
            st.write(f"状態: {status_color} **{job['status']}**")
            p_name = job.get('product_name', '設定なし')
            st.write(f"製品: **{p_name}** ({job['total_qty']}個 / サイクル: {job['cycle_time']}秒)")

            if job['status'] == 'Running':
                elapsed_sec = ((datetime.utcnow() + timedelta(hours=9)) - job['last_update']).total_seconds()
                est_current = min(int(job['current_qty'] + (elapsed_sec / job['cycle_time'])), job['total_qty'])
            else:
                est_current = job['current_qty']
                
            st.metric("現在生産数 (推測)", f"{est_current} / {job['total_qty']}")
            
            if job['status'] != 'Completed':
                col_ctrl1, col_ctrl2 = st.columns(2)
                with col_ctrl1:
                    if job['status'] == 'Running':
                        if st.button("⏸️ 一時停止", key=f"pause_main_{machine}"):
                            job['current_qty'] = est_current; job['status'] = 'Paused'; save_state(); st.rerun()
                    elif job['status'] == 'Paused':
                        if st.button("▶️ 再開", key=f"resume_main_{machine}"):
                            job['last_update'] = (datetime.utcnow() + timedelta(hours=9)); job['status'] = 'Running'; save_state(); st.rerun()
                with col_ctrl2:
                    if st.button("⏹️ 生産終了", key=f"stop_main_{machine}"):
                        st.session_state.jobs[machine] = None; save_state(); st.rerun()

            if job['status'] == 'Completed':
                if st.button("🔄 次の製品の生産をセット", key=f"next_ok_{machine}"):
                    st.session_state.jobs[machine] = None; save_state(); st.rerun()

            st.divider()
            st.markdown('<div class="mfr-status-header">📋 MFR測定状況：</div>', unsafe_allow_html=True)
            num_targets = len(job['targets'])
            for t in job['targets']:
                meas_text = get_measurement_text(num_targets, t, job['targets'])
                if t in job['completed']: st.write(f"✅ {meas_text} ー 測定完了")
                else:
                    if st.button(f"🎯 {meas_text} ー 測定完了を記録", key=f"comp_{machine}_{t}"):
                        if job['status'] == 'Running':
                            elapsed_sec = ((datetime.utcnow() + timedelta(hours=9)) - job['last_update']).total_seconds()
                            job['current_qty'] = min(int(job['current_qty'] + (elapsed_sec / job['cycle_time'])), job['total_qty'])
                            job['last_update'] = (datetime.utcnow() + timedelta(hours=9))
                            
                        job['completed'].append(t)
                        # 実際の測定完了から10分後に電源OFF候補を作成。
                        # 90分以内に次の測定がある場合は、次回更新時に自動取消します。
                        st.session_state.pending_power_off_due = (
                            datetime.utcnow() + timedelta(hours=9, minutes=10)
                        )
                        if len(job['completed']) == len(job['targets']): 
                            job['status'] = 'Completed'
                            job['current_qty'] = job['total_qty']
                        save_state(); st.rerun()

        machine_data[machine] = {'job': job, 'est_current': est_current}

# 下段パネル
cols_bottom = st.columns(3)
for idx, machine in enumerate(['100t', '450t', '550t']):
    with cols_bottom[idx]:
        st.divider() 
        job = machine_data[machine]['job']
        est_current = machine_data[machine]['est_current']
        
        with st.expander("🔧 実績の補正・サイクル微調整", expanded=False):
            adjust_qty_value = est_current if job is not None else 0
            adjust_cycle_value = float(job['cycle_time']) if job is not None else 30.0
            
            st.markdown("💡 **① 個数のズレを修正**")
            new_qty = st.number_input("現在の実際の個数", min_value=0, max_value=job['total_qty'] if job is not None else 999999, value=adjust_qty_value, step=1, key=f"adj_qty_{machine}")
            if st.button("💾 個数を上書き更新", key=f"update_qty_{machine}"):
                if job is not None:
                    job['current_qty'] = new_qty
                    job['last_update'] = (datetime.utcnow() + timedelta(hours=9))
                    save_state(); st.rerun()
                else:
                    st.warning("稼働していません。")
            
            st.markdown("---")
            
            st.markdown("💡 **② サイクル(生産ペース)の変更**")
            new_cycle = st.number_input("サイクルタイム微調整(秒)", min_value=1.0, value=adjust_cycle_value, step=0.1, key=f"adj_cyc_{machine}")
            if st.button("💾 サイクルのみ変更", key=f"update_cyc_{machine}"):
                if job is not None:
                    job['current_qty'] = est_current 
                    job['cycle_time'] = new_cycle
                    job['last_update'] = (datetime.utcnow() + timedelta(hours=9))
                    save_state(); st.rerun()
                else:
                    st.warning("稼働していません。")
st.markdown("---")

# --- UI：シフト別スケジュール表 ---
def get_shift_name(dt):
    h = dt.hour
    if 7 <= h < 15: return "A勤"
    elif 15 <= h < 23: return "B勤"
    else: return "C勤"

st.header("🗓️ 各勤務の電源操作・作業フロー 一覧") # ★ headerに格上げ
if on_blocks:
    html = "<table style='width:100%; border-collapse: collapse; font-size: 20px; text-align: center; margin-bottom: 20px;'>"
    html += "<tr style='background-color: #f3f4f6; color: #111; font-weight: bold; border-bottom: 3px solid #ccc;'><th style='padding: 15px; border: 1px solid #ddd; width: 10%;'>状態</th><th style='padding: 15px; border: 1px solid #ddd; width: 30%;'>電源ON担当・ON時刻</th><th style='padding: 15px; border: 1px solid #ddd;'>作業フロー</th></tr>"
    for b_start, b_end in on_blocks:
        status_text = "完了" if b_end < now else ("進行中" if b_start <= now <= b_end else "予定")
        bg_color = "#e6ffe6" if status_text == "完了" else ("#fffdeb" if status_text == "進行中" else "#ffffff")
        on_assignee = get_shift_name(b_start)
        on_time = b_start.strftime('%m/%d %H:%M')
        
        tasks_in_flow = []
        for pt in valid_upcoming:
            if b_start <= pt['est_time'] <= b_end:
                if pt['machine'] == '日常点検(A勤)': tasks_in_flow.append("日常点検")
                else: tasks_in_flow.append(f"{pt['machine']}MFR測定({get_measurement_text(len(pt['Targets']), pt['target_qty'], pt['Targets'])})")
        
        flow_full_text = " ➡ ".join(tasks_in_flow) + " ➡ OFF" if tasks_in_flow else "➡ OFF (測定なし)"
        flow_full_html = f"<span style='color: #000; font-size: 22px;'>➡</span> {flow_full_text}"
        
        html += f"<tr style='background-color: {bg_color}; border-bottom: 1px solid #ddd;'><td style='padding: 15px; font-weight: bold;'>{status_text}</td><td style='padding: 15px; font-weight: bold;'><span style='color: #d32f2f; font-size: 24px;'>🔥 ON: </span> {on_assignee} ({on_time})</td><td style='padding: 15px; font-weight: bold; text-align: left;'>{flow_full_html}</td></tr>"
    html += "</table>"
    st.markdown(html, unsafe_allow_html=True)
else:
    st.info("現在、予定されている電源操作はありません。")

# --- UI：全体可視化グラフ ---
st.header("📈 成型機稼働状況・MFR電源スケジュール") # ★ headerに格上げ

timeline_data = []
measurement_points = []

for machine, job in st.session_state.jobs.items():
    if job is None: continue
    start_time = job['last_update']
    end_time = (datetime.utcnow() + timedelta(hours=9)) if job['status'] == 'Completed' else job['last_update'] + timedelta(seconds=(job['total_qty'] - job['current_qty']) * job['cycle_time'])
    timeline_data.append({'Task': machine, 'Start': start_time, 'End': end_time, 'Status': job['status'], 'Targets': job['targets']})

    for t in job['targets']:
        is_completed = t in job['completed']

        if is_completed:
            # 完了済みマークは従来どおりの表示位置を維持する。
            if (
                job['status'] != 'Running'
                or (t - job['current_qty']) <= 0
            ):
                t_time = job['last_update']
            else:
                t_time = (
                    job['last_update']
                    + timedelta(
                        seconds=(
                            (t - job['current_qty'])
                            * job['cycle_time']
                        )
                    )
                )
            point_status = 'Completed'
        else:
            # 未完了の黄色◆は通知と完全に同じ測定予定時刻を使う。
            t_time = calculate_planned_measurement_time(job, t)

            # 一時停止中は測定予定時刻が確定しないので表示しない。
            if t_time is None:
                continue

            point_status = 'Planned'

        measurement_points.append({
            'Task': machine,
            'Time': t_time,
            'Target_Qty': t,
            'Targets': job['targets'],
            'Status': point_status,
        })

today_start = datetime.combine(now.date(), dt_time.min)

if st.session_state.last_inspection_date == today_date:
    inspection_time = datetime(now.year, now.month, now.day, 8 if is_monday else 7, 0, 0)
    measurement_points.append({'Task': 'MFR電源', 'Time': inspection_time, 'Target_Qty': '点検済', 'Targets': ['点検済'], 'Status': 'Completed'})

for pt in valid_upcoming:
    if pt['machine'] == '日常点検(A勤)':
        measurement_points.append({'Task': 'MFR電源', 'Time': pt['est_time'], 'Target_Qty': '日常点検', 'Targets': ['日常点検'], 'Status': 'Planned'})

for b_start, b_end in on_blocks:
    timeline_data.append({'Task': 'MFR電源', 'Start': max(b_start, now), 'End': max(b_end, now), 'Status': 'ON'})

DUMMY_DATE = datetime(2000, 1, 1)
def time_to_dummy(dt):
    return datetime.combine(DUMMY_DATE, dt.time()) if isinstance(dt, datetime) else datetime.combine(DUMMY_DATE, dt)

def get_date_str(dt):
    weekdays = ['月', '火', '水', '木', '金', '土', '日']
    return f"{dt.strftime('%m/%d')} ({weekdays[dt.weekday()]})"

new_timeline_data = []
overall_end_time = now + timedelta(hours=1) 

for d in timeline_data:
    if d['End'] < today_start: continue
    if d['End'] > overall_end_time: overall_end_time = d['End']
    curr_start = max(d['Start'], today_start)
    end_time = max(d['End'], curr_start)

    while curr_start.date() < end_time.date():
        eod = datetime.combine(curr_start.date(), datetime.max.time())
        new_timeline_data.append({'Task': d['Task'], 'StartDummy': time_to_dummy(curr_start), 'EndDummy': time_to_dummy(eod), 'Status': d['Status'], 'DateStr': get_date_str(curr_start)})
        curr_start = datetime.combine(curr_start.date() + timedelta(days=1), datetime.min.time())
        
    if curr_start <= end_time:
        new_timeline_data.append({'Task': d['Task'], 'StartDummy': time_to_dummy(curr_start), 'EndDummy': time_to_dummy(end_time), 'Status': d['Status'], 'DateStr': get_date_str(curr_start)})

new_measurement_points = []
for pt in measurement_points:
    if pt['Time'] < today_start: continue
    if pt['Time'] > overall_end_time: overall_end_time = pt['Time']
    new_measurement_points.append({'Task': pt['Task'], 'TimeDummy': time_to_dummy(pt['Time']), 'DateStr': get_date_str(pt['Time']), 'Target_Qty': pt['Target_Qty'], 'Targets': pt.get('Targets', []), 'Status': pt['Status']})

if new_timeline_data:
    df = pd.DataFrame(new_timeline_data)
    unique_dates = sorted(list(set(df['DateStr']))) 
    
    date_to_row = {date: len(unique_dates) - i for i, date in enumerate(unique_dates)}
    
    fig = px.timeline(
        df, x_start="StartDummy", x_end="EndDummy", y="Task", color="Status", facet_row="DateStr",
        color_discrete_map={'Running': '#00a82d', 'Paused': '#f5a623', 'Completed': '#88d8b0', 'ON': '#ff3333'},
        facet_row_spacing=0.15,
        category_orders={"DateStr": unique_dates, "Task": ["MFR電源", "550t", "450t", "100t"]} 
    )
    
    fig.update_yaxes(
        title_text="", tickfont=dict(size=16, color="black", weight="bold"), 
        autorange=False, range=[3.8, -0.8],
        showline=True, linewidth=1, linecolor='gray', mirror=True
    )
    
    # 時刻表示は「05:00」ではなく「5」、「23:00」ではなく「23」と表示する。
    hour_tick_values = [
        datetime(2000, 1, 1, hour, 0, 0) for hour in range(24)
    ] + [datetime(2000, 1, 2, 0, 0, 0)]
    hour_tick_text = [str(hour) for hour in range(24)] + ["24"]

    fig.update_xaxes(
        title_text="",
        tickmode="array",
        tickvals=hour_tick_values,
        ticktext=hour_tick_text,
        tickfont=dict(size=14, color="black", weight="bold"),
        range=[datetime(2000, 1, 1, 0, 0, 0), datetime(2000, 1, 2, 0, 0, 0)],
        showgrid=True, gridcolor='rgba(150, 150, 150, 0.5)', gridwidth=1, griddash='dot',
        showticklabels=True,
        showline=True, linewidth=1, linecolor='gray', mirror=True
    )
    fig.layout.xaxis.title.text = "時間（各シフトごとの担当帯）"

    fig.add_vrect(x0=time_to_dummy(dt_time(0,0)), x1=time_to_dummy(dt_time(7,0)), fillcolor="#e6f2ff", opacity=0.4, layer="below", line_width=1, line_color="gray")
    fig.add_vrect(x0=time_to_dummy(dt_time(7,0)), x1=time_to_dummy(dt_time(15,0)), fillcolor="#fff5cc", opacity=0.4, layer="below", line_width=1, line_color="gray")
    fig.add_vrect(x0=time_to_dummy(dt_time(15,0)), x1=time_to_dummy(dt_time(23,0)), fillcolor="#e6ffe6", opacity=0.4, layer="below", line_width=1, line_color="gray")
    fig.add_vrect(x0=time_to_dummy(dt_time(23,0)), x1=time_to_dummy(dt_time(23,59,59)), fillcolor="#e6f2ff", opacity=0.4, layer="below", line_width=1, line_color="gray")

    for facet_date in unique_dates:
        row_idx = date_to_row[facet_date]
        shifts_text = [
            ("C勤", time_to_dummy(dt_time(3, 30)), 'rgba(0,68,136,0.05)'),
            ("A勤", time_to_dummy(dt_time(11, 0)), 'rgba(136,102,0,0.05)'),
            ("B勤", time_to_dummy(dt_time(19, 0)), 'rgba(0,102,0,0.05)')
        ]
        for text, x_pos, color in shifts_text:
            fig.add_annotation(
                x=x_pos, y=1.5, text=text, font=dict(size=120, color=color, weight="bold"),
                showarrow=False, xanchor="center", yanchor="middle", row=row_idx, col=1
            )
            
    today_str = get_date_str(now)
    if today_str in date_to_row:
        today_row = date_to_row[today_str]
        now_dummy_time = time_to_dummy(now)
        fig.add_vline(x=now_dummy_time, line_width=3, line_dash="dash", line_color="#ff0000", layer="above", row=today_row, col=1)
        yref_name = f"y{today_row if today_row > 1 else ''} domain"
        fig.add_annotation(
            x=now_dummy_time, y=1.02, yref=yref_name, text="▼ 現在", font=dict(size=18, color="#ff0000", weight="bold"), 
            showarrow=False, xanchor="center", yanchor="bottom", bgcolor="white", bordercolor="#ff0000", borderwidth=1, row=today_row, col=1
        )

    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1], font=dict(size=22, weight="bold", color="black")) if "=" in a.text else None)

    if new_measurement_points:
        df_pts = pd.DataFrame(new_measurement_points)
        for facet_date in unique_dates:
            row_idx = date_to_row[facet_date]
            df_pts_in_facet = df_pts[df_pts['DateStr'] == facet_date]
            if df_pts_in_facet.empty: continue
            
            df_comp = df_pts_in_facet[df_pts_in_facet['Status'] == 'Completed']
            if not df_comp.empty:
                trace_completed_text = ['点検済' if pt.get('Targets', []) and pt['Targets'][0] == '点検済' else get_measurement_text(len(pt.get('Targets', [])), pt['Target_Qty'], pt.get('Targets', [])) for pt in df_comp.to_dict('records')]
                fig.add_trace(go.Scatter(
                    x=df_comp['TimeDummy'], y=df_comp['Task'], mode='markers+text',
                    marker=dict(color='#00e6e6', size=18, symbol='circle', line=dict(width=2, color='black')),
                    text=trace_completed_text, textposition='top center', textfont=dict(size=18, color='black', weight='bold'),
                    cliponaxis=False, hoverinfo='skip', showlegend=False 
                ), row=row_idx, col=1)

            df_plan = df_pts_in_facet[df_pts_in_facet['Status'] == 'Planned']
            if not df_plan.empty:
                trace_planned_text = ['日常点検' if pt.get('Targets', []) and pt['Targets'][0] == '日常点検' else get_measurement_text(len(pt.get('Targets', [])), pt['Target_Qty'], pt.get('Targets', [])) for pt in df_plan.to_dict('records')]
                fig.add_trace(go.Scatter(
                    x=df_plan['TimeDummy'], y=df_plan['Task'], mode='markers+text',
                    marker=dict(color='#ffff00', size=20, symbol='diamond', line=dict(width=2, color='black')),
                    text=trace_planned_text, textposition='top center', textfont=dict(size=20, color='black', weight='bold'),
                    cliponaxis=False, hoverinfo='skip', showlegend=False 
                ), row=row_idx, col=1)

    fig.update_layout(
        height=max(700, len(unique_dates) * 350), margin=dict(t=120, b=50, l=100, r=50), showlegend=True,
        uirevision='constant'
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("📊 グラフを表示するための稼働中のジョブはありません。")

# --- UI：🌱EcoNavi ---
st.markdown("---")
st.header("🌱 EcoNavi")
st.write(
    "日々のこまめな電源OFF運用によって節約できる「電気代」、"
    "「ヒーター等の設備寿命延長に伴う修繕費の削減額」、"
    "および「電源管理に必要な管理工数（労務費）」を自動計算する"
    "シミュレーターです。"
)

with st.expander(
    "📊 現在のスケジュールにおける削減効果金額を計算",
    expanded=True,
):
    # 1段目：電力・設備関係の条件
    col_k, col_e, col_h, col_l = st.columns(4)

    with col_k:
        power_kw = st.number_input(
            "MFR消費電力 (kW)",
            min_value=0.0,
            value=0.80,
            step=0.10,
            format="%.2f",
            help="最大値 0.80 kW",
        )

    with col_e:
        elec_price = st.number_input(
            "電気代単価 (円/kWh)",
            min_value=0.0,
            value=25.00,
            step=1.00,
            format="%.2f",
            help="暫定単価25円/kWh",
        )

    with col_h:
        heater_cost = st.number_input(
            "修繕・メンテナンス費用 (円)",
            min_value=0,
            value=0,
            step=10000,
            help="初期値は0円です。設備費を計算する場合のみ入力してください。",
        )

    with col_l:
        heater_life_hours = st.number_input(
            "メンテナンス周期 (時間)",
            min_value=0,
            value=0,
            step=1000,
            help="初期値は0時間です。設備費を計算する場合のみ入力してください。",
        )

    # 2段目：管理工数・労務費の条件
    st.markdown("##### 👷 管理工数・労務費の条件")
    col_wage, col_manual_time, col_system_time = st.columns(3)

    with col_wage:
        labor_hourly_rate = st.number_input(
            "1時間当たりの労務費 (円/h)",
            min_value=0,
            value=4600,
            step=100,
            help=(
                "デフォルトは4,600円/hです。"
                "0円にすると、管理工数・労務費を計算から除外します。"
            ),
        )

    with col_manual_time:
        manual_minutes_per_job = st.number_input(
            "システムなしの管理時間 (分/Lot)",
            min_value=0.0,
            value=5.0,
            step=0.5,
            format="%.1f",
            help=(
                "測定時刻、電源ON/OFF時刻、3台の予定重複、"
                "申し送りを手作業で確認する時間です。"
            ),
        )

    with col_system_time:
        st.metric(
            "システム使用時の管理時間",
            "0.0 分/Lot",
            "時刻を自動算出",
            help=(
                "システムが測定時刻と電源ON/OFF時刻を自動算出するため、"
                "管理計算工数は0分として計算します。"
            ),
        )

    # 設備費または周期のどちらかが0なら、修繕費計算を完全に除外する。
    maintenance_enabled = heater_cost > 0 and heater_life_hours > 0

    # 労務費または管理時間が0なら、管理工数・労務費計算を完全に除外する。
    labor_enabled = labor_hourly_rate > 0 and manual_minutes_per_job > 0

    excluded_messages = []
    if not maintenance_enabled:
        excluded_messages.append(
            "修繕・メンテナンス費用または周期が0のため、"
            "設備寿命・修繕費"
        )
    if not labor_enabled:
        excluded_messages.append(
            "労務費または管理時間が0のため、管理工数・労務費"
        )

    if excluded_messages:
        st.info(
            "ℹ️ "
            + "、".join(excluded_messages)
            + "は計算対象外です。0円の項目は合計金額とグラフに含めません。"
        )

    if timeline_data and on_blocks:
        schedule_start = min(d["Start"] for d in timeline_data)
        schedule_end = max(d["End"] for d in timeline_data)

        total_hours = max(
            0.0,
            (schedule_end - schedule_start).total_seconds() / 3600,
        )
        new_on_hours = max(
            0.0,
            sum(
                (b_end - b_start).total_seconds()
                for b_start, b_end in on_blocks
            )
            / 3600,
        )
        saved_hours = max(0.0, total_hours - new_on_hours)

        # 現在登録されているLot数を管理工数の対象とする。
        managed_job_count = sum(
            1
            for job in st.session_state.jobs.values()
            if job is not None
        )

        if labor_enabled:
            manual_labor_hours = (
                managed_job_count * manual_minutes_per_job / 60
            )
            system_labor_hours = 0.0
            old_labor = manual_labor_hours * labor_hourly_rate
            new_labor = system_labor_hours * labor_hourly_rate
            saved_labor_cost = max(0.0, old_labor - new_labor)
        else:
            manual_labor_hours = 0.0
            system_labor_hours = 0.0
            old_labor = 0.0
            new_labor = 0.0
            saved_labor_cost = 0.0

        # 電力削減時間が0でも、管理工数削減がある場合は結果を表示する。
        if saved_hours > 0 or saved_labor_cost > 0:
            saved_cost = saved_hours * power_kw * elec_price

            if maintenance_enabled:
                maintenance_cost_per_hour = (
                    heater_cost / heater_life_hours
                )
                saved_heater_value = (
                    saved_hours * maintenance_cost_per_hour
                )
                old_maint = total_hours * maintenance_cost_per_hour
                new_maint = new_on_hours * maintenance_cost_per_hour
            else:
                maintenance_cost_per_hour = 0.0
                saved_heater_value = 0.0
                old_maint = 0.0
                new_maint = 0.0

            st.success(
                f"✨ **現在のスケジュール期間中"
                f"（約 {total_hours:.1f} 時間・"
                f"{managed_job_count} Lot）の改善効果**"
            )

            res_col1, res_col2, res_col3, res_col4 = st.columns(4)

            help_time = (
                "【計算式】\n"
                "従来OFFにしていなかった全期間の時間"
                " － 今回のスケジュールでONになっている時間"
            )
            help_elec = (
                "【計算式】\n"
                "削減できた待機時間 × MFR消費電力(kW)"
                " × 電気代単価"
            )
            help_maint = (
                "【計算式】\n"
                "削減できた待機時間 × "
                "(修繕・メンテナンス費用 ÷ メンテナンス周期)\n\n"
                "※費用または周期を0にすると、この計算を除外します。"
            )
            help_labor = (
                "【システムなし】\n"
                "現在のLot数 × 手作業の管理時間(分/Lot)"
                " ÷ 60 × 労務費(円/h)\n\n"
                "【システム使用】\n"
                "測定時刻・電源ON/OFF時刻を自動算出するため0円\n\n"
                "※労務費または管理時間を0にすると、"
                "この計算を除外します。"
            )

            res_col1.metric(
                "無駄な待機時間の削減",
                f"{saved_hours:.1f} 時間",
                (
                    f"従来: {total_hours:.1f}h"
                    f" → 今回: {new_on_hours:.1f}h"
                ),
                delta_color="inverse",
                help=help_time,
            )

            res_col2.metric(
                "電気代の削減",
                f"{int(saved_cost):,} 円",
                f"▲ {int(saved_cost):,}円",
                delta_color="inverse",
                help=help_elec,
            )

            if maintenance_enabled:
                res_col3.metric(
                    "設備寿命(修繕費)の節約換算",
                    f"{int(saved_heater_value):,} 円",
                    "部品の長寿命化による効果",
                    help=help_maint,
                )
            else:
                res_col3.metric(
                    "設備寿命(修繕費)",
                    "計算対象外",
                    "0設定のため除外",
                    help=help_maint,
                )

            if labor_enabled:
                res_col4.metric(
                    "管理工数(労務費)の削減",
                    f"{int(saved_labor_cost):,} 円",
                    (
                        f"手動: {manual_labor_hours:.2f}h"
                        f" → システム: {system_labor_hours:.2f}h"
                    ),
                    delta_color="inverse",
                    help=help_labor,
                )
            else:
                res_col4.metric(
                    "管理工数(労務費)",
                    "計算対象外",
                    "0設定のため除外",
                    help=help_labor,
                )

            included_items = ["電気代"]
            if maintenance_enabled:
                included_items.append("設備寿命（修繕費）")
            if labor_enabled:
                included_items.append("管理工数（労務費）")

            st.caption(
                "※"
                + "・".join(included_items)
                + "の概算を、現在のスケジュールを基に計算しています。"
            )

            if labor_enabled:
                st.caption(
                    "※管理工数は、システムを使用せず必要時のみ電源管理を"
                    "行う場合に発生する、測定時刻・電源ON/OFF時刻・"
                    "3台の予定重複・申し送りの確認工数を、"
                    f"1Lot当たり {manual_minutes_per_job:.1f} 分として"
                    "換算した回避効果です。"
                )

            # --- 可視化グラフ ---
            st.markdown("<br>", unsafe_allow_html=True)

            old_elec = total_hours * power_kw * elec_price
            new_elec = new_on_hours * power_kw * elec_price

            total_old = old_elec + old_maint + old_labor
            total_new = new_elec + new_maint + new_labor
            saved_total = max(0.0, total_old - total_new)

            old_label = "❌ 改善前相当<br>(連続ON＋手動管理)"
            new_label = "✨ システム運用<br>(必要時のみON)"

            eco_rows = [
                {
                    "運用方法": old_label,
                    "コスト内訳": "電気代",
                    "金額": old_elec,
                },
                {
                    "運用方法": new_label,
                    "コスト内訳": "電気代",
                    "金額": new_elec,
                },
            ]

            if maintenance_enabled:
                eco_rows.extend(
                    [
                        {
                            "運用方法": old_label,
                            "コスト内訳": "修繕費 (寿命換算)",
                            "金額": old_maint,
                        },
                        {
                            "運用方法": new_label,
                            "コスト内訳": "修繕費 (寿命換算)",
                            "金額": new_maint,
                        },
                    ]
                )

            # 労務費が0の場合は、行自体を追加せずグラフから完全に除外する。
            if labor_enabled:
                eco_rows.extend(
                    [
                        {
                            "運用方法": old_label,
                            "コスト内訳": "管理工数 (労務費)",
                            "金額": old_labor,
                        },
                        {
                            "運用方法": new_label,
                            "コスト内訳": "管理工数 (労務費)",
                            "金額": new_labor,
                        },
                    ]
                )

            df_eco = pd.DataFrame(eco_rows)

            chart_title = (
                "<b>📊 システム運用による総合コスト削減効果</b>"
                if maintenance_enabled or labor_enabled
                else "<b>📊 システム運用による電気代削減効果</b>"
            )

            fig_eco = px.bar(
                df_eco,
                x="運用方法",
                y="金額",
                color="コスト内訳",
                text="金額",
                color_discrete_map={
                    "電気代": "#f4a261",
                    "修繕費 (寿命換算)": "#e76f51",
                    "管理工数 (労務費)": "#457b9d",
                },
            )

            # 金額が小さい区分でも文字を縮小せず、常に同じ大きさで表示する。
            # 棒の中に収まらない場合は自動的に外側へ移動する。
            fig_eco.update_traces(
                texttemplate="<b>%{text:,.0f} 円</b>",
                textposition="auto",
                textangle=0,
                insidetextfont=dict(size=18, color="white"),
                outsidetextfont=dict(size=18, color="#111111"),
                constraintext="none",
                cliponaxis=False,
            )

            # 全費用が0でもPlotlyで0除算しないよう、最低1円幅を確保する。
            y_axis_max = max(max(total_old, total_new) * 1.5, 1.0)

            fig_eco.update_layout(
                barmode="stack",
                # Plotlyの自動縮小を無効化し、すべての金額ラベルを18pxで統一する。
                uniformtext=dict(minsize=18, mode="show"),
                height=590,
                title=dict(text=chart_title, font=dict(size=22)),
                xaxis_title="",
                yaxis_title="発生コスト（円）",
                yaxis=dict(
                    range=[0, y_axis_max],
                    tickfont=dict(size=14, weight="bold"),
                ),
                xaxis=dict(tickfont=dict(size=17, weight="bold")),
                legend=dict(
                    title="<b>コスト内訳</b>",
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                    font=dict(size=14, weight="bold"),
                ),
                margin=dict(t=90, b=70, l=50, r=50),
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(250, 250, 250, 1)",
                yaxis_showgrid=True,
                yaxis_gridcolor="rgba(200,200,200,0.5)",
            )

            fig_eco.add_annotation(
                x=old_label,
                y=total_old,
                yshift=15,
                yanchor="bottom",
                text=f"<b>計 {int(total_old):,} 円</b>",
                showarrow=False,
                font=dict(size=22),
            )

            fig_eco.add_annotation(
                x=new_label,
                y=total_new,
                yshift=15,
                yanchor="bottom",
                text=f"<b>計 {int(total_new):,} 円</b>",
                showarrow=False,
                font=dict(size=22, color="#00a82d"),
            )

            approx_dx_px = 500
            approx_dy_px = (
                ((total_old - total_new) / y_axis_max) * 400
            )
            angle_deg = int(
                math.degrees(
                    math.atan2(approx_dy_px, approx_dx_px)
                )
            )

            fig_eco.add_annotation(
                x=0.5,
                y=(total_old + total_new) / 2,
                xref="paper",
                yref="y",
                text=(
                    "<span style='font-size:80px;color:#e63946;"
                    "text-shadow:2px 2px 3px rgba(0,0,0,0.2);'>"
                    "➡</span>"
                ),
                showarrow=False,
                textangle=angle_deg,
            )

            fig_eco.add_annotation(
                x=0.5,
                y=max(
                    max(total_old, total_new) * 1.15,
                    y_axis_max * 0.75,
                ),
                xref="paper",
                yref="y",
                yanchor="bottom",
                text=(
                    "<b>✨ 削減効果</b><br><br>"
                    "<b><span style='font-size:42px;color:#d00000;'>"
                    f"▲ {int(saved_total):,} 円"
                    "</span></b>"
                ),
                showarrow=False,
                font=dict(size=22, color="#111"),
                bgcolor="#fffdeb",
                bordercolor="#e63946",
                borderwidth=3,
                borderpad=15,
            )

            st.plotly_chart(fig_eco, use_container_width=True)

            # 計算内訳を画面上でも確認できるように表示する。
            with st.expander("🧮 管理工数・労務費の計算内訳", expanded=False):
                if labor_enabled:
                    st.code(
                        f"対象Lot数：{managed_job_count} Lot\n"
                        f"システムなし："
                        f"{managed_job_count} Lot × "
                        f"{manual_minutes_per_job:.1f}分 ÷ 60分 × "
                        f"{labor_hourly_rate:,}円/h"
                        f" ＝ {int(old_labor):,}円\n"
                        f"システム使用：自動算出のため "
                        f"{int(new_labor):,}円\n"
                        f"管理工数削減："
                        f"{int(old_labor):,}円 － {int(new_labor):,}円"
                        f" ＝ {int(saved_labor_cost):,}円"
                    )
                else:
                    st.write(
                        "労務費または管理時間が0のため、"
                        "管理工数・労務費は計算対象外です。"
                    )

        else:
            st.info(
                "現在のスケジュールでは、電源OFFによる削減時間と"
                "管理工数の削減効果がありません。"
            )
    else:
        st.write(
            "稼働中のジョブを登録すると、ここに削減効果金額が表示されます。"
        )
