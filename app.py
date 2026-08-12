# Version 1.6.30: 生産終了ボタンは未測定が残っていても即時終了・レジューム保存復元を再確認／旧測定必須ダイアログを無効化
# Version 1.6.29: 稼働中の成型機状態を専用GitHubブランチへ自動保存し、コード更新・再起動後も直前状態を復元
# Version 1.6.28: 起動チャイム点滅ボタンのクリック処理を修正・親画面Storage例外で停止しない堅牢化
# Version 1.6.27: 起動チャイムボタンを未確認時点滅・確認後は落ち着いた表示へ変更／同一Edgeセッション中は確認状態を維持
# Version 1.6.26: Windows通知を廃止し、チャイム音のみで運用・起動ボタンのクリック診断表示を追加
# Version 1.6.25: 通知時の最上部スクロールをStreamlit内部スクロール領域まで確実に戻す方式へ修正
# Version 1.6.24: 測定記録未入力時の10分後フォロー通知・新規アラート時はページ最上部へ自動スクロール
# Version 1.6.23: MFR測定記録後のOFF通知を即時化・次にやることへ即時OFFを反映・過去予定によるOFF取消を防止
# Version 1.6.22: 実機MFRが測定可能済みなら新規Lotの「始」を即時測定にする判定を追加
# Version 1.6.21: 新規アラート発生時に通知欄へ自動スクロール・生産終了後は自動で停止中へ戻す
# Version 1.6.20: Cost Saving週次グラフを6週固定枠表示・未実績の将来週も週枠と週ラベルを先行表示
# Version 1.6.19: ダイアログ催促音を高音3連パルスへ強化・Cost Saving全削除後のUI状態を自動リセット
# Version 1.6.18: 確認ダイアログ催促音を高音域へ変更（成形室の騒音下で気づきやすい音色）
# Version 1.6.17: 確認ダイアログ専用の催促音を追加（応答まで繰返し・通常アラート音と分離）
# Version 1.6.16: Cost Saving履歴の個別削除・週単位削除・全削除と削除後自動再集計を追加
# Version 1.6.15: EcoNaviとCost Savingの表示順を入れ替え（EcoNaviを上、Cost Savingを下）
# Version 1.6.14: Cost Saving週次グラフを週別グループ棒＋累計折れ線へ変更・少数週でも横幅を固定
# Version 1.6.13: OFF通知文言改善・生産終了前のMFR測定記録必須化・Cost Saving週次グラフを複合表示へ改善
# Version 1.6.12: Cost Saving実績管理を追加（生産/電源履歴・週次/日次効果・GitHub自動保存）
# Version 1.6.11: ヘッダーへVer表示を追加・成型中/生産終了バッジを大型化・成型中アイコンを回転矢印へ変更
# Version 1.6.10: 「次にやること」のMFR測定表示を「始／中／終 測定」に統一
# Version 1.6.9: 「次にやること」をタイムラインのONバーと完全同期・電源操作と測定を時刻順に左右自動並べ替え
# Version 1.6.8: 今後予定を「次の電源操作・次のMFR測定」に集約／電源OFF確認後に表示札記入確認ダイアログ
# Version 1.6.7: 色弱でも判別しやすい配色へ全面調整（青=正常/完了、黄橙=要操作、赤=アラート、灰=停止）
# Version 1.6.6: MFR測定ボタンを未測定=オレンジ・測定済み=緑へ色分けし、状態が明確な文言へ変更
# Version 1.6.5: 始・中のMFR測定完了を再押下で取消可能・通知履歴と電源ONバーも復元
# Version 1.6.4: 上部UI再整理・成型中回転表示・測定アラート確認で測定完了・最終測定後に生産終了確認
# Version 1.6.3: 現場操作画面を簡潔化・実機MFR電源確認ダイアログをシンプル化
# Version 1.6.2: 監視開始後の緑ボタンから「監視開始」表記を削除・測定回数は製品マスター登録値を優先
# Current spec: MFR測定回数は成型機固定ではなく、製品マスターの measurements（2回／3回）を使用
# Version 1.6.1: 生産開始時に実機MFR電源ON/OFF確認ダイアログを追加
# Version 1.6.0: 新規生産時のONアラート欠落を修正・ON状態管理とアラートIDを再設計
# Version 1.5.9: 加熱中の電源ONアラート再発行を防止・550tの2回測定設定を維持
# Version 1.5.7: 「▼ 現在」の三角位置を点線上へ修正
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
from plotly.subplots import make_subplots
import pandas as pd
from datetime import datetime, timedelta, time as dt_time, date
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


# --- 稼働状態のクラウド保存（コード更新・再起動対策） ---
# main ブランチへ頻繁に状態を書き込むとアプリの再デプロイにつながる可能性があるため、
# 稼働状態だけ専用ブランチへ保存する。
RUNTIME_STATE_FILE = "mfr_runtime_state.json"
RUNTIME_STATE_BRANCH = "mfr-runtime-state"
RUNTIME_STATE_SCHEMA_VERSION = 1


def _runtime_json_encode(value):
    """datetime/dateを含む稼働状態をJSON保存可能な形式へ変換する。"""
    if isinstance(value, datetime):
        return {
            "__mfr_runtime_type__": "datetime",
            "value": value.isoformat(),
        }
    if isinstance(value, date):
        return {
            "__mfr_runtime_type__": "date",
            "value": value.isoformat(),
        }
    if isinstance(value, dict):
        return {
            str(key): _runtime_json_encode(item)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [_runtime_json_encode(item) for item in value]

    # numpy等のスカラーが入った場合も通常のPython値へ変換する。
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            pass
    return value


def _runtime_json_decode(value):
    """クラウド保存したdatetime/dateをPython値へ復元する。"""
    if isinstance(value, dict):
        runtime_type = value.get("__mfr_runtime_type__")
        raw_value = value.get("value")
        if runtime_type == "datetime" and raw_value:
            try:
                return datetime.fromisoformat(str(raw_value))
            except (TypeError, ValueError):
                return None
        if runtime_type == "date" and raw_value:
            try:
                return date.fromisoformat(str(raw_value))
            except (TypeError, ValueError):
                return None
        return {
            key: _runtime_json_decode(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_runtime_json_decode(item) for item in value]
    return value


def ensure_runtime_state_branch():
    """稼働状態専用ブランチがなければmainから1回だけ作成する。"""
    if not GITHUB_TOKEN:
        return False

    api_base = f"https://api.github.com/repos/{GITHUB_REPO}"
    branch_ref_url = (
        f"{api_base}/git/ref/heads/{RUNTIME_STATE_BRANCH}"
    )

    try:
        req = urllib.request.Request(branch_ref_url)
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
        with urllib.request.urlopen(req, timeout=10):
            pass
        return True
    except Exception:
        pass

    try:
        main_ref_url = f"{api_base}/git/ref/heads/main"
        req_main = urllib.request.Request(main_ref_url)
        req_main.add_header("Authorization", f"token {GITHUB_TOKEN}")
        with urllib.request.urlopen(req_main, timeout=10) as res:
            main_sha = json.loads(res.read().decode("utf-8"))["object"]["sha"]

        create_url = f"{api_base}/git/refs"
        create_payload = {
            "ref": f"refs/heads/{RUNTIME_STATE_BRANCH}",
            "sha": main_sha,
        }
        req_create = urllib.request.Request(
            create_url,
            data=json.dumps(create_payload).encode("utf-8"),
            method="POST",
        )
        req_create.add_header("Authorization", f"token {GITHUB_TOKEN}")
        req_create.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req_create, timeout=15):
            pass
        return True
    except Exception:
        # 同時作成などでPOSTが失敗しても、ブランチが存在すれば成功扱い。
        try:
            req = urllib.request.Request(branch_ref_url)
            req.add_header("Authorization", f"token {GITHUB_TOKEN}")
            with urllib.request.urlopen(req, timeout=10):
                pass
            return True
        except Exception as e:
            print("稼働状態ブランチ準備エラー:", e)
            return False


def _build_runtime_state_payload(state_dict):
    """クラウドへ保存する稼働中状態だけを抽出する。"""
    runtime_keys = [
        "jobs",
        "last_inspection_date",
        "acknowledged_alerts",
        "pending_power_off_due",
        "pending_power_off_context",
        "pending_measurement_required_before_finish",
        "pending_production_finish_confirmation",
        "pending_signboard_confirmation",
        "mfr_power_is_on",
        "mfr_power_on_confirmed_at",
        "mfr_power_state_version",
    ]

    saved_at = state_dict.get("state_saved_at")
    if not isinstance(saved_at, datetime):
        saved_at = datetime.utcnow() + timedelta(hours=9)

    runtime_state = {
        key: state_dict.get(key)
        for key in runtime_keys
    }

    return {
        "schema_version": RUNTIME_STATE_SCHEMA_VERSION,
        "saved_at": saved_at.isoformat(),
        "app_version": str(globals().get("APP_VERSION", "")),
        "state": _runtime_json_encode(runtime_state),
    }


def load_runtime_state_from_github():
    """専用ブランチから直近の稼働状態を取得する。"""
    if not GITHUB_TOKEN or not ensure_runtime_state_branch():
        return None

    try:
        api_url = (
            f"https://api.github.com/repos/{GITHUB_REPO}/contents/"
            f"{RUNTIME_STATE_FILE}?ref={RUNTIME_STATE_BRANCH}"
        )
        req = urllib.request.Request(api_url)
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode("utf-8"))
            content = base64.b64decode(data["content"]).decode("utf-8")
            payload = json.loads(content)

        runtime_state = _runtime_json_decode(payload.get("state", {}))
        if not isinstance(runtime_state, dict):
            return None

        saved_at_text = payload.get("saved_at")
        try:
            runtime_state["state_saved_at"] = datetime.fromisoformat(
                str(saved_at_text)
            )
        except (TypeError, ValueError):
            runtime_state["state_saved_at"] = None

        runtime_state["runtime_state_source"] = "github"
        return runtime_state
    except Exception:
        # 初回はファイル未作成なのでNoneで正常。
        return None


def save_runtime_state_to_github(state_dict):
    """現在の稼働状態を専用ブランチへ保存する。"""
    if not GITHUB_TOKEN or not ensure_runtime_state_branch():
        return False

    try:
        api_url = (
            f"https://api.github.com/repos/{GITHUB_REPO}/contents/"
            f"{RUNTIME_STATE_FILE}"
        )

        sha = None
        try:
            req_check = urllib.request.Request(
                f"{api_url}?ref={RUNTIME_STATE_BRANCH}"
            )
            req_check.add_header("Authorization", f"token {GITHUB_TOKEN}")
            with urllib.request.urlopen(req_check, timeout=10) as res:
                sha = json.loads(res.read().decode("utf-8")).get("sha")
        except Exception:
            pass

        payload_data = _build_runtime_state_payload(state_dict)
        encoded = base64.b64encode(
            json.dumps(
                payload_data,
                ensure_ascii=False,
                indent=2,
            ).encode("utf-8")
        ).decode("utf-8")

        payload = {
            "message": "Update MFR Runtime State",
            "content": encoded,
            "branch": RUNTIME_STATE_BRANCH,
        }
        if sha:
            payload["sha"] = sha

        req = urllib.request.Request(
            api_url,
            data=json.dumps(payload).encode("utf-8"),
            method="PUT",
        )
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=15):
            pass
        return True
    except Exception as e:
        print("稼働状態GitHubセーブエラー:", e)
        return False


def _get_state_saved_at(state_dict, local_file_path=None):
    """状態データの保存時刻を取得する。旧pickleはファイル更新時刻を補助使用。"""
    if not isinstance(state_dict, dict):
        return None

    saved_at = state_dict.get("state_saved_at")
    if isinstance(saved_at, datetime):
        return saved_at
    if isinstance(saved_at, str):
        try:
            return datetime.fromisoformat(saved_at)
        except ValueError:
            pass

    if local_file_path and os.path.exists(local_file_path):
        try:
            return datetime.fromtimestamp(os.path.getmtime(local_file_path))
        except OSError:
            pass
    return None


def choose_newest_runtime_state(local_state, cloud_state, local_file_path=None):
    """コード更新後はクラウドとローカルのうち新しい稼働状態を採用する。"""
    if cloud_state is None:
        return local_state
    if local_state is None:
        return cloud_state

    cloud_time = _get_state_saved_at(cloud_state)
    local_explicit_time = local_state.get("state_saved_at")

    # V1.6.28以前のpickleには保存時刻フィールドがない。
    # すでにクラウド状態が存在する場合は、古い同梱pickleよりクラウドを優先する。
    if not isinstance(local_explicit_time, (datetime, str)):
        selected = dict(cloud_state)
    else:
        local_time = _get_state_saved_at(local_state, local_file_path)
        if cloud_time is None:
            selected = dict(local_state)
        elif local_time is None or cloud_time >= local_time:
            selected = dict(cloud_state)
        else:
            selected = dict(local_state)

    # 製品マスターとCost Savingは従来どおり別系統で同期するため、
    # ローカルにしかない値があれば引き継ぐ。
    for local_only_key in ("products", "cost_saving_data"):
        if local_only_key not in selected and local_only_key in local_state:
            selected[local_only_key] = local_state.get(local_only_key)

    return selected


# --- Cost Saving 実績・クラウド保存 ---
COST_SAVING_FILE = "mfr_cost_saving_history.json"

DEFAULT_COST_SAVING_SETTINGS = {
    "power_kw": 0.80,
    "electricity_price": 25.0,
    "labor_hourly_rate": 4600.0,
    "manual_minutes_per_lot": 5.0,
    "maintenance_cost": 0.0,
    "maintenance_life_hours": 0.0,
}


def get_default_cost_saving_data():
    return {
        "schema_version": 2,
        "settings": dict(DEFAULT_COST_SAVING_SETTINGS),
        "production_history": [],
        "power_events": [],
        # 削除済みIDはクラウド側の古い履歴が再同期で復活しないための墓標。
        "deleted_production_ids": [],
        "deleted_power_event_ids": [],
        # 週単位削除では電源ON/OFFの連続性を壊さず、その週だけ集計対象外にする。
        "excluded_weeks": [],
    }


def normalize_cost_saving_data(data):
    base = get_default_cost_saving_data()
    if not isinstance(data, dict):
        return base

    settings = dict(DEFAULT_COST_SAVING_SETTINGS)
    raw_settings = data.get("settings", {})
    if isinstance(raw_settings, dict):
        settings.update(raw_settings)

    production_history = data.get("production_history", [])
    if not isinstance(production_history, list):
        production_history = []

    power_events = data.get("power_events", [])
    if not isinstance(power_events, list):
        power_events = []

    deleted_production_ids = data.get("deleted_production_ids", [])
    if not isinstance(deleted_production_ids, list):
        deleted_production_ids = []
    deleted_production_ids = list(dict.fromkeys(
        str(value) for value in deleted_production_ids if value
    ))

    deleted_power_event_ids = data.get("deleted_power_event_ids", [])
    if not isinstance(deleted_power_event_ids, list):
        deleted_power_event_ids = []
    deleted_power_event_ids = list(dict.fromkeys(
        str(value) for value in deleted_power_event_ids if value
    ))

    excluded_weeks = data.get("excluded_weeks", [])
    if not isinstance(excluded_weeks, list):
        excluded_weeks = []
    excluded_weeks = list(dict.fromkeys(
        str(value) for value in excluded_weeks if value
    ))

    deleted_production_set = set(deleted_production_ids)
    production_history = [
        item for item in production_history
        if not isinstance(item, dict)
        or str(item.get("job_id", "")) not in deleted_production_set
    ]

    deleted_power_set = set(deleted_power_event_ids)
    power_events = [
        item for item in power_events
        if not isinstance(item, dict)
        or str(item.get("event_id", "")) not in deleted_power_set
    ]

    return {
        "schema_version": 2,
        "settings": settings,
        "production_history": production_history,
        "power_events": power_events,
        "deleted_production_ids": deleted_production_ids,
        "deleted_power_event_ids": deleted_power_event_ids,
        "excluded_weeks": excluded_weeks,
    }


def load_cost_saving_from_github():
    if not GITHUB_TOKEN:
        return None
    try:
        api_url = (
            f"https://api.github.com/repos/{GITHUB_REPO}/contents/"
            f"{COST_SAVING_FILE}"
        )
        req = urllib.request.Request(api_url)
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode("utf-8"))
            content = base64.b64decode(data["content"]).decode("utf-8")
            return normalize_cost_saving_data(json.loads(content))
    except Exception:
        return None


def _merge_history_by_key(remote_items, local_items, key_name):
    merged = {}
    for item in (remote_items or []):
        if isinstance(item, dict) and item.get(key_name):
            merged[str(item[key_name])] = item
    for item in (local_items or []):
        if isinstance(item, dict) and item.get(key_name):
            merged[str(item[key_name])] = item
    return list(merged.values())


def merge_cost_saving_data(remote_data, local_data, prefer_local_settings=True):
    remote = normalize_cost_saving_data(remote_data)
    local = normalize_cost_saving_data(local_data)

    if prefer_local_settings:
        settings = dict(remote["settings"])
        settings.update(local["settings"])
    else:
        settings = dict(local["settings"])
        settings.update(remote["settings"])

    deleted_production_ids = list(dict.fromkeys(
        remote.get("deleted_production_ids", [])
        + local.get("deleted_production_ids", [])
    ))
    deleted_power_event_ids = list(dict.fromkeys(
        remote.get("deleted_power_event_ids", [])
        + local.get("deleted_power_event_ids", [])
    ))
    excluded_weeks = list(dict.fromkeys(
        remote.get("excluded_weeks", [])
        + local.get("excluded_weeks", [])
    ))

    production_history = _merge_history_by_key(
        remote["production_history"],
        local["production_history"],
        "job_id",
    )
    production_history = [
        item for item in production_history
        if str(item.get("job_id", "")) not in set(deleted_production_ids)
    ]

    power_events = _merge_history_by_key(
        remote["power_events"],
        local["power_events"],
        "event_id",
    )
    power_events = [
        item for item in power_events
        if str(item.get("event_id", "")) not in set(deleted_power_event_ids)
    ]

    return {
        "schema_version": 2,
        "settings": settings,
        "production_history": production_history,
        "power_events": power_events,
        "deleted_production_ids": deleted_production_ids,
        "deleted_power_event_ids": deleted_power_event_ids,
        "excluded_weeks": excluded_weeks,
    }


def save_cost_saving_to_github(cost_data):
    if not GITHUB_TOKEN:
        return False

    try:
        api_url = (
            f"https://api.github.com/repos/{GITHUB_REPO}/contents/"
            f"{COST_SAVING_FILE}"
        )

        sha = None
        try:
            req_check = urllib.request.Request(api_url)
            req_check.add_header("Authorization", f"token {GITHUB_TOKEN}")
            with urllib.request.urlopen(req_check, timeout=10) as res:
                sha = json.loads(res.read().decode("utf-8")).get("sha")
        except Exception:
            pass

        encoded = base64.b64encode(
            json.dumps(
                normalize_cost_saving_data(cost_data),
                ensure_ascii=False,
                indent=2,
            ).encode("utf-8")
        ).decode("utf-8")

        payload = {
            "message": "Update MFR Cost Saving History",
            "content": encoded,
            "branch": "main",
        }
        if sha:
            payload["sha"] = sha

        req = urllib.request.Request(
            api_url,
            data=json.dumps(payload).encode("utf-8"),
            method="PUT",
        )
        req.add_header("Authorization", f"token {GITHUB_TOKEN}")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=15):
            pass
        return True
    except Exception as e:
        print("Cost Saving GitHubセーブエラー:", e)
        return False


def sync_cost_saving_to_github():
    """ローカル履歴とGitHub履歴をID単位で統合して保存する。"""
    if not GITHUB_TOKEN:
        return False

    local_data = normalize_cost_saving_data(
        st.session_state.get("cost_saving_data")
    )
    remote_data = load_cost_saving_from_github()
    merged = merge_cost_saving_data(
        remote_data,
        local_data,
        prefer_local_settings=True,
    )
    st.session_state.cost_saving_data = merged
    return save_cost_saving_to_github(merged)


def parse_history_datetime(value):
    if isinstance(value, datetime):
        return value
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None


def get_cost_saving_settings_snapshot():
    data = normalize_cost_saving_data(
        st.session_state.get("cost_saving_data")
    )
    return dict(data["settings"])


def record_power_event(action, actual_time, alert_id, scheduled_time=None):
    """実際に確認されたMFR電源ON/OFFを重複なく記録する。"""
    if action not in ("ON", "OFF") or not isinstance(actual_time, datetime):
        return False

    data = normalize_cost_saving_data(
        st.session_state.get("cost_saving_data")
    )
    event_id = str(alert_id)
    if event_id in set(data.get("deleted_power_event_ids", [])):
        st.session_state.cost_saving_data = data
        return False
    if any(
        str(event.get("event_id")) == event_id
        for event in data["power_events"]
        if isinstance(event, dict)
    ):
        st.session_state.cost_saving_data = data
        return False

    data["power_events"].append({
        "event_id": event_id,
        "action": action,
        "actual_at": actual_time.isoformat(timespec="seconds"),
        "scheduled_at": (
            scheduled_time.isoformat(timespec="seconds")
            if isinstance(scheduled_time, datetime)
            else None
        ),
        "settings": get_cost_saving_settings_snapshot(),
    })
    st.session_state.cost_saving_data = data
    return True


def archive_production_job(machine, job, ended_at, completion_type):
    """終了したLotをCost Saving生産履歴へ1回だけ保存する。"""
    if not isinstance(job, dict) or not job.get("job_id"):
        return False

    data = normalize_cost_saving_data(
        st.session_state.get("cost_saving_data")
    )
    job_id = str(job["job_id"])
    if job_id in set(data.get("deleted_production_ids", [])):
        st.session_state.cost_saving_data = data
        return False
    if any(
        str(record.get("job_id")) == job_id
        for record in data["production_history"]
        if isinstance(record, dict)
    ):
        st.session_state.cost_saving_data = data
        return False

    settings = get_cost_saving_settings_snapshot()
    labor_rate = max(0.0, float(settings.get("labor_hourly_rate", 0) or 0))
    manual_minutes = max(
        0.0,
        float(settings.get("manual_minutes_per_lot", 0) or 0),
    )
    labor_saving_yen = manual_minutes / 60.0 * labor_rate

    started_at = job.get("production_started_at")
    if not isinstance(started_at, datetime):
        started_at = parse_history_datetime(started_at)
    if not isinstance(started_at, datetime):
        started_at = job.get("last_update")
    if not isinstance(started_at, datetime):
        started_at = ended_at

    measurement_records = []
    for item in job.get("measurement_records", []):
        if isinstance(item, dict):
            measurement_records.append(dict(item))

    data["production_history"].append({
        "job_id": job_id,
        "machine": machine,
        "product_name": job.get("product_name", ""),
        "total_qty": int(job.get("total_qty", 0) or 0),
        "final_qty": int(job.get("current_qty", 0) or 0),
        "cycle_time": float(job.get("cycle_time", 0) or 0),
        "measurement_count": len(job.get("targets", [])),
        "measurement_completed_count": len(job.get("completed", [])),
        "measurement_records": measurement_records,
        "started_at": started_at.isoformat(timespec="seconds"),
        "ended_at": ended_at.isoformat(timespec="seconds"),
        "completion_type": completion_type,
        "labor_saving_yen": round(labor_saving_yen, 2),
        "settings": settings,
    })
    st.session_state.cost_saving_data = data
    return True


def build_power_off_intervals(power_events, now_jst):
    """OFF確認から次のON確認までを削減通電時間として返す。"""
    events = []
    for event in power_events or []:
        if not isinstance(event, dict):
            continue
        actual_at = parse_history_datetime(event.get("actual_at"))
        if actual_at is None:
            continue
        action = str(event.get("action", "")).upper()
        if action not in ("ON", "OFF"):
            continue
        events.append((actual_at, action, event))

    events.sort(key=lambda row: row[0])
    intervals = []
    open_off = None

    for actual_at, action, event in events:
        if action == "OFF":
            if open_off is None:
                open_off = (actual_at, event)
        elif action == "ON" and open_off is not None:
            off_at, off_event = open_off
            if actual_at > off_at:
                intervals.append({
                    "start": off_at,
                    "end": actual_at,
                    "settings": dict(
                        off_event.get("settings")
                        or DEFAULT_COST_SAVING_SETTINGS
                    ),
                    "open": False,
                })
            open_off = None

    if open_off is not None:
        off_at, off_event = open_off
        if now_jst > off_at:
            intervals.append({
                "start": off_at,
                "end": now_jst,
                "settings": dict(
                    off_event.get("settings")
                    or DEFAULT_COST_SAVING_SETTINGS
                ),
                "open": True,
            })

    return intervals


def _week_start(dt_value):
    return (dt_value - timedelta(days=dt_value.weekday())).replace(
        hour=0, minute=0, second=0, microsecond=0
    )


def _add_effect(bucket, key, **values):
    row = bucket.setdefault(key, {
        "saved_hours": 0.0,
        "saved_kwh": 0.0,
        "electricity_yen": 0.0,
        "labor_yen": 0.0,
        "maintenance_yen": 0.0,
        "lots": 0,
    })
    for name, value in values.items():
        row[name] = row.get(name, 0) + value


def _split_power_interval_into_buckets(interval, bucket, mode):
    cursor = interval["start"]
    end = interval["end"]
    settings = dict(DEFAULT_COST_SAVING_SETTINGS)
    settings.update(interval.get("settings") or {})

    power_kw = max(0.0, float(settings.get("power_kw", 0) or 0))
    elec_price = max(
        0.0,
        float(settings.get("electricity_price", 0) or 0),
    )
    maintenance_cost = max(
        0.0,
        float(settings.get("maintenance_cost", 0) or 0),
    )
    maintenance_life = max(
        0.0,
        float(settings.get("maintenance_life_hours", 0) or 0),
    )
    maintenance_per_hour = (
        maintenance_cost / maintenance_life
        if maintenance_cost > 0 and maintenance_life > 0
        else 0.0
    )

    while cursor < end:
        if mode == "day":
            key = cursor.replace(hour=0, minute=0, second=0, microsecond=0)
            boundary = key + timedelta(days=1)
        else:
            key = _week_start(cursor)
            boundary = key + timedelta(days=7)

        segment_end = min(end, boundary)
        hours = max(
            0.0,
            (segment_end - cursor).total_seconds() / 3600.0,
        )
        kwh = hours * power_kw
        _add_effect(
            bucket,
            key,
            saved_hours=hours,
            saved_kwh=kwh,
            electricity_yen=kwh * elec_price,
            maintenance_yen=hours * maintenance_per_hour,
        )
        cursor = segment_end


def build_cost_saving_summary(cost_data, now_jst):
    data = normalize_cost_saving_data(cost_data)
    daily = {}
    weekly = {}
    excluded_week_keys = set(data.get("excluded_weeks", []))

    intervals = build_power_off_intervals(
        data["power_events"],
        now_jst,
    )
    for interval in intervals:
        _split_power_interval_into_buckets(interval, daily, "day")
        _split_power_interval_into_buckets(interval, weekly, "week")

    for record in data["production_history"]:
        if not isinstance(record, dict):
            continue
        ended_at = parse_history_datetime(record.get("ended_at"))
        if ended_at is None:
            continue
        labor_yen = max(
            0.0,
            float(record.get("labor_saving_yen", 0) or 0),
        )
        day_key = ended_at.replace(hour=0, minute=0, second=0, microsecond=0)
        week_key = _week_start(ended_at)
        week_key_text = week_key.strftime("%Y-%m-%d")
        if week_key_text in excluded_week_keys:
            continue
        _add_effect(daily, day_key, labor_yen=labor_yen, lots=1)
        _add_effect(weekly, week_key, labor_yen=labor_yen, lots=1)

    # 週単位削除済みの週は、電源OFF区間由来の効果も含めて集計から除外する。
    if excluded_week_keys:
        weekly = {
            key: value for key, value in weekly.items()
            if key.strftime("%Y-%m-%d") not in excluded_week_keys
        }
        daily = {
            key: value for key, value in daily.items()
            if _week_start(key).strftime("%Y-%m-%d") not in excluded_week_keys
        }

    return daily, weekly, intervals


def effect_total_yen(row):
    return (
        float(row.get("electricity_yen", 0) or 0)
        + float(row.get("labor_yen", 0) or 0)
        + float(row.get("maintenance_yen", 0) or 0)
    )


def format_cost_saving_week_label(week_start):
    week_end = week_start + timedelta(days=6)
    return (
        f"{week_start.strftime('%Y/%m/%d')}～"
        f"{week_end.strftime('%m/%d')}"
    )


def get_cost_saving_history_weeks(cost_data):
    """生産履歴または電源履歴が存在する週を月曜始まりで返す。"""
    data = normalize_cost_saving_data(cost_data)
    weeks = set()
    excluded = set(data.get("excluded_weeks", []))

    for record in data.get("production_history", []):
        if not isinstance(record, dict):
            continue
        ended_at = parse_history_datetime(record.get("ended_at"))
        if ended_at is not None:
            weeks.add(_week_start(ended_at))

    for event in data.get("power_events", []):
        if not isinstance(event, dict):
            continue
        actual_at = parse_history_datetime(event.get("actual_at"))
        if actual_at is not None:
            weeks.add(_week_start(actual_at))

    # すでに週削除済みの週は再削除候補に出さない。
    return sorted(
        [week for week in weeks if week.strftime("%Y-%m-%d") not in excluded],
        reverse=True,
    )


def delete_cost_saving_production_record(job_id):
    """生産履歴1件を削除し、クラウド再同期でも復活しないよう墓標を残す。"""
    data = normalize_cost_saving_data(
        st.session_state.get("cost_saving_data")
    )
    job_id = str(job_id or "")
    if not job_id:
        return False

    before_count = len(data["production_history"])
    data["production_history"] = [
        record for record in data["production_history"]
        if str(record.get("job_id", "")) != job_id
    ]
    if len(data["production_history"]) == before_count:
        return False

    deleted_ids = list(data.get("deleted_production_ids", []))
    if job_id not in deleted_ids:
        deleted_ids.append(job_id)
    data["deleted_production_ids"] = deleted_ids
    st.session_state.cost_saving_data = normalize_cost_saving_data(data)
    return True


def delete_cost_saving_week(week_start):
    """
    指定週のCost Saving実績を削除する。

    生産履歴は実データから削除する。電源ON/OFF履歴は隣接週とのOFF→ON連続性を
    壊さないため内部時系列を保持しつつ、その週の表示・集計から除外する。
    """
    if not isinstance(week_start, datetime):
        return False

    data = normalize_cost_saving_data(
        st.session_state.get("cost_saving_data")
    )
    target_key = _week_start(week_start).strftime("%Y-%m-%d")

    deleted_ids = list(data.get("deleted_production_ids", []))
    kept_records = []
    removed_any = False
    for record in data["production_history"]:
        ended_at = parse_history_datetime(record.get("ended_at"))
        if (
            ended_at is not None
            and _week_start(ended_at).strftime("%Y-%m-%d") == target_key
        ):
            job_id = str(record.get("job_id", ""))
            if job_id and job_id not in deleted_ids:
                deleted_ids.append(job_id)
            removed_any = True
            continue
        kept_records.append(record)

    data["production_history"] = kept_records
    data["deleted_production_ids"] = deleted_ids

    excluded_weeks = list(data.get("excluded_weeks", []))
    if target_key not in excluded_weeks:
        excluded_weeks.append(target_key)
        removed_any = True
    data["excluded_weeks"] = excluded_weeks

    st.session_state.cost_saving_data = normalize_cost_saving_data(data)
    return removed_any


def delete_all_cost_saving_history():
    """計算条件を残し、生産履歴・電源実績をすべて削除する。"""
    data = normalize_cost_saving_data(
        st.session_state.get("cost_saving_data")
    )

    deleted_production_ids = list(data.get("deleted_production_ids", []))
    for record in data["production_history"]:
        job_id = str(record.get("job_id", ""))
        if job_id and job_id not in deleted_production_ids:
            deleted_production_ids.append(job_id)

    deleted_power_event_ids = list(data.get("deleted_power_event_ids", []))
    for event in data["power_events"]:
        event_id = str(event.get("event_id", ""))
        if event_id and event_id not in deleted_power_event_ids:
            deleted_power_event_ids.append(event_id)

    had_history = bool(
        data["production_history"]
        or data["power_events"]
        or data.get("excluded_weeks")
    )

    data["production_history"] = []
    data["power_events"] = []
    data["deleted_production_ids"] = deleted_production_ids
    data["deleted_power_event_ids"] = deleted_power_event_ids
    data["excluded_weeks"] = []
    st.session_state.cost_saving_data = normalize_cost_saving_data(data)
    return had_history


def save_cost_saving_history_change():
    """削除などの履歴変更をローカル保存し、墓標込みでGitHubへ同期する。"""
    save_state()
    cloud_saved = sync_cost_saving_to_github()
    save_state()
    return cloud_saved

# ページ設定
logo_path = "logo.png" 
icon_path = "icon.ico" 
st.set_page_config(page_title="MFR電源管理システム", page_icon=icon_path, layout="wide")

APP_VERSION = "1.6.30"

# 10秒ごとに自動更新（Excelの後ろでも通知時刻を早く検出）
AUTO_REFRESH_MS = 10_000
st_autorefresh(interval=AUTO_REFRESH_MS, key="data_refresh")

# --- データの保存と読み込み ---
# 相対パスではなくapp.pyと同じ場所へ固定し、起動ディレクトリ差による読み違いを防ぐ。
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(SCRIPT_DIR, "mfr_state.pkl")

def load_state():
    """ローカルとクラウドの稼働状態を比較し、最も新しい状態を復元する。"""
    local_state = None
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "rb") as f:
                loaded = pickle.load(f)
            if isinstance(loaded, dict):
                local_state = loaded
        except Exception as e:
            print("ローカル状態読み込みエラー:", e)

    cloud_state = load_runtime_state_from_github()
    selected_state = choose_newest_runtime_state(
        local_state,
        cloud_state,
        STATE_FILE,
    )

    if isinstance(selected_state, dict):
        return selected_state
    return None

def infer_mfr_power_state_from_alert_history(alert_ids):
    """
    V1.5.9より前の保存データからMFR電源状態を推定する。

    確認履歴は押した順に保存されているため、
    最後に確認した電源操作がONならTrue、OFFならFalseとする。
    """
    power_is_on = False

    for alert_id in alert_ids or []:
        alert_id_text = str(alert_id)

        if alert_id_text.startswith("ON_"):
            power_is_on = True
        elif alert_id_text.startswith("OFF_ACTUAL_"):
            power_is_on = False

    return power_is_on


def save_state():
    state_to_save = {
        'jobs': st.session_state.jobs,
        'last_inspection_date': st.session_state.last_inspection_date,
        'products': st.session_state.products,
        # 作業者が［確認しました］を押した通知だけを保存
        'acknowledged_alerts': st.session_state.acknowledged_alerts,
        # 実際に測定・点検が完了した10分後の電源OFF通知
        'pending_power_off_due': st.session_state.pending_power_off_due,
        # OFF通知で「どの測定／点検が完了したか」を説明するための文脈。
        'pending_power_off_context': st.session_state.get(
            'pending_power_off_context'
        ),
        # V1.6.30以降、手動の［生産終了］は未測定が残っていても即時終了する。
        # 旧版の測定必須ダイアログ状態は保存せず、常に解除する。
        'pending_measurement_required_before_finish': None,
        # 最終MFR測定後の「生産も終了ですか？」確認待ち。
        'pending_production_finish_confirmation': st.session_state.get(
            'pending_production_finish_confirmation'
        ),
        # 電源OFF確認後の「次回ON予定を表示札へ記入」確認待ち。
        'pending_signboard_confirmation': st.session_state.get(
            'pending_signboard_confirmation'
        ),
        # Cost Savingの生産履歴・電源実績・計算条件。
        'cost_saving_data': normalize_cost_saving_data(
            st.session_state.get('cost_saving_data')
        ),
        # 作業者が確認した実際のMFR電源状態。
        # ON確認後は、OFF確認されるまで再度ONアラートを出さない。
        'mfr_power_is_on': st.session_state.get('mfr_power_is_on', False),
        'mfr_power_on_confirmed_at': st.session_state.get(
            'mfr_power_on_confirmed_at'
        ),
        # V1.6.0以降の電源状態管理。
        'mfr_power_state_version': 2,
        # ローカル／クラウドのどちらが新しい状態か判定するための保存時刻。
        'state_saved_at': datetime.utcnow() + timedelta(hours=9),
    }
    with open(STATE_FILE, "wb") as f:
        pickle.dump(state_to_save, f)

    # V1.6.29以降は稼働状態も専用ブランチへ自動同期する。
    # GitHub未設定・一時的な通信失敗でもローカル運用は継続する。
    if GITHUB_TOKEN:
        save_runtime_state_to_github(state_to_save)

def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# --- Edge通知・チャイム音 ---
# 通知音は必ずこのプログラムと同じフォルダーから読み込みます。
# 旧版の alert_chime.wav を誤って読み込まないよう、固有名を使用します。
# SCRIPT_DIR は状態ファイル設定時に定義済み。
ALERT_SOUND_FILE = os.path.join(
    SCRIPT_DIR,
    "alert_crystal_rise.wav",
)
ALERT_SOUND_NAME = "クリスタルライズ"
ALERT_SOUND_VERSION = "crystal_rise_parent_engine_1_6_28"

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
    始業時にクリックして、チャイム音の再生を有効にする。

    通知音エンジンはStreamlitのiframe内ではなく、
    親のEdge画面へscriptとして直接設置する。
    これにより10秒ごとの自動更新後も繰り返しタイマーを維持する。
    """
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
    lastPlayAt: 0,
    urgentTimer: null,
    urgentWatchdog: null,
    urgentDialogId: null,
    urgentSources: [],
    urgentLastPlayAt: 0
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

  function stopUrgentSources() {
    for (const oscillator of state.urgentSources) {
      try {
        oscillator.stop();
      } catch (error) {}
    }
    state.urgentSources = [];
  }

  async function playUrgentOnce() {
    const audioContext = getAudioContext();

    if (audioContext.state === "suspended") {
      await audioContext.resume();
    }

    const now = audioContext.currentTime + 0.02;

    const compressor = audioContext.createDynamicsCompressor();
    compressor.threshold.setValueAtTime(-16, now);
    compressor.knee.setValueAtTime(10, now);
    compressor.ratio.setValueAtTime(5, now);
    compressor.attack.setValueAtTime(0.002, now);
    compressor.release.setValueAtTime(0.18, now);
    compressor.connect(audioContext.destination);

    const master = audioContext.createGain();
    master.gain.setValueAtTime(0.90, now);
    master.connect(compressor);

    // ダイアログ専用「確認催促音」。
    // 成形室の騒音に埋もれにくいよう、2.8kHz～4.8kHz帯の
    // 高い3連パルスを2セット鳴らす。短く鋭い「ピピピッ」を
    // 繰り返し、通常のクリスタルライズとは明確に区別する。
    const events = [
      {start: 0.00, frequency: 2800.00, duration: 0.085, level: 0.82},
      {start: 0.11, frequency: 3800.00, duration: 0.085, level: 0.92},
      {start: 0.22, frequency: 4800.00, duration: 0.100, level: 1.00},
      {start: 0.62, frequency: 2800.00, duration: 0.085, level: 0.82},
      {start: 0.73, frequency: 3800.00, duration: 0.085, level: 0.92},
      {start: 0.84, frequency: 4800.00, duration: 0.110, level: 1.00}
    ];

    for (const event of events) {
      const oscillator = audioContext.createOscillator();
      const gain = audioContext.createGain();
      const eventStart = now + event.start;
      const eventEnd = eventStart + event.duration;

      oscillator.type = "square";
      oscillator.frequency.setValueAtTime(event.frequency, eventStart);

      gain.gain.setValueAtTime(0.0001, eventStart);
      gain.gain.exponentialRampToValueAtTime(
        Math.max(0.0002, event.level * 0.20),
        eventStart + 0.004
      );
      gain.gain.exponentialRampToValueAtTime(0.0001, eventEnd);

      oscillator.connect(gain);
      gain.connect(master);
      state.urgentSources.push(oscillator);

      oscillator.onended = () => {
        state.urgentSources = state.urgentSources.filter(
          item => item !== oscillator
        );
      };

      oscillator.start(eventStart);
      oscillator.stop(eventEnd + 0.02);
    }

    state.urgentLastPlayAt = Date.now();
    return audioContext.state;
  }

  function stopUrgentLoop(clearStorage = true) {
    if (state.urgentTimer) {
      w.clearInterval(state.urgentTimer);
      state.urgentTimer = null;
    }

    if (state.urgentWatchdog) {
      w.clearInterval(state.urgentWatchdog);
      state.urgentWatchdog = null;
    }

    state.urgentDialogId = null;
    state.urgentLastPlayAt = 0;
    stopUrgentSources();

    if (clearStorage) {
      w.localStorage.removeItem("mfr_active_dialog_id");
      w.localStorage.removeItem("mfr_dialog_reminder_enabled");
    }
  }

  async function startUrgentLoop(dialogId) {
    if (!dialogId) return;

    const storedDialogId = w.localStorage.getItem("mfr_active_dialog_id");

    if (
      state.urgentTimer
      && state.urgentDialogId === dialogId
      && storedDialogId === dialogId
    ) {
      return;
    }

    stopUrgentLoop(false);
    state.urgentDialogId = dialogId;
    w.localStorage.setItem("mfr_active_dialog_id", dialogId);
    w.localStorage.setItem("mfr_dialog_reminder_enabled", "1");

    const playIfActive = async () => {
      const activeDialogId = w.localStorage.getItem("mfr_active_dialog_id");
      const enabled =
        w.localStorage.getItem("mfr_dialog_reminder_enabled") === "1";

      if (
        !enabled
        || activeDialogId !== dialogId
        || state.urgentDialogId !== dialogId
      ) {
        stopUrgentLoop(false);
        return;
      }

      try {
        await playUrgentOnce();
        w.localStorage.removeItem("mfr_dialog_audio_error");
      } catch (error) {
        w.localStorage.setItem(
          "mfr_dialog_audio_error",
          `${error?.name || "AudioError"}: ${error?.message || String(error)}`
        );
      }
    };

    // ダイアログ表示直後に鳴らし、その後は約2.6秒ごとに催促する。
    await playIfActive();
    state.urgentTimer = w.setInterval(playIfActive, 2600);

    // Edgeのタイマー停止・遅延時にも復旧する。
    state.urgentWatchdog = w.setInterval(() => {
      const activeDialogId = w.localStorage.getItem("mfr_active_dialog_id");
      const enabled =
        w.localStorage.getItem("mfr_dialog_reminder_enabled") === "1";
      const elapsed = Date.now() - (state.urgentLastPlayAt || 0);

      if (
        enabled
        && activeDialogId === dialogId
        && state.urgentDialogId === dialogId
        && elapsed >= 3600
      ) {
        playIfActive();
      }
    }, 1000);
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

    const activeDialogId = w.localStorage.getItem("mfr_active_dialog_id");
    const dialogReminderEnabled =
      w.localStorage.getItem("mfr_dialog_reminder_enabled") === "1";

    if (dialogReminderEnabled && activeDialogId) {
      w.setTimeout(() => {
        startUrgentLoop(activeDialogId);
      }, 1300);
    }

    return contextState;
  }

  function stopAlert() {
    stopLoop(true);
  }

  function stopAll() {
    stopLoop(true);
    stopUrgentLoop(true);
  }

  w.__mfrCrystalEngine = {
    version: VERSION,
    activate,
    playOnce,
    startLoop,
    stopAlert,
    playUrgentOnce,
    startUrgentLoop,
    stopUrgentLoop,
    stopAll,
    getState: () => ({
      alertId: state.alertId,
      timerActive: Boolean(state.timer),
      urgentDialogId: state.urgentDialogId,
      urgentTimerActive: Boolean(state.urgentTimer),
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
    <style>
      #mfr-enable {{
        width: 100%;
        padding: 10px 12px;
        font-size: 16px;
        font-weight: 900;
        border-radius: 8px;
        cursor: pointer;
        position: relative;
        z-index: 2;
        pointer-events: auto;
        touch-action: manipulation;
      }}
      #mfr-enable.needs-activation {{
        border: 3px solid #1e3a8a;
        animation: mfr-activation-blink 1.15s ease-in-out infinite;
      }}
      @keyframes mfr-activation-blink {{
        0%, 100% {{
          background-color: #1d4ed8;
          color: #ffffff;
          border-color: #1e3a8a;
          box-shadow: 0 0 14px rgba(37,99,235,0.55);
        }}
        50% {{
          background-color: #facc15;
          color: #111827;
          border-color: #a16207;
          box-shadow: 0 0 22px rgba(250,204,21,0.78);
        }}
      }}
      #mfr-enable.activating {{
        animation: none !important;
        background-color: #1e40af !important;
        color: #ffffff !important;
        border: 2px solid #1e3a8a !important;
        box-shadow: none !important;
      }}
      #mfr-enable.activated {{
        animation: none !important;
        background-color: #64748b !important;
        color: #ffffff !important;
        border: 2px solid #475569 !important;
        box-shadow: none !important;
      }}
      #mfr-enable.audio-error {{
        animation: none !important;
        background-color: #b91c1c !important;
        color: #ffffff !important;
        border: 2px solid #7f1d1d !important;
        box-shadow: none !important;
      }}
    </style>

    <div style="font-family:Meiryo,sans-serif;border:1px solid #93c5fd;
                border-radius:9px;padding:7px;background:#eff6ff;">
      <button id="mfr-enable" class="needs-activation" type="button">
        起動時に必ず押してください。チャイム音テスト
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

      function setButtonState(stateName) {{
        button.classList.remove(
          "needs-activation",
          "activating",
          "activated",
          "audio-error"
        );
        if (stateName === "activating") {{
          button.classList.add("activating");
          button.textContent = "チャイム音を確認中...";
        }} else if (stateName === "activated") {{
          button.classList.add("activated");
          button.textContent = "✓ チャイム音 有効";
        }} else if (stateName === "error") {{
          button.classList.add("audio-error");
          button.textContent = "⚠ チャイム音を確認してください";
        }} else {{
          button.classList.add("needs-activation");
          button.textContent = "起動時に必ず押してください。チャイム音テスト";
        }}
      }}

      function safeStorageSet(storage, key, value) {{
        try {{
          storage.setItem(key, value);
          return true;
        }} catch (error) {{
          return false;
        }}
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

      button.addEventListener("click", async (event) => {{
        event.preventDefault();
        event.stopPropagation();

        // クリックを受け付けた瞬間に点滅を停止する。
        // 親画面側でエラーが起きても、クリック自体が入ったことを確認できる。
        hideStatus();
        setButtonState("activating");
        button.disabled = true;

        try {{
          installParentEngine();

          if (
            !parentWindow.__mfrCrystalEngine
            || typeof parentWindow.__mfrCrystalEngine.activate !== "function"
          ) {{
            throw new Error("通知音エンジンを準備できませんでした。");
          }}

          // Windows通知は使用しない。チャイム音だけを有効化する。
          await parentWindow.__mfrCrystalEngine.activate();

          // Storage保存は補助処理。ここが失敗しても音声成功を無効にしない。
          safeStorageSet(parentWindow.localStorage, "mfr_monitor_enabled", "1");
          safeStorageSet(
            parentWindow.localStorage,
            "mfr_alert_sound_version",
            soundVersion
          );

          hideStatus();
          setButtonState("activated");

        }} catch (error) {{
          showError(
            "⚠️ チャイム音を再生できませんでした。\\n"
            + `エラー：${{error?.name || "UnknownError"}}\\n`
            + `${{error?.message || String(error)}}`
          );
          setButtonState("error");
        }} finally {{
          button.disabled = false;
        }}
      }});

      // 初期化時の親画面アクセスに失敗しても、ボタンのクリック処理は残す。
      try {{
        installParentEngine();
      }} catch (error) {{
        // クリック時に再試行する。
      }}
    }})();
    </script>
    """

    components.html(html, height=78, scrolling=False)



def start_browser_alarm(alert_id, title, body):
    """
    親のブラウザー画面に設置した通知音エンジンへ、
    確認されるまでの繰り返し再生を依頼する。

    V1.6.26以降はWindows通知を使用せず、チャイム音だけで通知する。
    """
    alert_id_json = json.dumps(alert_id, ensure_ascii=False)

    launcher_code = f"""
(() => {{
  const alertId = {alert_id_json};

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

  if (window.__mfrCrystalEngine) {
    if (typeof window.__mfrCrystalEngine.stopAlert === "function") {
      window.__mfrCrystalEngine.stopAlert();
    } else if (typeof window.__mfrCrystalEngine.stopAll === "function") {
      window.__mfrCrystalEngine.stopAll();
    }
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




def start_dialog_reminder(dialog_id):
    """確認ダイアログが開いている間、専用の催促音を繰り返す。"""
    dialog_id_json = json.dumps(str(dialog_id), ensure_ascii=False)
    launcher_code = f"""
(() => {{
  const dialogId = {dialog_id_json};
  localStorage.setItem("mfr_active_dialog_id", dialogId);
  localStorage.setItem("mfr_dialog_reminder_enabled", "1");

  let attempts = 0;
  const startWhenReady = () => {{
    attempts += 1;
    if (
      window.__mfrCrystalEngine
      && typeof window.__mfrCrystalEngine.startUrgentLoop === "function"
    ) {{
      // 確認ダイアログ中は通常アラート音と重ねず、催促音を優先する。
      if (typeof window.__mfrCrystalEngine.stopAlert === "function") {{
        window.__mfrCrystalEngine.stopAlert();
      }}
      window.__mfrCrystalEngine.startUrgentLoop(dialogId).catch((error) => {{
        localStorage.setItem(
          "mfr_dialog_audio_error",
          `${{error?.name || "AudioError"}}: ${{error?.message || String(error)}}`
        );
      }});
      return;
    }}

    if (attempts < 30) {{
      window.setTimeout(startWhenReady, 200);
    }}
  }};

  startWhenReady();
}})();
"""
    launcher_code_js = json.dumps(launcher_code)
    components.html(
        f"""
        <script>
        (() => {{
          const parentWindow = window.parent;
          const launcherCode = {launcher_code_js};
          const launcher = parentWindow.document.createElement("script");
          launcher.textContent = launcherCode;
          parentWindow.document.head.appendChild(launcher);
          launcher.remove();
        }})();
        </script>
        """,
        height=0,
        width=0,
    )


def stop_dialog_reminder():
    """ダイアログへの応答後、専用の催促音だけを停止する。"""
    stop_code = r"""
(() => {
  localStorage.removeItem("mfr_active_dialog_id");
  localStorage.removeItem("mfr_dialog_reminder_enabled");

  if (
    window.__mfrCrystalEngine
    && typeof window.__mfrCrystalEngine.stopUrgentLoop === "function"
  ) {
    window.__mfrCrystalEngine.stopUrgentLoop(true);
  }
})();
"""
    stop_code_js = json.dumps(stop_code)
    components.html(
        f"""
        <script>
        (() => {{
          const parentWindow = window.parent;
          const stopCode = {stop_code_js};
          const stopper = parentWindow.document.createElement("script");
          stopper.textContent = stopCode;
          parentWindow.document.head.appendChild(stopper);
          stopper.remove();
        }})();
        </script>
        """,
        height=0,
        width=0,
    )



def scroll_to_active_alert(alert_id):
    """
    新しいアラートが発生した瞬間だけ、親Edge画面をページ最上部へ戻す。

    Streamlitではwindow自体ではなく[data-testid="stMain"]等の内部要素が
    スクロールコンテナになる場合があるため、ページ上端アンカーへの
    scrollIntoViewと、候補スクロール要素のscrollTop=0を併用する。

    実際に上端へ戻ったことを確認してからアラートIDをlocalStorageへ保存し、
    失敗した場合は短時間再試行する。
    """
    alert_id_json = json.dumps(str(alert_id), ensure_ascii=False)
    scroll_code = f"""
(() => {{
  const alertId = {alert_id_json};
  const storageKey = "mfr_last_auto_scrolled_alert_id_v1_6_25";

  if (localStorage.getItem(storageKey) === alertId) {{
    return;
  }}

  let attempts = 0;

  const getScrollCandidates = () => {{
    const selectors = [
      '[data-testid="stMain"]',
      '.stMain',
      'section.main',
      '[data-testid="stAppViewContainer"]',
      '.main'
    ];

    const candidates = [];
    for (const selector of selectors) {{
      const element = document.querySelector(selector);
      if (element && !candidates.includes(element)) {{
        candidates.push(element);
      }}
    }}

    if (document.scrollingElement && !candidates.includes(document.scrollingElement)) {{
      candidates.push(document.scrollingElement);
    }}
    if (document.documentElement && !candidates.includes(document.documentElement)) {{
      candidates.push(document.documentElement);
    }}
    if (document.body && !candidates.includes(document.body)) {{
      candidates.push(document.body);
    }}

    return candidates;
  }};

  const forceTop = () => {{
    const topAnchor = document.getElementById('mfr-page-top-anchor');

    if (topAnchor && typeof topAnchor.scrollIntoView === 'function') {{
      try {{
        topAnchor.scrollIntoView({{
          behavior: 'auto',
          block: 'start',
          inline: 'nearest'
        }});
      }} catch (error) {{}}
    }}

    try {{
      window.scrollTo(0, 0);
    }} catch (error) {{}}

    for (const element of getScrollCandidates()) {{
      try {{
        if (typeof element.scrollTo === 'function') {{
          element.scrollTo({{ top: 0, left: 0, behavior: 'auto' }});
        }}
        element.scrollTop = 0;
      }} catch (error) {{}}
    }}
  }};

  const isAtTop = () => {{
    const topAnchor = document.getElementById('mfr-page-top-anchor');
    if (topAnchor) {{
      const rect = topAnchor.getBoundingClientRect();
      if (rect.top >= -8 && rect.top <= 120) {{
        return true;
      }}
    }}

    const candidates = getScrollCandidates();
    return candidates.some((element) => {{
      try {{
        return Math.abs(Number(element.scrollTop || 0)) <= 5;
      }} catch (error) {{
        return false;
      }}
    }});
  }};

  const scrollWhenReady = () => {{
    attempts += 1;
    forceTop();

    window.setTimeout(() => {{
      forceTop();

      if (isAtTop()) {{
        localStorage.setItem(storageKey, alertId);
        return;
      }}

      if (attempts < 30) {{
        window.setTimeout(scrollWhenReady, 120);
      }}
    }}, 80);
  }};

  scrollWhenReady();
}})();
"""
    scroll_code_js = json.dumps(scroll_code)
    components.html(
        f"""
        <script>
        (() => {{
          const parentWindow = window.parent;
          const scrollCode = {scroll_code_js};
          const script = parentWindow.document.createElement("script");
          script.textContent = scrollCode;
          parentWindow.document.head.appendChild(script);
          script.remove();
        }})();
        </script>
        """,
        height=0,
        width=0,
    )


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

    /* =========================================================
       色弱に配慮した状態配色
       青 = 正常・完了 / 黄橙 = 未実施・要操作 / 赤 = アラート / 灰 = 停止
       色だけに依存せず、文字・記号も必ず併用する。
       ========================================================= */

    /* MFR測定：未測定は黄橙色のボタン */
    [class*="st-key-comp_"] button,
    [class*="st-key-comp-"] button {
        background: #facc15 !important;
        border: 3px solid #8a5a00 !important;
        color: #111827 !important;
        font-weight: 900 !important;
        box-shadow: inset 0 0 0 1px rgba(255,255,255,0.65) !important;
    }

    [class*="st-key-comp_"] button:hover,
    [class*="st-key-comp-"] button:hover {
        background: #fde047 !important;
        border-color: #713f12 !important;
        color: #111827 !important;
    }

    /* MFR測定：測定済み（取消可能）は青いボタン */
    [class*="st-key-undo_comp_"] button,
    [class*="st-key-undo-comp-"] button {
        background: #2563eb !important;
        border: 3px solid #1e3a8a !important;
        color: #ffffff !important;
        font-weight: 900 !important;
        box-shadow: inset 0 0 0 1px rgba(255,255,255,0.65) !important;
    }

    [class*="st-key-undo_comp_"] button:hover,
    [class*="st-key-undo-comp-"] button:hover {
        background: #1d4ed8 !important;
        border-color: #172554 !important;
        color: #ffffff !important;
    }

    /* 最終測定済み：操作不可の青い状態表示 */
    .mfr-measurement-done-static {
        width: 100%;
        box-sizing: border-box;
        text-align: center;
        background: #2563eb;
        border: 3px solid #1e3a8a;
        color: #ffffff;
        border-radius: 5px;
        padding: 0.46rem 0.75rem;
        font-weight: 900;
        line-height: 1.45;
        margin-bottom: 0.45rem;
    }

    /* 通常状態カード（Streamlit success/error の赤緑依存を避ける） */
    .status-card {
        width: 100%;
        box-sizing: border-box;
        border-radius: 8px;
        padding: 0.62rem 0.85rem;
        margin: 0.15rem 0 0.35rem 0;
        font-weight: 800;
        line-height: 1.35;
    }
    .status-blue {
        background: #e8f1ff;
        border: 2px solid #2563eb;
        color: #0b3b8c;
    }
    .status-yellow {
        background: #fff7cc;
        border: 2px solid #d97706;
        color: #6b3a00;
    }
    .status-red {
        background: #fee2e2;
        border: 2px solid #dc2626;
        color: #7f1d1d;
    }
    .status-gray {
        background: #f1f5f9;
        border: 2px solid #94a3b8;
        color: #334155;
    }

    /* 現場向け：次に必要な操作だけを大きく表示するカード */
    .next-action-card {
        width: 100%;
        box-sizing: border-box;
        border-radius: 12px;
        padding: 1rem 1.1rem;
        min-height: 150px;
        margin: 0.15rem 0 0.55rem 0;
    }
    .next-action-label {
        font-size: 1.0rem;
        font-weight: 800;
        margin-bottom: 0.35rem;
    }
    .next-action-main {
        font-size: 2.05rem;
        font-weight: 900;
        line-height: 1.18;
        margin-bottom: 0.35rem;
    }
    .next-action-sub {
        font-size: 1.05rem;
        font-weight: 700;
        line-height: 1.4;
    }
    .next-action-yellow {
        background: #fff7cc;
        border: 3px solid #d97706;
        color: #3f2a00;
    }
    .next-action-blue {
        background: #e8f1ff;
        border: 3px solid #2563eb;
        color: #0b2f6b;
    }
    .next-action-red {
        background: #fee2e2;
        border: 3px solid #dc2626;
        color: #7f1d1d;
    }
    .next-action-gray {
        background: #f1f5f9;
        border: 3px solid #94a3b8;
        color: #334155;
    }

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


    /* 成型機の状態を一目で判別できるステータス表示 */
    .machine-status-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.82rem;
        padding: 0.78rem 1.35rem;
        min-height: 68px;
        border-radius: 6px;
        font-size: clamp(1.45rem, 1.05rem + 1.0vw, 2.05rem);
        font-weight: 900;
        margin: 0.08rem 0 0.55rem 0;
        line-height: 1.05;
        box-shadow: 0 1px 2px rgba(15, 23, 42, 0.08);
    }

    .machine-status-icon-circle {
        width: 2.1rem;
        height: 2.1rem;
        min-width: 2.1rem;
        border-radius: 999px;
        background: #ffffff;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 1.35rem;
        font-weight: 900;
        line-height: 1;
        flex-shrink: 0;
    }

    .machine-status-label {
        display: inline-block;
        letter-spacing: 0.01em;
    }

    .machine-running-badge {
        background: #ff1717;
        border: 3px solid #111827;
        color: #ffffff;
    }

    .machine-running-badge .machine-status-icon-circle {
        color: #1d4ed8;
    }

    .machine-paused-badge {
        background: #fff3bf;
        border: 3px solid #d97706;
        color: #6b3a00;
    }

    .machine-paused-badge .machine-status-icon-circle {
        color: #d97706;
    }

    .machine-completed-badge {
        background: #5b9bd5;
        border: 3px solid #0f2d57;
        color: #ffffff;
    }

    .machine-completed-badge .machine-status-icon-circle {
        color: #2563eb;
    }

    .machine-idle-badge {
        background: #f1f5f9;
        border: 2px solid #94a3b8;
        color: #334155;
    }

    .machine-idle-badge .machine-status-icon-circle {
        color: #475569;
    }

    .machine-spin {
        display: inline-block;
        font-size: 1.35rem;
        line-height: 1;
        animation: machine-rotate 1.05s linear infinite;
    }

    @keyframes machine-rotate {
        from { transform: rotate(0deg); }
        to   { transform: rotate(360deg); }
    }

    .top-section-title {
        font-size: 1.18rem;
        font-weight: 800;
        margin: 0.15rem 0 0.3rem 0;
        color: #1f2937;
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
    gh_cost_saving = load_cost_saving_from_github()

    if saved_state:
        st.session_state.jobs = saved_state['jobs']
        st.session_state.last_inspection_date = saved_state['last_inspection_date']
        st.session_state.acknowledged_alerts = saved_state.get('acknowledged_alerts', [])
        st.session_state.pending_power_off_due = saved_state.get('pending_power_off_due')
        st.session_state.pending_power_off_context = saved_state.get(
            'pending_power_off_context'
        )
        # V1.6.30で手動生産終了時の測定必須チェックを廃止したため、
        # 旧版から残った確認待ちは復元しない。
        st.session_state.pending_measurement_required_before_finish = None
        st.session_state.pending_production_finish_confirmation = (
            saved_state.get('pending_production_finish_confirmation')
        )
        st.session_state.pending_signboard_confirmation = (
            saved_state.get('pending_signboard_confirmation')
        )
        local_cost_saving = normalize_cost_saving_data(
            saved_state.get('cost_saving_data')
        )
        if gh_cost_saving is not None:
            st.session_state.cost_saving_data = merge_cost_saving_data(
                gh_cost_saving,
                local_cost_saving,
                prefer_local_settings=False,
            )
        else:
            st.session_state.cost_saving_data = local_cost_saving

        power_state_version = int(
            saved_state.get('mfr_power_state_version', 0)
        )

        if power_state_version >= 2:
            st.session_state.mfr_power_is_on = bool(
                saved_state.get('mfr_power_is_on', False)
            )
            st.session_state.mfr_power_on_confirmed_at = (
                saved_state.get('mfr_power_on_confirmed_at')
            )
        else:
            # V1.5.9以前は確認履歴からON状態を推定していたため、
            # 過去のON確認が新しい生産を誤って抑止する可能性がある。
            # V1.6.0への初回移行時は安全側でOFFとして判定し直す。
            st.session_state.mfr_power_is_on = False
            st.session_state.mfr_power_on_confirmed_at = None

        # ★GitHubのデータがあれば最優先、なければローカルデータ
        st.session_state.products = gh_products if gh_products is not None else saved_state.get('products', {})
    else:
        st.session_state.jobs = {'100t': None, '450t': None, '550t': None}
        st.session_state.last_inspection_date = None
        st.session_state.acknowledged_alerts = []
        st.session_state.pending_power_off_due = None
        st.session_state.pending_power_off_context = None
        st.session_state.pending_measurement_required_before_finish = None
        st.session_state.pending_production_finish_confirmation = None
        st.session_state.pending_signboard_confirmation = None
        st.session_state.cost_saving_data = (
            normalize_cost_saving_data(gh_cost_saving)
            if gh_cost_saving is not None
            else get_default_cost_saving_data()
        )
        st.session_state.mfr_power_is_on = False
        st.session_state.mfr_power_on_confirmed_at = None
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

        if 'production_started_at' not in saved_job:
            inferred_start = None
            try:
                job_stamp = str(saved_job.get('job_id', '')).rsplit('_', 1)[-1]
                inferred_start = datetime.strptime(job_stamp, '%Y%m%d%H%M%S')
            except (TypeError, ValueError):
                pass
            if inferred_start is None:
                inferred_start = saved_job.get('last_update')
            if not isinstance(inferred_start, datetime):
                inferred_start = datetime.utcnow() + timedelta(hours=9)
            saved_job['production_started_at'] = inferred_start

        if 'measurement_records' not in saved_job:
            saved_job['measurement_records'] = []

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
    # 起動時にローカルとクラウドの履歴を統合し、未同期分があれば反映する。
    if GITHUB_TOKEN:
        sync_cost_saving_to_github()
        save_state()

# コード更新中も既存ブラウザーセッションを安全に引き継ぐ
if 'acknowledged_alerts' not in st.session_state:
    st.session_state.acknowledged_alerts = []
if 'pending_power_off_due' not in st.session_state:
    st.session_state.pending_power_off_due = None
if 'pending_power_off_context' not in st.session_state:
    st.session_state.pending_power_off_context = None
if 'pending_measurement_required_before_finish' not in st.session_state:
    st.session_state.pending_measurement_required_before_finish = None
if 'mfr_power_is_on' not in st.session_state:
    st.session_state.mfr_power_is_on = False
if 'mfr_power_on_confirmed_at' not in st.session_state:
    st.session_state.mfr_power_on_confirmed_at = None
if 'pending_production_start' not in st.session_state:
    st.session_state.pending_production_start = None
if 'pending_production_finish_confirmation' not in st.session_state:
    st.session_state.pending_production_finish_confirmation = None
if 'pending_signboard_confirmation' not in st.session_state:
    st.session_state.pending_signboard_confirmation = None
if 'cost_saving_data' not in st.session_state:
    st.session_state.cost_saving_data = get_default_cost_saving_data()

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
                
                st.info(f"✓ 「{p_name} ({p_machine})」をクラウドに登録・更新しました！")
                st.rerun()
        
        # 4. 削除ツール
        st.markdown("---")
        if st.session_state.products:
            del_name = st.selectbox("削除する製品を選択", list(st.session_state.products.keys()), key="del_prod_sel")
            if st.button("🗑️ 選択した製品を削除（クラウド同期）"):
                del st.session_state.products[del_name]
                save_state()
                save_products_to_github(st.session_state.products) # ★削除もGitHubに同期！
                
                st.info(f"✓ 「{del_name}」をクラウドから削除しました。")
                st.rerun()

    st.markdown("---")
    st.subheader("🔧 リセット・テスト用ツール")
    if st.button("🔄 すべての成型機の状態をリセット"):
        st.session_state.jobs = {'100t': None, '450t': None, '550t': None}
        st.session_state.pending_power_off_due = None
        st.session_state.pending_power_off_context = None
        st.session_state.pending_measurement_required_before_finish = None
        st.session_state.mfr_power_is_on = False
        st.session_state.mfr_power_on_confirmed_at = None
        st.session_state.pending_production_start = None
        st.session_state.pending_production_finish_confirmation = None
        st.session_state.pending_signboard_confirmation = None
        save_state(); st.rerun()
        
    if st.button("🔄 今日の点検状態を未実施に戻す"):
        st.session_state.last_inspection_date = None; st.session_state.inspection_dialog_shown = False
        save_state(); st.rerun()

    if st.button("🔕 通知の確認履歴をリセット（テスト用）"):
        # 履歴だけをリセットし、現在の実機電源状態記録は変更しない。
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

    # 実機MFRがすでに加熱済みの状態でゼロから生産開始した場合は、
    # 「始」測定を生産開始直後に実施できる。
    first_measure_due_at = job.get('first_measure_due_at')
    first_target = job['targets'][0] if job.get('targets') else None

    if (
        target == first_target
        and isinstance(first_measure_due_at, datetime)
    ):
        est_time = first_measure_due_at
    else:
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


def complete_mfr_measurement(machine, target_qty):
    """
    MFR測定を完了として記録する。

    通知画面の確認ボタンと成型機パネルの手動ボタンで共通使用する。
    最終測定まで完了した場合は、生産終了確認ダイアログを予約する。
    """
    job = st.session_state.jobs.get(machine)
    if job is None or target_qty not in job.get('targets', []):
        return False

    now_jst = datetime.utcnow() + timedelta(hours=9)

    # 稼働中なら、測定を完了した時点までの推定生産数を確定する。
    if job.get('status') == 'Running':
        elapsed_sec = (now_jst - job['last_update']).total_seconds()
        job['current_qty'] = min(
            int(job['current_qty'] + (elapsed_sec / job['cycle_time'])),
            job['total_qty'],
        )
        job['last_update'] = now_jst

    if target_qty not in job['completed']:
        job['completed'].append(target_qty)

        measurement_records = job.setdefault('measurement_records', [])
        if not any(
            record.get('target_qty') == target_qty
            for record in measurement_records
            if isinstance(record, dict)
        ):
            measurement_records.append({
                'target_qty': target_qty,
                'label': get_measurement_text(
                    len(job.get('targets', [])),
                    target_qty,
                    job.get('targets', []),
                ),
                'measured_at': now_jst.isoformat(timespec='seconds'),
            })

    # このボタンは「MFR測定が完了した後」に押すため、
    # 押下時点＝実際の測定完了時刻として扱う。
    # 次の測定・点検まで十分な空き時間がある場合は、
    # 追加で10分待たず、その場で電源OFFアラートを出す。
    # 90分以内に次の測定・点検がある場合は、次回更新時に自動取消する。
    st.session_state.pending_power_off_due = now_jst
    measurement_label = get_measurement_text(
        len(job.get('targets', [])),
        target_qty,
        job.get('targets', []),
    )
    st.session_state.pending_power_off_context = {
        'type': 'measurement',
        'machine': machine,
        'label': measurement_label,
        'completed_at': now_jst,
    }

    all_measurements_completed = all(
        target in job['completed']
        for target in job['targets']
    )

    if all_measurements_completed:
        # 最終測定＝自動的に生産終了とはせず、作業者へ確認する。
        st.session_state.pending_production_finish_confirmation = {
            'machine': machine,
            'job_id': job.get('job_id'),
        }

    return all_measurements_completed


def undo_mfr_measurement(machine, target_qty):
    """
    誤って完了にした「始」「中」のMFR測定を未測定へ戻す。

    完了記録だけでなく、その測定の通知確認履歴も取り消すため、
    予定時刻・黄色◆・MFR電源ONバー・必要な測定アラートが
    次回rerunで自動的に再計算される。
    """
    job = st.session_state.jobs.get(machine)
    if job is None or target_qty not in job.get('targets', []):
        return False

    targets = list(job.get('targets', []))
    if not targets:
        return False

    # 最終測定「終」は生産終了確認と連動するため、
    # ワンタッチ取消の対象にはしない。
    if target_qty == targets[-1]:
        return False

    if target_qty not in job.get('completed', []):
        return False

    job['completed'] = [
        target for target in job['completed']
        if target != target_qty
    ]
    job['measurement_records'] = [
        record
        for record in job.get('measurement_records', [])
        if not (
            isinstance(record, dict)
            and record.get('target_qty') == target_qty
        )
    ]

    # 通知から測定完了にした場合も、未測定へ戻した時点で
    # 同じ測定の確認履歴を取り消し、必要なら再通知できるようにする。
    job_id = job.get('job_id', machine)
    measurement_alert_id = f"MEAS_{job_id}_{target_qty}"
    measurement_reminder_id = f"MEAS_REMINDER_{job_id}_{target_qty}"
    st.session_state.acknowledged_alerts = [
        alert_id
        for alert_id in st.session_state.acknowledged_alerts
        if str(alert_id) not in (
            measurement_alert_id,
            measurement_reminder_id,
        )
    ]

    # 誤完了によって作られた10分後のOFF予約を解除する。
    # 未測定へ戻したポイントを含め、次回rerunで電源ON区間を再計算する。
    st.session_state.pending_power_off_due = None
    st.session_state.pending_power_off_context = None

    pending_finish = st.session_state.get(
        'pending_production_finish_confirmation'
    )
    if (
        pending_finish
        and pending_finish.get('machine') == machine
        and pending_finish.get('job_id') == job_id
    ):
        st.session_state.pending_production_finish_confirmation = None

    return True


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


def format_next_action_time(dt_value, reference_time):
    """次の作業時刻を「今日／明日／日付」で大きく読みやすく表示する。"""
    if not isinstance(dt_value, datetime):
        return "予定なし"

    if dt_value.date() == reference_time.date():
        return f"今日 {dt_value.strftime('%H:%M')}"
    if dt_value.date() == reference_time.date() + timedelta(days=1):
        return f"明日 {dt_value.strftime('%H:%M')}"
    return dt_value.strftime('%m/%d %H:%M')


def get_next_power_on_time(reference_time=None):
    """現在時刻より後の、最も近いMFR電源ON予定時刻を返す。"""
    if reference_time is None:
        reference_time = datetime.utcnow() + timedelta(hours=9)

    future_starts = [
        block_start
        for block_start, _ in on_blocks
        if block_start > reference_time
    ]
    return min(future_starts) if future_starts else None


def get_next_power_action(reference_time):
    """
    タイムラインの赤いMFR電源ONバー（on_blocks）と同じ予定から、
    作業者が次に行う電源操作を1件だけ返す。

    V1.6.9では、PC側のON記録だけを理由に未来のOFF時刻を先に表示しない。
    これにより「次にやること」とタイムラインの開始／終了時刻を完全に一致させる。
    """
    power_is_on = bool(st.session_state.get('mfr_power_is_on', False))

    # 測定・点検完了後にOFF待ちがある場合は、
    # タイムライン上の未来のON予定よりも実際の次操作を優先する。
    # 測定記録ボタン押下時点でOFF可能なら「今すぐOFF」を表示する。
    pending_off = st.session_state.get('pending_power_off_due')
    if power_is_on and isinstance(pending_off, datetime):
        return 'OFF', pending_off

    # 現在時刻が赤いONバーの中にいる場合：
    # 実機ONなら次はバー終端でOFF、実機OFFならON予定を過ぎているので今すぐON。
    active_blocks = sorted(
        (
            (block_start, block_end)
            for block_start, block_end in on_blocks
            if block_start <= reference_time < block_end
        ),
        key=lambda block: block[0],
    )
    if active_blocks:
        block_start, block_end = active_blocks[0]
        if power_is_on:
            return 'OFF', block_end
        return 'ON', block_start

    # 赤いONバーの外にいる場合は、次に始まるバーの開始時刻＝次のON操作。
    # PC側に古いON記録が残っていても、未来のOFFを先に表示しない。
    future_blocks = sorted(
        (
            (block_start, block_end)
            for block_start, block_end in on_blocks
            if block_start > reference_time
        ),
        key=lambda block: block[0],
    )
    if future_blocks:
        return 'ON', future_blocks[0][0]

    return None, None


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
            elapsed_from_due = now - m_time

            if elapsed_from_due >= timedelta(minutes=10):
                # 測定予定から10分経っても記録されていない場合は、
                # 「測定記録忘れ」を明確にした新しいフォロー通知へ切り替える。
                # IDを別にすることで、通知音・自動スクロールも
                # 10分後に改めて発生させる。
                reminder_id = (
                    f"MEAS_REMINDER_{job_id}_{pt['target_qty']}"
                )

                future_items = [
                    item for item in valid_upcoming
                    if item.get('est_time') is not None
                    and not (
                        item['machine'] == pt['machine']
                        and item['target_qty'] == pt['target_qty']
                    )
                    and item['est_time'] > now
                ]
                future_items.sort(key=lambda item: item['est_time'])
                next_item = future_items[0] if future_items else None

                if next_item is not None:
                    remaining_minutes = max(
                        1,
                        int(math.ceil(
                            (next_item['est_time'] - now).total_seconds()
                            / 60
                        )),
                    )
                    if remaining_minutes > 90:
                        followup_action = (
                            f"次の測定・点検まで"
                            f"{format_remaining_time(remaining_minutes)}あるため、"
                            "測定記録後にMFR測定器の電源をOFFにしてください。"
                        )
                    else:
                        followup_action = (
                            f"次の測定・点検まで"
                            f"{format_remaining_time(remaining_minutes)}です。"
                            "測定記録を確実に行ってください。"
                        )
                else:
                    followup_action = (
                        "次の測定・点検予定がないため、測定記録後に"
                        "MFR測定器の電源をOFFにしてください。"
                    )

                active_alerts.append({
                    "id": reminder_id,
                    "due": m_time + timedelta(minutes=10),
                    "title": "⏰ MFR測定記録アラート",
                    "message": (
                        f"{pt['machine']} 成型機（{meas_text}）の測定予定から"
                        "10分経過しました。測定が完了している場合は、"
                        "下の［測定済みとして記録］を押してください。 "
                        f"{followup_action}"
                    ),
                    "kind": "measurement",
                    "machine": pt['machine'],
                    "target_qty": pt['target_qty'],
                })
            else:
                active_alerts.append({
                    "id": alert_id_meas,
                    "due": m_time,
                    "title": "🎯 MFR測定アラート",
                    "message": (
                        f"{pt['machine']} 成型機（{meas_text}）のMFR測定時刻です。"
                        f" 予定時刻：{m_time.strftime('%m/%d %H:%M')}"
                    ),
                    "kind": "measurement",
                    "machine": pt['machine'],
                    "target_qty": pt['target_qty'],
                })

# 3. 電源ON・OFF
# on_blocks の終了時刻には、最終測定後10分の冷却時間を含めています。
for b_start, b_off in on_blocks:
    target_tasks = [
        x['machine'] for x in valid_upcoming
        if x['est_time'] is not None and b_start <= x['est_time'] <= b_off
    ]
    target_machine = target_tasks[0] if target_tasks else "成型機"

    # 電源ON予定を過ぎても未確認ならアラートを維持する。
    # ただし、一度ON操作を確認して実機が加熱中である間は、
    # 残り予定からon_blocksが再計算されてもONアラートを再発行しない。
    if b_start <= now and not st.session_state.mfr_power_is_on:
        block_measurements = [
            x for x in valid_upcoming
            if (
                x['est_time'] is not None
                and b_start <= x['est_time'] <= b_off
            )
        ]

        if block_measurements:
            first_measure = min(
                block_measurements,
                key=lambda item: item['est_time'],
            )
            first_measure_time = first_measure['est_time']
            target_machine = first_measure['machine']

            if target_machine == '日常点検(A勤)':
                on_context = (
                    f"INSP_"
                    f"{first_measure_time.strftime('%Y%m%d_%H%M')}"
                )
            else:
                first_job = st.session_state.jobs.get(target_machine)
                first_job_id = (
                    first_job.get('job_id', target_machine)
                    if first_job is not None
                    else target_machine
                )
                on_context = (
                    f"{first_job_id}_"
                    f"{first_measure['target_qty']}"
                )
        else:
            first_measure_time = b_start + timedelta(minutes=60)
            on_context = b_start.strftime('%Y%m%d_%H%M%S')

        # 同じ時刻の過去テスト履歴と衝突しないよう、
        # Lot/測定ポイントを含む固有IDにする。
        alert_id_on = (
            f"ON_{on_context}_"
            f"{b_start.strftime('%Y%m%d_%H%M%S')}"
        )

        if alert_id_on not in st.session_state.acknowledged_alerts:
            active_alerts.append({
                "id": alert_id_on,
                "due": b_start,
                "title": "🔥 MFR電源ONアラート",
                "message": (
                    f"MFR測定器の電源をONにしてください。"
                    f" 対象：{target_machine}／"
                    f"最初の予定：{first_measure_time.strftime('%m/%d %H:%M')}"
                ),
                "kind": "power_on",
            })

# 4. 実際の測定完了後、次予定が遠ければ即時電源OFF
pending_off_due = st.session_state.pending_power_off_due
if pending_off_due is not None:
    # 未完了の測定・点検が「完了時刻より後、90分以内」に残る場合だけ、
    # 電源を維持するためOFF予約を取り消す。
    # 過去時刻の未完了予定が残っていてもOFF判断を邪魔させない。
    off_context = st.session_state.get('pending_power_off_context') or {}
    completion_time = off_context.get('completed_at')
    if not isinstance(completion_time, datetime):
        completion_time = pending_off_due

    keep_power_on = any(
        item['est_time'] is not None
        and completion_time < item['est_time']
        and item['est_time'] <= completion_time + timedelta(minutes=90)
        for item in valid_upcoming
    )

    if keep_power_on:
        st.session_state.pending_power_off_due = None
        st.session_state.pending_power_off_context = None
        save_state()
    elif now >= pending_off_due:
        off_context = st.session_state.get('pending_power_off_context') or {}
        off_source_key = str(off_context.get('machine') or off_context.get('type') or 'MFR')
        off_source_key = ''.join(ch for ch in off_source_key if ch.isalnum() or ch in ('-', '_'))
        alert_id_off = (
            f"OFF_ACTUAL_{pending_off_due.strftime('%Y%m%d_%H%M%S')}_{off_source_key}"
        )
        if alert_id_off not in st.session_state.acknowledged_alerts:
            context_type = off_context.get('type')

            if context_type == 'measurement':
                source_text = (
                    f"{off_context.get('machine', '対象')}の成型機の"
                    f"「{off_context.get('label', 'MFR')}」の測定が完了しました。"
                )
            elif context_type == 'inspection':
                source_text = "日常点検が完了しました。"
            else:
                source_text = "最後の測定・点検が完了しました。"

            next_mfr_after_off = next(
                (
                    item for item in valid_upcoming
                    if item['machine'] != '日常点検(A勤)'
                    and item.get('est_time') is not None
                    and item['est_time'] > now
                ),
                None,
            )

            if next_mfr_after_off is not None:
                remaining_minutes = max(
                    1,
                    int(math.ceil(
                        (next_mfr_after_off['est_time'] - now).total_seconds()
                        / 60
                    )),
                )
                next_measure_text = (
                    f"次の測定まで{format_remaining_time(remaining_minutes)}あるため、"
                )
            else:
                next_measure_text = "次のMFR測定予定がないため、"

            active_alerts.append({
                "id": alert_id_off,
                "due": pending_off_due,
                "title": "💤 MFR電源OFFアラート",
                "message": (
                    f"{source_text} {next_measure_text}"
                    "MFR測定器の電源をOFFにしてください。"
                ),
                "kind": "power_off",
            })

active_alerts.sort(key=lambda item: item["due"])


# --- UI：ヘッダー（QRシステムと同じサイズ感に統一） ---
# 通知発生時にページ最上部へ確実に戻すための専用アンカー。
st.markdown(
    '<div id="mfr-page-top-anchor" style="height:1px; margin:0; padding:0; scroll-margin-top:0;"></div>',
    unsafe_allow_html=True,
)
try:
    logo_base64 = get_image_base64(logo_path)
    logo_html = f"""
    <div style="display: flex; align-items: flex-end; gap: 16px; flex-wrap: wrap; margin-bottom: 1rem;">
        <img src="data:image/png;base64,{logo_base64}" height="100" style="flex-shrink: 0;">
        <div style="display: flex; align-items: flex-end; gap: 16px; flex-wrap: wrap;">
            <span style="font-size: calc(1.4rem + 1.2vw); font-weight: 700; line-height: 1.0; color: #1f2937;">MFRスマート電源管理システム</span>
            <span style="font-size: calc(0.95rem + 0.35vw); font-weight: 800; line-height: 1.1; color: #475569; margin-bottom: 0.20rem;">Ver. {APP_VERSION}</span>
        </div>
    </div>
    """
    st.markdown(logo_html, unsafe_allow_html=True)
except:
    st.markdown(
        f"## MFRスマート電源管理システム　<span style='font-size:1.1rem;color:#475569;'>Ver. {APP_VERSION}</span>",
        unsafe_allow_html=True,
    )

st.caption(f"現在時刻　{now.strftime('%Y/%m/%d %H:%M')}")

# --- 上部ダッシュボード：通知 → MFR状態 → 成型機 の順に優先表示 ---
st.markdown('<div class="top-section-title">🔔 通知</div>', unsafe_allow_html=True)
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
        <div id="mfr-active-alert-anchor" style="scroll-margin-top:12px;"></div>
        <div class="mfr-active-alert">
            <div style="font-size:1.7rem;font-weight:800;">{primary_alert["title"]}</div>
            <div style="font-size:1.25rem;margin-top:8px;">{primary_alert["message"]}</div>
            <div style="font-size:1rem;margin-top:8px;">予定から {overdue_time_text} 経過</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    scroll_to_active_alert(primary_alert["id"])

    if primary_alert["kind"] == "measurement":
        ack_button_text = "✅ 測定済みとして記録（通知音を停止）"
    else:
        ack_button_text = "✅ 確認しました（通知音を停止）"

    if st.button(
        ack_button_text,
        key=f"ack_{primary_alert['id']}",
        type="primary",
    ):
        cost_saving_changed = False

        if primary_alert["kind"] == "measurement":
            # 測定通知の確認＝実際のMFR測定完了として同時に記録する。
            complete_mfr_measurement(
                primary_alert["machine"],
                primary_alert["target_qty"],
            )

        st.session_state.acknowledged_alerts.append(primary_alert["id"])

        if primary_alert["kind"] == "power_on":
            # 作業者が実際にMFR電源をONにした時点を、加熱開始時刻として記録。
            power_on_confirmed_at = (
                datetime.utcnow() + timedelta(hours=9)
            )
            st.session_state.mfr_power_is_on = True
            st.session_state.mfr_power_on_confirmed_at = (
                power_on_confirmed_at
            )
            cost_saving_changed = record_power_event(
                "ON",
                power_on_confirmed_at,
                primary_alert["id"],
                primary_alert.get("due"),
            ) or cost_saving_changed

            # 「実機OFF」と確認していたLotは、実際にON操作を確認した
            # この時点から60分後を測定可能時刻として数え直す。
            ready_at = (
                power_on_confirmed_at
                + timedelta(minutes=MFR_WARMUP_MINUTES)
            )
            for waiting_job in st.session_state.jobs.values():
                if (
                    waiting_job is not None
                    and waiting_job.get('status') in ('Running', 'Paused')
                    and waiting_job.get('waiting_for_mfr_power_on', False)
                ):
                    waiting_job['heat_ready_at'] = ready_at
                    waiting_job['waiting_for_mfr_power_on'] = False
                    waiting_job['first_measure_due_at'] = None

        elif primary_alert["kind"] == "power_off":
            # 作業者が実際にMFR電源をOFFにしたことを記録。
            power_off_confirmed_at = (
                datetime.utcnow() + timedelta(hours=9)
            )
            st.session_state.mfr_power_is_on = False
            st.session_state.mfr_power_on_confirmed_at = None
            st.session_state.pending_power_off_due = None
            st.session_state.pending_power_off_context = None
            cost_saving_changed = record_power_event(
                "OFF",
                power_off_confirmed_at,
                primary_alert["id"],
                primary_alert.get("due"),
            ) or cost_saving_changed

            # OFF確認直後に、次回ON予定を表示札へ記入したか確認する。
            next_on_time = get_next_power_on_time(
                datetime.utcnow() + timedelta(hours=9)
            )
            st.session_state.pending_signboard_confirmation = {
                'next_on_time': next_on_time,
                'off_confirmed_at': datetime.utcnow() + timedelta(hours=9),
            }

        save_state()
        if cost_saving_changed:
            sync_cost_saving_to_github()
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
    st.markdown(
        '<div class="status-card status-blue">✓ アラートなし</div>',
        unsafe_allow_html=True,
    )

st.caption("※シフト開始時に青いボタンを1回押し、Edgeは開いたままにしてください。")

st.markdown('<div class="top-section-title">💡 MFR状態</div>', unsafe_allow_html=True)
status_col, inspection_col = st.columns([1.25, 1.0])

with status_col:
    st.markdown("**MFR電源**")

    if st.session_state.get('mfr_power_is_on', False):
        st.markdown(
            '<div class="status-card status-blue">⚡ MFR電源 ON</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="status-card status-gray">○ MFR電源 OFF</div>',
            unsafe_allow_html=True,
        )


with inspection_col:
    st.markdown("**日常点検**")
    is_monday = (today_date.weekday() == 0)
    inspection_start_time = datetime.combine(
        today_date,
        dt_time(8 if is_monday else 7, 0, 0),
    )

    if st.session_state.last_inspection_date == today_date:
        st.markdown(
            '<div class="status-card status-blue">✅ 点検済み</div>',
            unsafe_allow_html=True,
        )
    elif now >= inspection_start_time:
        st.markdown(
            f'<div class="status-card status-red">! 点検未完了 '
            f'（{inspection_start_time.strftime("%H:%M")}予定）</div>',
            unsafe_allow_html=True,
        )
        if st.button("✅ 日常点検 完了", key="inspection_complete_top"):
            st.session_state.last_inspection_date = today_date
            st.session_state.pending_power_off_due = (
                now + timedelta(minutes=10)
            )
            st.session_state.pending_power_off_context = {
                'type': 'inspection',
                'completed_at': now,
            }
            save_state()
            st.rerun()
    else:
        st.markdown(
            f'<div class="status-card status-yellow">○ 点検未実施 '
            f'（{inspection_start_time.strftime("%H:%M")}開始）</div>',
            unsafe_allow_html=True,
        )

# --- UI：次にやること（タイムラインと同じ予定を時刻順に表示） ---
st.header("⏭️ 次にやること")

next_power_action, next_power_time = get_next_power_action(now)
next_mfr = next(
    (
        item for item in valid_upcoming
        if item['machine'] != '日常点検(A勤)'
        and item['est_time'] is not None
    ),
    None,
)

# 電源操作とMFR測定を同じ「次の作業」として扱い、予定時刻で並べ替える。
# 早い作業を左、遅い作業を右へ自動配置する。
next_actions = []

if next_power_action and isinstance(next_power_time, datetime):
    next_actions.append({
        'type': 'power',
        'time': next_power_time,
        'power_action': next_power_action,
    })

if next_mfr is not None and isinstance(next_mfr.get('est_time'), datetime):
    next_actions.append({
        'type': 'measurement',
        'time': next_mfr['est_time'],
        'measurement': next_mfr,
    })

# 同時刻の場合は電源操作を先にする（通常はONが測定60分前なので同時にはならない）。
next_actions.sort(
    key=lambda item: (
        item['time'],
        0 if item['type'] == 'power' else 1,
    )
)

# 2列を維持するため、予定が1件だけの場合は右側を「予定なし」とする。
while len(next_actions) < 2:
    next_actions.append({
        'type': 'none',
        'time': None,
    })

left_col, right_col = st.columns(2)

for order_no, (column, action_item) in enumerate(
    zip((left_col, right_col), next_actions[:2]),
    start=1,
):
    with column:
        action_type = action_item['type']

        if action_type == 'power':
            action_time = action_item['time']
            power_action = action_item['power_action']
            time_text = format_next_action_time(action_time, now)
            is_overdue = action_time <= now
            card_class = (
                "next-action-red"
                if is_overdue
                else "next-action-yellow"
            )

            if power_action == 'ON':
                action_icon = "⚡"
                action_text = "MFR電源 ON"
            else:
                action_icon = "○"
                action_text = "MFR電源 OFF"

            if is_overdue:
                sub_text = (
                    f"予定 {action_time.strftime('%H:%M')}　"
                    "→ 今すぐ操作してください"
                )
            else:
                remaining_min = max(
                    0,
                    int((action_time - now).total_seconds() // 60),
                )
                sub_text = f"あと {format_remaining_time(remaining_min)}"

            st.markdown(
                f"""
                <div class="next-action-card {card_class}">
                    <div class="next-action-label">{"①" if order_no == 1 else "②"} 次の電源操作</div>
                    <div class="next-action-main">{action_icon} {action_text}</div>
                    <div class="next-action-main">{time_text}</div>
                    <div class="next-action-sub">{sub_text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        elif action_type == 'measurement':
            measurement = action_item['measurement']
            measurement_time = action_item['time']
            measurement_time_text = format_next_action_time(
                measurement_time,
                now,
            )
            meas_text = get_measurement_text(
                len(measurement['Targets']),
                measurement['target_qty'],
                measurement['Targets'],
            )
            remaining_min = max(
                0,
                int((measurement_time - now).total_seconds() // 60),
            )
            measure_class = (
                "next-action-red"
                if measurement_time <= now
                else "next-action-blue"
            )
            sub_text = (
                "測定時刻です。今すぐ確認してください"
                if measurement_time <= now
                else f"あと {format_remaining_time(remaining_min)}"
            )

            st.markdown(
                f"""
                <div class="next-action-card {measure_class}">
                    <div class="next-action-label">{"①" if order_no == 1 else "②"} 次のMFR測定</div>
                    <div class="next-action-main">🎯 {measurement['machine']}・{meas_text} 測定</div>
                    <div class="next-action-main">{measurement_time_text}</div>
                    <div class="next-action-sub">{sub_text}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:
            st.markdown(
                f"""
                <div class="next-action-card next-action-gray">
                    <div class="next-action-label">{"①" if order_no == 1 else "②"} 次の予定</div>
                    <div class="next-action-main">予定なし</div>
                    <div class="next-action-sub">現在、次に必要な操作はありません。</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

st.caption(
    "※タイムラインと同じ予定を使用し、時刻が早い作業を左側に表示しています。"
)

st.markdown("---")


def has_mfr_measurement_since(power_on_at, reference_time=None):
    """
    現在のMFR電源ON期間中に、すでに実測定が完了しているかを判定する。

    1回でも実測定が完了していれば、その時点でMFRは測定可能温度に
    到達していたことが確認できるため、新規Lotの「始」測定を
    追加の60分待ちにしない。
    """
    if not isinstance(power_on_at, datetime):
        return False

    if reference_time is None:
        reference_time = datetime.utcnow() + timedelta(hours=9)

    for active_job in st.session_state.jobs.values():
        if active_job is None:
            continue

        for record in active_job.get('measurement_records', []):
            if not isinstance(record, dict):
                continue

            measured_at = record.get('measured_at')
            if isinstance(measured_at, datetime):
                measured_dt = measured_at
            elif isinstance(measured_at, str):
                try:
                    measured_dt = datetime.fromisoformat(measured_at)
                except ValueError:
                    continue
            else:
                continue

            if power_on_at <= measured_dt <= reference_time:
                return True

    return False


def finalize_production_start_with_actual_power(power_is_on):
    """
    生産開始時に作業者が目視確認した実機MFR電源状態を正として、
    PC側の電源状態と測定予定を同期する。
    """
    pending = st.session_state.get('pending_production_start')
    if not pending:
        return

    now_jst = datetime.utcnow() + timedelta(hours=9)
    start_timestamp = pending['start_timestamp']
    machine = pending['machine']
    current_qty = int(pending['current_qty'])
    targets = list(pending['targets'])
    completed = list(pending['completed'])

    previous_power_is_on = bool(
        st.session_state.get('mfr_power_is_on', False)
    )
    previous_power_on_at = st.session_state.get(
        'mfr_power_on_confirmed_at'
    )

    first_measure_due_at = None

    if power_is_on:
        # 実機ONを最優先する。
        st.session_state.mfr_power_is_on = True
        mfr_ready_now = False

        if (
            previous_power_is_on
            and isinstance(previous_power_on_at, datetime)
        ):
            # 別の成形機ですでにONしている場合は、
            # その加熱開始時刻をそのまま引き継ぐ。
            power_on_at = previous_power_on_at
            heat_ready_at = (
                power_on_at
                + timedelta(minutes=MFR_WARMUP_MINUTES)
            )

            # 60分未満でも、このON期間中に他LotのMFR測定が
            # すでに完了していれば、実機は測定可能状態と判断する。
            # 例：100tの「始」測定済み後に450tを開始した場合。
            mfr_ready_now = (
                heat_ready_at <= now_jst
                or has_mfr_measurement_since(
                    power_on_at,
                    now_jst,
                )
            )

            if mfr_ready_now:
                heat_ready_at = now_jst
        else:
            # PC記録と不一致で「実機はON」と回答された場合は、
            # 作業者の実機確認を優先し、すでに測定可能なON状態として扱う。
            # これによりゼロ開始なら「始」測定をすぐ実施できる。
            power_on_at = (
                now_jst
                - timedelta(minutes=MFR_WARMUP_MINUTES)
            )
            heat_ready_at = now_jst
            mfr_ready_now = True

            # 他の稼働中Lotも、実機が加熱済みであるという
            # 作業者確認に同期する。
            for active_job in st.session_state.jobs.values():
                if (
                    active_job is not None
                    and active_job.get('status') in ('Running', 'Paused')
                ):
                    active_job['heat_ready_at'] = now_jst
                    active_job['waiting_for_mfr_power_on'] = False
                    active_job['first_measure_due_at'] = None

        st.session_state.mfr_power_on_confirmed_at = power_on_at

        # MFRがすでに測定可能で、ゼロから開始するLotなら、
        # 「始」測定を生産開始直後の予定にする。
        if mfr_ready_now:
            heat_ready_at = now_jst
            if (
                current_qty == 0
                and targets
                and targets[0] not in completed
            ):
                first_measure_due_at = start_timestamp

        waiting_for_mfr_power_on = False

    else:
        # 実機OFFを最優先する。
        st.session_state.mfr_power_is_on = False
        st.session_state.mfr_power_on_confirmed_at = None

        # 過去のON確認履歴によって新しいONアラートが抑止されないよう、
        # ON系の確認履歴だけを破棄する。
        st.session_state.acknowledged_alerts = [
            alert_id
            for alert_id in st.session_state.acknowledged_alerts
            if not str(alert_id).startswith("ON_")
        ]

        # この時点ではまだ実際のON操作をしていないため、
        # 暫定的に60分後を測定可能時刻とする。
        # ONアラート確認時に「実際にONした時刻＋60分」へ再補正する。
        heat_ready_at = (
            now_jst + timedelta(minutes=MFR_WARMUP_MINUTES)
        )
        waiting_for_mfr_power_on = True

        # MFRが実際にOFFなら、他の稼働中Lotも同じ測定器を使えない。
        # すべての未完了Lotを加熱待ち状態へ同期する。
        for active_job in st.session_state.jobs.values():
            if (
                active_job is not None
                and active_job.get('status') in ('Running', 'Paused')
            ):
                active_job['heat_ready_at'] = heat_ready_at
                active_job['waiting_for_mfr_power_on'] = True
                active_job['first_measure_due_at'] = None

    st.session_state.jobs[machine] = {
        'job_id': (
            f"{machine}_"
            f"{start_timestamp.strftime('%Y%m%d%H%M%S')}"
        ),
        'product_name': pending['product_name'],
        'total_qty': pending['total_qty'],
        'cycle_time': pending['cycle_time'],
        'current_qty': current_qty,
        'last_update': start_timestamp,
        'production_started_at': start_timestamp,
        'measurement_records': [],
        'heat_ready_at': heat_ready_at,
        'waiting_for_mfr_power_on': waiting_for_mfr_power_on,
        'first_measure_due_at': first_measure_due_at,
        'targets': targets,
        'completed': completed,
        'status': 'Running',
    }

    st.session_state.pending_production_start = None
    save_state()
    st.rerun()


def finish_production(machine, job_id):
    """最終測定後の確認で「はい」が選ばれた成型機を生産完了にする。"""
    job = st.session_state.jobs.get(machine)
    if job is None or job.get('job_id') != job_id:
        stop_dialog_reminder()
        st.session_state.pending_production_finish_confirmation = None
        save_state()
        return

    ended_at = datetime.utcnow() + timedelta(hours=9)
    # 途中終了にも対応するため、予定生産数へ強制的に合わせない。
    # 稼働中なら終了ボタンを押した時点までの推定生産数を確定する。
    if job.get('status') == 'Running':
        elapsed_sec = max(
            0.0,
            (ended_at - job['last_update']).total_seconds(),
        )
        job['current_qty'] = min(
            int(job['current_qty'] + (elapsed_sec / job['cycle_time'])),
            job['total_qty'],
        )
        job['last_update'] = ended_at
    # 履歴保存用に生産終了状態を確定するが、画面上には終了状態を残さない。
    # Cost Savingへ履歴を保存した直後に、その成型機を停止中（job=None）へ戻す。
    job['status'] = 'Completed'
    job['production_ended_at'] = ended_at
    archive_production_job(
        machine,
        job,
        ended_at,
        'final_measurement_confirmed',
    )
    st.session_state.pending_production_finish_confirmation = None
    st.session_state.jobs[machine] = None
    save_state()
    sync_cost_saving_to_github()
    save_state()
    st.rerun()


def get_missing_measurement_labels(job):
    """生産終了前に未記録となっているMFR測定ラベルを返す。"""
    targets = list(job.get('targets', [])) if job else []
    completed = set(job.get('completed', [])) if job else set()
    return [
        get_measurement_text(len(targets), target, targets)
        for target in targets
        if target not in completed
    ]


def render_measurement_required_before_finish_dialog():
    """未記録のMFR測定がある状態では生産終了させない。"""
    pending = st.session_state.get(
        'pending_measurement_required_before_finish'
    )
    if not pending:
        return

    machine = pending.get('machine')
    job_id = pending.get('job_id')
    job = st.session_state.jobs.get(machine)

    if job is None or job.get('job_id') != job_id:
        stop_dialog_reminder()
        st.session_state.pending_measurement_required_before_finish = None
        save_state()
        return

    missing_labels = get_missing_measurement_labels(job)
    if not missing_labels:
        stop_dialog_reminder()
        st.session_state.pending_measurement_required_before_finish = None
        save_state()
        return

    st.markdown("### MFR測定記録が未完了です")
    st.caption(f"{machine} 成型機 ｜ {job.get('product_name', '')}")
    st.warning(
        "生産を終了する前に、必要なMFR測定をすべて実施し、"
        "MFR測定の記録ボタンを押してください。"
    )
    st.markdown(
        "**未記録：** " + "・".join(missing_labels) + " 測定"
    )
    st.info(
        "予定数量の途中で生産を終了する場合でも、"
        "製品マスターで設定された回数分のMFR測定記録が必要です。"
    )

    if st.button(
        "↩️ 測定記録へ戻る",
        type="primary",
        use_container_width=True,
        key=f"return_measurement_{machine}_{job_id}",
    ):
        stop_dialog_reminder()
        st.session_state.pending_measurement_required_before_finish = None
        save_state()
        st.rerun()


def render_production_finish_confirmation_dialog():
    """最終MFR測定完了後に、生産も終了したかを簡潔に確認する。"""
    pending = st.session_state.get(
        'pending_production_finish_confirmation'
    )
    if not pending:
        return

    machine = pending.get('machine')
    job_id = pending.get('job_id')
    job = st.session_state.jobs.get(machine)

    # すでに別Lotへ切り替わっている場合は古い確認を破棄する。
    if job is None or job.get('job_id') != job_id:
        stop_dialog_reminder()
        st.session_state.pending_production_finish_confirmation = None
        save_state()
        return

    st.markdown("### 最後のMFR測定を完了しました")
    st.caption(f"{machine} 成型機 ｜ {job.get('product_name', '')}")
    st.write("この製品の生産も終了ですか？")

    col_yes, col_no = st.columns(2)

    with col_yes:
        if st.button(
            "✅ はい（生産終了）",
            type="primary",
            use_container_width=True,
            key=f"finish_yes_{machine}_{job_id}",
        ):
            stop_dialog_reminder()
            finish_production(machine, job_id)

    with col_no:
        if st.button(
            "いいえ（生産継続）",
            use_container_width=True,
            key=f"finish_no_{machine}_{job_id}",
        ):
            stop_dialog_reminder()
            st.session_state.pending_production_finish_confirmation = None
            save_state()
            st.rerun()


def render_signboard_confirmation_dialog():
    """MFR電源OFF確認後に、表示札への次回ON時刻記入を確認する。"""
    pending = st.session_state.get('pending_signboard_confirmation')
    if not pending:
        return

    next_on_time = pending.get('next_on_time')
    now_jst = datetime.utcnow() + timedelta(hours=9)

    st.markdown("### MFR電源表示札を確認してください")

    if isinstance(next_on_time, datetime):
        next_on_text = format_next_action_time(next_on_time, now_jst)
        st.markdown(
            f"<div style='font-size:2rem;font-weight:900;"
            f"text-align:center;color:#0b2f6b;margin:0.5rem 0 0.8rem;'>"
            f"次の電源ON　{next_on_text}</div>",
            unsafe_allow_html=True,
        )
        st.write("次の電源ON予定時刻を表示札に記入しましたか？")
        confirm_text = "✅ はい、記入しました"
    else:
        st.markdown(
            "<div style='font-size:1.7rem;font-weight:900;"
            "text-align:center;color:#334155;margin:0.5rem 0 0.8rem;'>"
            "次の電源ON予定はありません</div>",
            unsafe_allow_html=True,
        )
        st.write("表示札をOFF状態にしましたか？")
        confirm_text = "✅ はい、確認しました"

    if st.button(
        confirm_text,
        type="primary",
        use_container_width=True,
        key="confirm_signboard_written",
    ):
        stop_dialog_reminder()
        st.session_state.pending_signboard_confirmation = None
        save_state()
        st.rerun()


def render_mfr_power_confirmation_dialog():
    """生産開始時に、実機MFRの現在の電源状態だけを簡潔に確認する。"""
    pending = st.session_state.get('pending_production_start')
    if not pending:
        return

    machine = pending['machine']
    product_name = pending['product_name']

    # 現場では判断に必要な情報だけを表示する。
    # PC側の記録、他機の稼働状況、加熱引継ぎなどの詳細は
    # 内部ロジックで処理し、このダイアログには表示しない。
    st.markdown("### 実機のMFR電源は？")
    st.caption(f"{machine} 成型機 ｜ {product_name}")
    st.write("MFR測定器を見て、現在の状態を選択してください。")

    col_on, col_off = st.columns(2)

    with col_on:
        if st.button(
            "⚡ ON",
            type="primary",
            use_container_width=True,
            key="confirm_mfr_power_on",
        ):
            stop_dialog_reminder()
            finalize_production_start_with_actual_power(True)

    with col_off:
        if st.button(
            "○ OFF",
            use_container_width=True,
            key="confirm_mfr_power_off",
        ):
            stop_dialog_reminder()
            finalize_production_start_with_actual_power(False)

    if st.button(
        "キャンセル",
        use_container_width=True,
        key="cancel_pending_production_start",
    ):
        stop_dialog_reminder()
        st.session_state.pending_production_start = None
        st.rerun()


# 電源OFF後の表示札記入確認ダイアログ。
if hasattr(st, "dialog"):
    show_signboard_confirmation_dialog = st.dialog(
        "📝 表示札の確認",
        width="small",
    )(render_signboard_confirmation_dialog)
elif hasattr(st, "experimental_dialog"):
    show_signboard_confirmation_dialog = st.experimental_dialog(
        "📝 表示札の確認",
    )(render_signboard_confirmation_dialog)
else:
    show_signboard_confirmation_dialog = render_signboard_confirmation_dialog


# 生産終了ボタン押下時、MFR測定記録が不足している場合のダイアログ。
if hasattr(st, "dialog"):
    show_measurement_required_before_finish_dialog = st.dialog(
        "📋 MFR測定記録の確認",
        width="small",
    )(render_measurement_required_before_finish_dialog)
elif hasattr(st, "experimental_dialog"):
    show_measurement_required_before_finish_dialog = st.experimental_dialog(
        "📋 MFR測定記録の確認",
    )(render_measurement_required_before_finish_dialog)
else:
    show_measurement_required_before_finish_dialog = (
        render_measurement_required_before_finish_dialog
    )


# 最終測定後の生産終了確認ダイアログ。
if hasattr(st, "dialog"):
    show_production_finish_confirmation_dialog = st.dialog(
        "🏁 生産終了の確認",
        width="small",
    )(render_production_finish_confirmation_dialog)
elif hasattr(st, "experimental_dialog"):
    show_production_finish_confirmation_dialog = st.experimental_dialog(
        "🏁 生産終了の確認",
    )(render_production_finish_confirmation_dialog)
else:
    show_production_finish_confirmation_dialog = (
        render_production_finish_confirmation_dialog
    )


# Streamlitのバージョンに応じて正式ダイアログを使用。
if hasattr(st, "dialog"):
    show_mfr_power_confirmation_dialog = st.dialog(
        "🔌 MFR電源を確認",
        width="small",
    )(render_mfr_power_confirmation_dialog)
elif hasattr(st, "experimental_dialog"):
    show_mfr_power_confirmation_dialog = st.experimental_dialog(
        "🔌 MFR電源を確認",
    )(render_mfr_power_confirmation_dialog)
else:
    # 古いStreamlitでは通常表示へフォールバック。
    show_mfr_power_confirmation_dialog = (
        render_mfr_power_confirmation_dialog
    )


if st.session_state.get('pending_signboard_confirmation'):
    start_dialog_reminder("signboard_confirmation")
    show_signboard_confirmation_dialog()
elif st.session_state.get('pending_production_finish_confirmation'):
    pending = st.session_state.get('pending_production_finish_confirmation') or {}
    start_dialog_reminder(
        f"production_finish_{pending.get('machine', '')}_{pending.get('job_id', '')}"
    )
    show_production_finish_confirmation_dialog()
elif st.session_state.get('pending_production_start'):
    pending = st.session_state.get('pending_production_start') or {}
    start_dialog_reminder(
        f"mfr_power_{pending.get('machine', '')}_{pending.get('product_name', '')}"
    )
    show_mfr_power_confirmation_dialog()
else:
    stop_dialog_reminder()


# V1.6.21以前の保存データで「Completed」が残っている場合も、
# 成型機画面は自動的に停止中へ戻す。
legacy_completed_cleared = False
for machine_name, saved_job in list(st.session_state.jobs.items()):
    if saved_job is not None and saved_job.get('status') == 'Completed':
        ended_at = saved_job.get('production_ended_at')
        if not isinstance(ended_at, datetime):
            ended_at = datetime.utcnow() + timedelta(hours=9)
        archive_production_job(
            machine_name,
            saved_job,
            ended_at,
            'legacy_completed_auto_clear',
        )
        st.session_state.jobs[machine_name] = None
        legacy_completed_cleared = True

if legacy_completed_cleared:
    save_state()
    sync_cost_saving_to_github()
    save_state()
    st.rerun()

# --- UI：成型機コントロールパネル ---
st.markdown('<div class="top-section-title">🏭 成型機</div>', unsafe_allow_html=True)
cols_top = st.columns(3)
machine_data = {}

for idx, machine in enumerate(['100t', '450t', '550t']):
    with cols_top[idx]:
        st.header(f"⚙️ {machine} 成型機")
        job = st.session_state.jobs[machine]
        est_current = 0
        
        if job is None:
            st.markdown(
                '<div class="machine-status-badge machine-idle-badge">'
                '<span class="machine-status-icon-circle">●</span>'
                '<span class="machine-status-label">停止中</span></div>',
                unsafe_allow_html=True,
            )
            # ★その成型機用に登録された製品だけを抽出（※機種設定がない古いデータは全成型機に表示してエラー回避）
            machine_products = [p_name for p_name, p_info in st.session_state.products.items() if p_info.get('machine', machine) == machine]
            
            if not machine_products:
                st.warning(f"⚠️ サイドバーから {machine} 用の製品マスターを登録してください。")
            else:
                product_name = st.selectbox("製品名を選択", machine_products, key=f"prod_sel_{machine}")
                prod_info = st.session_state.products[product_name]
                total_qty, cycle_time, meas_count = prod_info['qty'], prod_info['cycle'], prod_info['measurements']
                
                st.caption(
                    f"生産数 {total_qty}個 ｜ サイクル {cycle_time:g}秒 ｜ "
                    f"MFR測定 {meas_count}回"
                )
                
                if meas_count == 2: targets = [1, total_qty]
                else: targets = [1, total_qty] if total_qty <= 2 else [1, total_qty // 2, total_qty]

                current_qty = 0
                completed = []
                with st.expander("途中から開始する場合", expanded=False):
                    current_qty = st.number_input(
                        "現在の生産数",
                        min_value=0,
                        max_value=int(total_qty),
                        value=0,
                        step=1,
                        key=f"cur_{machine}",
                    )
                    default_completed = [t for t in targets if t <= current_qty]
                    completed = st.multiselect(
                        "測定済み",
                        options=targets,
                        default=default_completed,
                        format_func=lambda x: f"{x}個目",
                        key=f"comp_sel_{machine}",
                    )

                if st.button("▶️ 生産開始", key=f"start_btn_{machine}"):
                    # 実際のMFR電源状態を確認してからジョブを確定する。
                    st.session_state.pending_production_start = {
                        'machine': machine,
                        'product_name': product_name,
                        'total_qty': total_qty,
                        'cycle_time': cycle_time,
                        'current_qty': current_qty,
                        'targets': list(targets),
                        'completed': list(completed),
                        'start_timestamp': (
                            datetime.utcnow() + timedelta(hours=9)
                        ),
                    }
                    st.rerun()
        else:
            if job['status'] == 'Running':
                st.markdown(
                    '<div class="machine-status-badge machine-running-badge">'
                    '<span class="machine-status-icon-circle"><span class="machine-spin">⟳</span></span>'
                    '<span class="machine-status-label">成型中</span></div>',
                    unsafe_allow_html=True,
                )
            elif job['status'] == 'Paused':
                st.markdown(
                    '<div class="machine-status-badge machine-paused-badge">'
                    '<span class="machine-status-icon-circle">⏸</span>'
                    '<span class="machine-status-label">一時停止</span></div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    '<div class="machine-status-badge machine-completed-badge">'
                    '<span class="machine-status-icon-circle">☑</span>'
                    '<span class="machine-status-label">生産終了</span></div>',
                    unsafe_allow_html=True,
                )

            p_name = job.get('product_name', '設定なし')
            st.caption(
                f"{p_name} ｜ {job['total_qty']}個 ｜ "
                f"{job['cycle_time']:g}秒/個"
            )

            if job['status'] == 'Running':
                elapsed_sec = ((datetime.utcnow() + timedelta(hours=9)) - job['last_update']).total_seconds()
                est_current = min(int(job['current_qty'] + (elapsed_sec / job['cycle_time'])), job['total_qty'])
            else:
                est_current = job['current_qty']
                
            st.metric("推定生産数", f"{est_current} / {job['total_qty']}")
            
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
                        # V1.6.30: 手動の［生産終了］は、未測定のMFRポイントが
                        # 残っていても作業者の終了判断を優先し、即時停止する。
                        ended_at = datetime.utcnow() + timedelta(hours=9)
                        job['current_qty'] = est_current
                        job['last_update'] = ended_at
                        job['status'] = 'Completed'
                        job['production_ended_at'] = ended_at
                        archive_production_job(
                            machine,
                            job,
                            ended_at,
                            'manual_end',
                        )

                        # この成型機に残っている旧確認待ちを解除し、
                        # 履歴保存後すぐに停止中（job=None）へ戻す。
                        pending_finish = st.session_state.get(
                            'pending_production_finish_confirmation'
                        )
                        if pending_finish and pending_finish.get('machine') == machine:
                            st.session_state.pending_production_finish_confirmation = None
                        st.session_state.pending_measurement_required_before_finish = None
                        st.session_state.jobs[machine] = None
                        save_state()
                        sync_cost_saving_to_github()
                        save_state()
                        st.rerun()

            st.divider()
            st.markdown('<div class="mfr-status-header">📋 MFR測定</div>', unsafe_allow_html=True)
            num_targets = len(job['targets'])
            final_target = job['targets'][-1] if job['targets'] else None

            for t in job['targets']:
                meas_text = get_measurement_text(num_targets, t, job['targets'])

                if t in job['completed']:
                    if t != final_target:
                        # 測定済みは青。再押下すると未測定へ戻せることも明示する。
                        if st.button(
                            f"✅ {meas_text}　測定済み　｜　押すと取消",
                            key=f"undo_comp_{machine}_{t}",
                            use_container_width=True,
                        ):
                            if undo_mfr_measurement(machine, t):
                                save_state()
                                st.rerun()
                    else:
                        # 最終測定は生産終了確認と連動するため、
                        # 青の測定済み表示のみとし、ワンタッチ取消にはしない。
                        st.markdown(
                            f'<div class="mfr-measurement-done-static">'
                            f'✅ {meas_text}　測定済み</div>',
                            unsafe_allow_html=True,
                        )
                else:
                    # 未測定は黄橙。現在の状態と押すタイミングを明示する。
                    if st.button(
                        f"○ {meas_text}　未測定　｜　測定後に押す",
                        key=f"comp_{machine}_{t}",
                        use_container_width=True,
                    ):
                        complete_mfr_measurement(machine, t)
                        save_state()
                        st.rerun()

        machine_data[machine] = {'job': job, 'est_current': est_current}

# 下段パネル
cols_bottom = st.columns(3)
for idx, machine in enumerate(['100t', '450t', '550t']):
    with cols_bottom[idx]:
        st.divider() 
        job = machine_data[machine]['job']
        est_current = machine_data[machine]['est_current']
        
        with st.expander("🔧 生産数・サイクル補正", expanded=False):
            adjust_qty_value = est_current if job is not None else 0
            adjust_cycle_value = float(job['cycle_time']) if job is not None else 30.0
            
            st.markdown("**生産数の補正**")
            new_qty = st.number_input("現在の実際の個数", min_value=0, max_value=job['total_qty'] if job is not None else 999999, value=adjust_qty_value, step=1, key=f"adj_qty_{machine}")
            if st.button("💾 個数を上書き更新", key=f"update_qty_{machine}"):
                if job is not None:
                    job['current_qty'] = new_qty
                    job['last_update'] = (datetime.utcnow() + timedelta(hours=9))
                    save_state(); st.rerun()
                else:
                    st.warning("稼働していません。")
            
            st.markdown("---")
            
            st.markdown("**サイクルの補正**")
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

# --- UI：全体可視化グラフ ---
st.header("📈 稼働・MFRスケジュール")

timeline_data = []
measurement_points = []

for machine, job in st.session_state.jobs.items():
    if job is None: continue
    start_time = job['last_update']
    if job['status'] == 'Completed':
        end_time = job.get(
            'production_ended_at',
            datetime.utcnow() + timedelta(hours=9),
        )
    else:
        end_time = job['last_update'] + timedelta(
            seconds=(job['total_qty'] - job['current_qty']) * job['cycle_time']
        )
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
    timeline_data.append({'Task': 'MFR電源', 'Start': b_start, 'End': b_end, 'Status': 'ON'})

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
        color_discrete_map={'Running': '#2563eb', 'Paused': '#d97706', 'Completed': '#0891b2', 'ON': '#dc2626'},
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
    fig.add_vrect(x0=time_to_dummy(dt_time(15,0)), x1=time_to_dummy(dt_time(23,0)), fillcolor="#f3e8ff", opacity=0.4, layer="below", line_width=1, line_color="gray")
    fig.add_vrect(x0=time_to_dummy(dt_time(23,0)), x1=time_to_dummy(dt_time(23,59,59)), fillcolor="#e6f2ff", opacity=0.4, layer="below", line_width=1, line_color="gray")

    for facet_date in unique_dates:
        row_idx = date_to_row[facet_date]
        shifts_text = [
            ("C勤", time_to_dummy(dt_time(3, 30)), 'rgba(0,68,136,0.05)'),
            ("A勤", time_to_dummy(dt_time(11, 0)), 'rgba(136,102,0,0.05)'),
            ("B勤", time_to_dummy(dt_time(19, 0)), 'rgba(109,40,217,0.05)')
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
        fig.add_vline(x=now_dummy_time, line_width=3, line_dash="dash", line_color="#c81e1e", layer="above", row=today_row, col=1)
        yref_name = f"y{today_row if today_row > 1 else ''} domain"
        # 「▼」を現在時刻の点線の真上へ置き、
        # 「現在」は右側へ分けて表示する。
        fig.add_annotation(
            x=now_dummy_time,
            y=1.02,
            yref=yref_name,
            text="▼",
            font=dict(size=20, color="#c81e1e", weight="bold"),
            showarrow=False,
            xanchor="center",
            yanchor="bottom",
            bgcolor="white",
            bordercolor="#c81e1e",
            borderwidth=1,
            row=today_row,
            col=1,
        )
        fig.add_annotation(
            x=now_dummy_time,
            xshift=18,
            y=1.02,
            yref=yref_name,
            text="現在",
            font=dict(size=18, color="#c81e1e", weight="bold"),
            showarrow=False,
            xanchor="left",
            yanchor="bottom",
            bgcolor="white",
            bordercolor="#c81e1e",
            borderwidth=1,
            row=today_row,
            col=1,
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
                    marker=dict(color='#2563eb', size=18, symbol='circle', line=dict(width=3, color='black')),
                    text=trace_completed_text, textposition='top center', textfont=dict(size=18, color='black', weight='bold'),
                    cliponaxis=False, hoverinfo='skip', showlegend=False 
                ), row=row_idx, col=1)

            df_plan = df_pts_in_facet[df_pts_in_facet['Status'] == 'Planned']
            if not df_plan.empty:
                trace_planned_text = ['日常点検' if pt.get('Targets', []) and pt['Targets'][0] == '日常点検' else get_measurement_text(len(pt.get('Targets', [])), pt['Target_Qty'], pt.get('Targets', [])) for pt in df_plan.to_dict('records')]
                fig.add_trace(go.Scatter(
                    x=df_plan['TimeDummy'], y=df_plan['Task'], mode='markers+text',
                    marker=dict(color='#ffd43b', size=20, symbol='diamond', line=dict(width=3, color='black')),
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

            st.info(
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
                font=dict(size=22, color="#1d4ed8"),
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


# --- UI：Cost Saving 実績 ---
st.markdown("---")
st.header("💰 Cost Saving")
st.caption(
    "生産終了実績とMFR電源の実操作履歴から、電力・労務費・設備消耗の"
    "削減効果を日次／週次で自動集計します。"
)

cost_data = normalize_cost_saving_data(st.session_state.cost_saving_data)
st.session_state.cost_saving_data = cost_data
cost_settings = cost_data["settings"]
now_cost = datetime.utcnow() + timedelta(hours=9)
daily_effects, weekly_effects, power_off_intervals = build_cost_saving_summary(
    cost_data,
    now_cost,
)

current_week_key = _week_start(now_cost)
current_week = weekly_effects.get(current_week_key, {
    "saved_hours": 0.0,
    "saved_kwh": 0.0,
    "electricity_yen": 0.0,
    "labor_yen": 0.0,
    "maintenance_yen": 0.0,
    "lots": 0,
})

cumulative = {
    "saved_hours": 0.0,
    "saved_kwh": 0.0,
    "electricity_yen": 0.0,
    "labor_yen": 0.0,
    "maintenance_yen": 0.0,
    "lots": 0,
}
for effect in weekly_effects.values():
    for key in cumulative:
        cumulative[key] += effect.get(key, 0) or 0

st.markdown("#### 今週の効果（現在まで）")
week_cols = st.columns(5)
with week_cols[0]:
    st.metric(
        "合計効果",
        f"¥{effect_total_yen(current_week):,.0f}",
    )
with week_cols[1]:
    st.metric(
        "電気代削減",
        f"¥{current_week['electricity_yen']:,.0f}",
        f"{current_week['saved_kwh']:.1f} kWh",
    )
with week_cols[2]:
    st.metric(
        "労務費削減",
        f"¥{current_week['labor_yen']:,.0f}",
        f"{int(current_week['lots'])} Lot",
    )
with week_cols[3]:
    st.metric(
        "設備消耗低減",
        f"¥{current_week['maintenance_yen']:,.0f}",
    )
with week_cols[4]:
    st.metric(
        "削減通電時間",
        f"{current_week['saved_hours']:.1f} h",
    )

with st.expander("📈 累計効果", expanded=False):
    cumulative_cols = st.columns(5)
    with cumulative_cols[0]:
        st.metric("累計効果", f"¥{effect_total_yen(cumulative):,.0f}")
    with cumulative_cols[1]:
        st.metric(
            "累計電気代削減",
            f"¥{cumulative['electricity_yen']:,.0f}",
            f"{cumulative['saved_kwh']:.1f} kWh",
        )
    with cumulative_cols[2]:
        st.metric(
            "累計労務費削減",
            f"¥{cumulative['labor_yen']:,.0f}",
            f"{int(cumulative['lots'])} Lot",
        )
    with cumulative_cols[3]:
        st.metric(
            "累計設備消耗低減",
            f"¥{cumulative['maintenance_yen']:,.0f}",
        )
    with cumulative_cols[4]:
        st.metric(
            "累計削減通電時間",
            f"{cumulative['saved_hours']:.1f} h",
        )

cost_tab_week, cost_tab_day, cost_tab_history, cost_tab_settings = st.tabs([
    "📅 週次実績",
    "📆 日次実績",
    "🧾 生産・電源履歴",
    "⚙️ 計算条件",
])

with cost_tab_week:
    week_rows = []
    if weekly_effects:
        first_week = min(weekly_effects.keys())
        cursor_week = first_week
        while cursor_week <= current_week_key:
            effect = weekly_effects.get(cursor_week, {})
            week_end = cursor_week + timedelta(days=6)
            week_rows.append({
                "週": (
                    f"{cursor_week.strftime('%Y/%m/%d')}～"
                    f"{week_end.strftime('%m/%d')}"
                ),
                "Lot数": int(effect.get("lots", 0) or 0),
                "削減通電時間(h)": round(
                    float(effect.get("saved_hours", 0) or 0), 2
                ),
                "削減電力量(kWh)": round(
                    float(effect.get("saved_kwh", 0) or 0), 2
                ),
                "電気代削減(円)": round(
                    float(effect.get("electricity_yen", 0) or 0)
                ),
                "労務費削減(円)": round(
                    float(effect.get("labor_yen", 0) or 0)
                ),
                "設備消耗低減(円)": round(
                    float(effect.get("maintenance_yen", 0) or 0)
                ),
                "週間効果(円)": round(effect_total_yen(effect)),
            })
            cursor_week += timedelta(days=7)

    if week_rows:
        weekly_df = pd.DataFrame(week_rows).tail(52)
        running_total = weekly_df["週間効果(円)"].cumsum()
        # 表示範囲以前の実績がある場合も累計値がつながるよう補正。
        all_week_total = sum(
            round(effect_total_yen(effect))
            for effect in weekly_effects.values()
        )
        visible_total = int(weekly_df["週間効果(円)"].sum())
        carry = max(0, int(all_week_total) - visible_total)
        weekly_df["累計効果(円)"] = running_total + carry

        st.dataframe(
            weekly_df,
            use_container_width=True,
            hide_index=True,
        )
    else:
        weekly_df = pd.DataFrame()
        st.info(
            "まだCost Saving実績はありません。"
            "グラフには今週から6週間分の枠を表示しています。"
        )

    # ------------------------------------------------------------------
    # Cost Saving 週次グラフ
    # ・常に6週間を1画面へ固定表示する。
    # ・実績のない週も週枠と週ラベルを表示する。
    # ・電気代／労務費／設備消耗低減は一定幅の3本を横並び表示。
    # ・累計効果は実績が確定している現在週まで折れ線表示する。
    # ------------------------------------------------------------------
    actual_week_keys = sorted(
        week_key
        for week_key in weekly_effects.keys()
        if week_key <= current_week_key
    )

    # 活動開始直後は最初の実績週を左端にし、将来週を多めに見せる。
    # 3週以上経過後は「直近2週＋今週＋今後3週」の6週表示へ自動移行する。
    first_actual_week = (
        actual_week_keys[0]
        if actual_week_keys
        else current_week_key
    )
    chart_start_week = max(
        first_actual_week,
        current_week_key - timedelta(days=14),
    )
    chart_week_starts = [
        chart_start_week + timedelta(days=7 * index)
        for index in range(6)
    ]

    component_specs = [
        ("electricity_yen", "電気代削減", "#2563eb", "#1e3a8a"),
        ("labor_yen", "労務費削減", "#f59e0b", "#92400e"),
        ("maintenance_yen", "設備消耗低減", "#7c3aed", "#4c1d95"),
    ]

    chart_rows = []
    carry_before_chart = sum(
        round(effect_total_yen(effect))
        for week_key, effect in weekly_effects.items()
        if week_key < chart_start_week
    )
    running_chart_total = float(carry_before_chart)

    for index, week_start in enumerate(chart_week_starts):
        week_end = week_start + timedelta(days=6)
        effect = weekly_effects.get(week_start, {})
        week_total = float(round(effect_total_yen(effect)))

        # 未来週は予測値を描かず、累計線も現在週で止める。
        if week_start <= current_week_key:
            running_chart_total += week_total
            cumulative_value = running_chart_total
        else:
            cumulative_value = None

        chart_rows.append({
            "x": index,
            "week_start": week_start,
            "week_end": week_end,
            "tick": (
                f"{week_start.strftime('%m/%d')}<br>"
                f"～{week_end.strftime('%m/%d')}"
            ),
            "hover_week": (
                f"{week_start.strftime('%Y/%m/%d')}～"
                f"{week_end.strftime('%m/%d')}"
            ),
            "electricity_yen": float(
                effect.get("electricity_yen", 0) or 0
            ),
            "labor_yen": float(effect.get("labor_yen", 0) or 0),
            "maintenance_yen": float(
                effect.get("maintenance_yen", 0) or 0
            ),
            "week_total": week_total,
            "cumulative": cumulative_value,
        })

    chart_df = pd.DataFrame(chart_rows)
    fig_cost = make_subplots(specs=[[{"secondary_y": True}]])

    for value_key, trace_name, color, border_color in component_specs:
        fig_cost.add_trace(
            go.Bar(
                x=chart_df["x"],
                y=chart_df[value_key],
                name=trace_name,
                width=0.18,
                marker=dict(
                    color=color,
                    line=dict(color=border_color, width=1.2),
                ),
                customdata=chart_df["hover_week"],
                hovertemplate=(
                    "%{customdata}<br>"
                    + trace_name
                    + "：¥%{y:,.0f}<extra></extra>"
                ),
            ),
            secondary_y=False,
        )

    # 実績のある週だけ、その週の合計金額を3本の棒の上へ表示する。
    component_value_keys = [item[0] for item in component_specs]
    group_tops = chart_df[component_value_keys].max(axis=1).astype(float)
    group_text_y = group_tops.where(group_tops > 0, 0) * 1.12
    group_text = [
        f"合計 ¥{value:,.0f}" if value > 0 else ""
        for value in chart_df["week_total"]
    ]
    fig_cost.add_trace(
        go.Scatter(
            x=chart_df["x"],
            y=group_text_y,
            mode="text",
            text=group_text,
            textposition="top center",
            textfont=dict(size=12, color="#334155"),
            name="週間合計",
            showlegend=False,
            hoverinfo="skip",
            cliponaxis=False,
        ),
        secondary_y=False,
    )

    # 累計効果は将来週へ予測延長せず、現在週までの実績だけを結ぶ。
    fig_cost.add_trace(
        go.Scatter(
            x=chart_df["x"],
            y=chart_df["cumulative"],
            name="累計効果",
            mode="lines+markers",
            connectgaps=False,
            line=dict(color="#0f172a", width=4),
            marker=dict(
                size=9,
                color="#ffffff",
                line=dict(color="#0f172a", width=3),
            ),
            customdata=chart_df["hover_week"],
            hovertemplate=(
                "%{customdata}<br>累計効果：¥%{y:,.0f}<extra></extra>"
            ),
        ),
        secondary_y=True,
    )

    # 6週間それぞれに固定枠を描画する。
    # 実績ゼロの週でも枠が残るため、週の区切りが一目で分かる。
    for index in range(6):
        fig_cost.add_shape(
            type="rect",
            xref="x",
            yref="paper",
            x0=index - 0.46,
            x1=index + 0.46,
            y0=0,
            y1=1,
            line=dict(color="#cbd5e1", width=1.1),
            fillcolor=(
                "rgba(248,250,252,0.60)"
                if index % 2 == 0
                else "rgba(255,255,255,0.30)"
            ),
            layer="below",
        )

    left_axis_max = max(
        1.0,
        float(chart_df[component_value_keys].max(axis=1).max() or 0) * 1.35,
    )
    cumulative_values = [
        float(value)
        for value in chart_df["cumulative"].tolist()
        if value is not None and not pd.isna(value)
    ]
    right_axis_max = max(
        1.0,
        (max(cumulative_values) if cumulative_values else 0.0) * 1.20,
    )

    fig_cost.update_layout(
        title={
            "text": "週ごとのCost Saving効果（週別内訳・累計）",
            "x": 0.01,
            "xanchor": "left",
        },
        barmode="group",
        bargap=0.34,
        bargroupgap=0.08,
        hovermode="x unified",
        height=520,
        margin=dict(t=90, b=90, l=70, r=85),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
        ),
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        font=dict(size=13, color="#1f2937"),
    )
    fig_cost.update_xaxes(
        title_text="週",
        type="linear",
        range=[-0.55, 5.55],
        tickmode="array",
        tickvals=list(range(6)),
        ticktext=chart_df["tick"].tolist(),
        showgrid=False,
        zeroline=False,
        tickangle=0,
        fixedrange=False,
    )
    fig_cost.update_yaxes(
        title_text="週間効果（円）",
        secondary_y=False,
        gridcolor="#e5e7eb",
        range=[0, left_axis_max],
        zeroline=True,
        zerolinecolor="#94a3b8",
    )
    fig_cost.update_yaxes(
        title_text="累計効果（円）",
        secondary_y=True,
        showgrid=False,
        range=[0, right_axis_max],
        zeroline=False,
    )
    st.plotly_chart(fig_cost, use_container_width=True)

    if not weekly_df.empty:
        weekly_csv = weekly_df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "⬇️ 週次実績CSVをダウンロード",
            data=weekly_csv,
            file_name="MFR_Cost_Saving_週次実績.csv",
            mime="text/csv",
        )

with cost_tab_day:
    day_rows = []
    for day_key in sorted(daily_effects.keys()):
        effect = daily_effects[day_key]
        day_rows.append({
            "日付": day_key.strftime("%Y/%m/%d"),
            "Lot数": int(effect.get("lots", 0) or 0),
            "削減通電時間(h)": round(
                float(effect.get("saved_hours", 0) or 0), 2
            ),
            "削減電力量(kWh)": round(
                float(effect.get("saved_kwh", 0) or 0), 2
            ),
            "電気代削減(円)": round(
                float(effect.get("electricity_yen", 0) or 0)
            ),
            "労務費削減(円)": round(
                float(effect.get("labor_yen", 0) or 0)
            ),
            "設備消耗低減(円)": round(
                float(effect.get("maintenance_yen", 0) or 0)
            ),
            "日次効果(円)": round(effect_total_yen(effect)),
        })

    if day_rows:
        daily_df = pd.DataFrame(day_rows).tail(60)
        st.dataframe(
            daily_df,
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("まだ日次実績はありません。")

with cost_tab_history:
    production_rows = []
    sorted_production = sorted(
        cost_data["production_history"],
        key=lambda record: str(record.get("ended_at", "")),
        reverse=True,
    )
    for record in sorted_production:
        started_at = parse_history_datetime(record.get("started_at"))
        ended_at = parse_history_datetime(record.get("ended_at"))
        measurement_texts = []
        for measurement in record.get("measurement_records", []):
            if not isinstance(measurement, dict):
                continue
            measured_at = parse_history_datetime(measurement.get("measured_at"))
            if measured_at is not None:
                measurement_texts.append(
                    f"{measurement.get('label', '')} {measured_at.strftime('%H:%M')}"
                )

        production_rows.append({
            "終了日": ended_at.strftime("%Y/%m/%d") if ended_at else "",
            "成型機": record.get("machine", ""),
            "製品": record.get("product_name", ""),
            "生産数": record.get("final_qty", 0),
            "開始": started_at.strftime("%m/%d %H:%M") if started_at else "",
            "終了": ended_at.strftime("%m/%d %H:%M") if ended_at else "",
            "MFR測定": " / ".join(measurement_texts),
            "測定回数": (
                f"{record.get('measurement_completed_count', 0)}/"
                f"{record.get('measurement_count', 0)}"
            ),
            "労務費削減(円)": round(
                float(record.get("labor_saving_yen", 0) or 0)
            ),
        })

    st.markdown("##### 生産履歴")
    if production_rows:
        production_df = pd.DataFrame(production_rows)
        st.dataframe(
            production_df,
            use_container_width=True,
            hide_index=True,
        )
        production_csv = production_df.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "⬇️ 生産履歴CSVをダウンロード",
            data=production_csv,
            file_name="MFR_Cost_Saving_生産履歴.csv",
            mime="text/csv",
        )
    else:
        st.info("まだ生産終了履歴はありません。")

    st.markdown("##### MFR電源実績")
    power_rows = []
    excluded_week_keys = set(cost_data.get("excluded_weeks", []))
    for event in sorted(
        cost_data["power_events"],
        key=lambda item: str(item.get("actual_at", "")),
        reverse=True,
    ):
        actual_at = parse_history_datetime(event.get("actual_at"))
        scheduled_at = parse_history_datetime(event.get("scheduled_at"))
        if (
            actual_at is not None
            and _week_start(actual_at).strftime("%Y-%m-%d") in excluded_week_keys
        ):
            continue
        power_rows.append({
            "実績日時": actual_at.strftime("%Y/%m/%d %H:%M") if actual_at else "",
            "操作": event.get("action", ""),
            "予定日時": scheduled_at.strftime("%Y/%m/%d %H:%M") if scheduled_at else "",
        })

    if power_rows:
        st.dataframe(
            pd.DataFrame(power_rows),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("まだMFR電源ON/OFF実績はありません。")

    st.markdown("---")
    st.markdown("##### 🗑️ Cost Saving履歴の削除")
    st.caption(
        "削除後は日次・週次・累計・グラフを自動再計算し、クラウドにも反映します。"
        "計算条件は削除されません。"
    )

    delete_feedback = st.session_state.pop("cost_delete_feedback", None)
    if delete_feedback:
        feedback_kind = delete_feedback.get("kind", "success")
        feedback_text = delete_feedback.get("text", "")
        if feedback_kind == "warning":
            st.warning(feedback_text)
        elif feedback_kind == "info":
            st.info(feedback_text)
        else:
            st.success(feedback_text)

    delete_mode = st.radio(
        "削除方法",
        ["個別削除", "週ごと全削除", "全削除"],
        horizontal=True,
        key="cost_delete_mode",
    )

    if delete_mode == "個別削除":
        current_records = sorted(
            cost_data["production_history"],
            key=lambda record: str(record.get("ended_at", "")),
            reverse=True,
        )
        if current_records:
            record_map = {
                str(record.get("job_id", "")): record
                for record in current_records
                if record.get("job_id")
            }
            selected_job_id = st.selectbox(
                "削除する生産履歴",
                options=list(record_map.keys()),
                format_func=lambda job_id: (
                    f"{(parse_history_datetime(record_map[job_id].get('ended_at')) or now_cost).strftime('%Y/%m/%d %H:%M')} ｜ "
                    f"{record_map[job_id].get('machine', '')} ｜ "
                    f"{record_map[job_id].get('product_name', '')} ｜ "
                    f"{record_map[job_id].get('final_qty', 0)}個"
                ),
                key="cost_delete_job_select",
            )
            confirm_one = st.checkbox(
                "選択した生産履歴1件を削除することを確認しました",
                key="cost_delete_one_confirm",
            )
            if st.button(
                "🗑️ 選択した1件を削除",
                disabled=not confirm_one,
                use_container_width=True,
                key="cost_delete_one_button",
            ):
                if delete_cost_saving_production_record(selected_job_id):
                    cloud_saved = save_cost_saving_history_change()
                    if GITHUB_TOKEN and not cloud_saved:
                        st.warning(
                            "ローカルでは削除しましたが、クラウド同期に失敗しました。"
                            "通信状態を確認して再度同期してください。"
                        )
                    else:
                        st.success("選択した生産履歴を削除しました。集計を再計算します。")
                    st.rerun()
        else:
            st.info("個別削除できる生産履歴はありません。")

    elif delete_mode == "週ごと全削除":
        history_weeks = get_cost_saving_history_weeks(cost_data)
        if history_weeks:
            week_map = {
                week.strftime("%Y-%m-%d"): week
                for week in history_weeks
            }
            selected_week_key = st.selectbox(
                "削除する週",
                options=list(week_map.keys()),
                format_func=lambda key: format_cost_saving_week_label(week_map[key]),
                key="cost_delete_week_select",
            )
            st.warning(
                "選択した週の生産履歴と、その週のCost Saving効果をすべて削除します。"
                "MFR電源ON/OFFの内部時系列は、前後週の計算を壊さないため保持しますが、"
                "選択週の表示・集計からは除外されます。"
            )
            confirm_week = st.checkbox(
                "選択した週をすべて削除することを確認しました",
                key="cost_delete_week_confirm",
            )
            if st.button(
                "🗑️ 選択した週を全削除",
                disabled=not confirm_week,
                use_container_width=True,
                key="cost_delete_week_button",
            ):
                if delete_cost_saving_week(week_map[selected_week_key]):
                    cloud_saved = save_cost_saving_history_change()
                    if GITHUB_TOKEN and not cloud_saved:
                        st.warning(
                            "ローカルでは週削除しましたが、クラウド同期に失敗しました。"
                        )
                    else:
                        st.success("選択した週を削除しました。集計を再計算します。")
                    st.rerun()
        else:
            st.info("週単位で削除できる実績はありません。")

    else:
        st.error(
            "Cost Savingの生産履歴・MFR電源実績をすべて削除します。"
            "この操作は元に戻せません。計算条件のみ残ります。"
        )
        confirm_all_1 = st.checkbox(
            "全履歴を削除することを理解しました",
            key="cost_delete_all_confirm_1",
        )
        confirm_all_2 = st.checkbox(
            "本当にすべて削除します",
            key="cost_delete_all_confirm_2",
        )

        def handle_delete_all_cost_saving():
            """全削除を実行し、削除後は確認UIを通常状態へ戻す。"""
            if not (
                st.session_state.get("cost_delete_all_confirm_1", False)
                and st.session_state.get("cost_delete_all_confirm_2", False)
            ):
                return

            if delete_all_cost_saving_history():
                cloud_saved = save_cost_saving_history_change()
                if GITHUB_TOKEN and not cloud_saved:
                    st.session_state.cost_delete_feedback = {
                        "kind": "warning",
                        "text": (
                            "ローカルではCost Saving履歴をすべて削除しましたが、"
                            "クラウド同期に失敗しました。"
                        ),
                    }
                else:
                    st.session_state.cost_delete_feedback = {
                        "kind": "success",
                        "text": "✅ Cost Saving履歴をすべて削除しました。",
                    }
            else:
                st.session_state.cost_delete_feedback = {
                    "kind": "info",
                    "text": "削除対象の履歴はありません。",
                }

            # 次の描画では通常の「個別削除」状態へ戻し、
            # 全削除の赤い確認UI・チェック状態を残さない。
            st.session_state.cost_delete_mode = "個別削除"
            st.session_state.cost_delete_all_confirm_1 = False
            st.session_state.cost_delete_all_confirm_2 = False

        st.button(
            "🗑️ Cost Saving履歴をすべて削除",
            type="primary",
            disabled=not (confirm_all_1 and confirm_all_2),
            use_container_width=True,
            key="cost_delete_all_button",
            on_click=handle_delete_all_cost_saving,
        )

with cost_tab_settings:
    st.write(
        "この条件はCost Saving実績の計算に使用し、クラウドへ保存します。"
        "修繕費または周期を0にすると設備消耗低減額は0円として扱います。"
    )

    with st.form("cost_saving_settings_form"):
        set_col1, set_col2, set_col3 = st.columns(3)
        with set_col1:
            cs_power_kw = st.number_input(
                "MFR消費電力 (kW)",
                min_value=0.0,
                value=float(cost_settings.get("power_kw", 0.80)),
                step=0.10,
                format="%.2f",
                key="cs_power_kw_input",
            )
            cs_electricity_price = st.number_input(
                "電気代単価 (円/kWh)",
                min_value=0.0,
                value=float(cost_settings.get("electricity_price", 25.0)),
                step=1.0,
                format="%.2f",
                key="cs_electricity_price_input",
            )
        with set_col2:
            cs_labor_rate = st.number_input(
                "1時間当たり労務費 (円/h)",
                min_value=0.0,
                value=float(cost_settings.get("labor_hourly_rate", 4600.0)),
                step=100.0,
                key="cs_labor_rate_input",
            )
            cs_manual_minutes = st.number_input(
                "システムなし管理時間 (分/Lot)",
                min_value=0.0,
                value=float(cost_settings.get("manual_minutes_per_lot", 5.0)),
                step=0.5,
                format="%.1f",
                key="cs_manual_minutes_input",
            )
        with set_col3:
            cs_maintenance_cost = st.number_input(
                "修繕・メンテナンス費用 (円)",
                min_value=0.0,
                value=float(cost_settings.get("maintenance_cost", 0.0)),
                step=10000.0,
                key="cs_maintenance_cost_input",
            )
            cs_maintenance_life = st.number_input(
                "メンテナンス周期 (時間)",
                min_value=0.0,
                value=float(cost_settings.get("maintenance_life_hours", 0.0)),
                step=1000.0,
                key="cs_maintenance_life_input",
            )

        if st.form_submit_button(
            "💾 計算条件を保存（クラウド同期）",
            use_container_width=True,
        ):
            st.session_state.cost_saving_data["settings"] = {
                "power_kw": float(cs_power_kw),
                "electricity_price": float(cs_electricity_price),
                "labor_hourly_rate": float(cs_labor_rate),
                "manual_minutes_per_lot": float(cs_manual_minutes),
                "maintenance_cost": float(cs_maintenance_cost),
                "maintenance_life_hours": float(cs_maintenance_life),
            }
            save_state()
            cloud_saved = sync_cost_saving_to_github()
            save_state()
            if GITHUB_TOKEN and cloud_saved:
                st.success("Cost Saving計算条件をクラウドへ保存しました。")
            elif GITHUB_TOKEN:
                st.warning(
                    "ローカルには保存しましたが、クラウド同期に失敗しました。"
                )
            else:
                st.info("ローカルへ保存しました。")
            st.rerun()

    if power_off_intervals and power_off_intervals[-1].get("open"):
        st.caption(
            "※現在MFR電源がOFF中の場合、OFF確認時刻から現在までの時間を"
            "今週の削減効果へ暫定加算しています。"
        )

    if GITHUB_TOKEN:
        st.caption(
            f"クラウド保存先：{COST_SAVING_FILE}"
        )
    else:
        st.caption(
            "GitHubトークンが設定されていないため、現在はローカル保存です。"
        )

