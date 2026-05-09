"""agent-im OpenAPI 鍏叡妯″潡锛氬垱寤轰細璇濄€佹煡璇細璇濓紙閴存潈涓?Authorization: Bearer <access_key>锛?""

import json
import os
import sys
import urllib.request
import urllib.error

# 榛樿 im 鐜
IM_BASE = os.environ.get("OPENAPI_IM_BASE", os.environ.get("IM_BASE_URL", "https://im.liblib.tv"))
ACCESS_KEY = os.environ.get("LIBTV_ACCESS_KEY", "")

# 椤圭洰鐢诲竷鍦板潃鍓嶇紑锛屾嫾涓?projectId 鍗抽」鐩湴鍧€
PROJECT_CANVAS_BASE = "https://www.liblib.tv/canvas?projectId="


def build_project_url(project_id: str) -> str:
    """鏍规嵁 projectId锛堝嵆 projectUuid锛夋嫾鎺ラ」鐩敾甯冨湴鍧€"""
    if not project_id:
        return ""
    return PROJECT_CANVAS_BASE + project_id.strip()

if not ACCESS_KEY:
    print("閿欒锛氳璁剧疆 LIBTV_ACCESS_KEY 鐜鍙橀噺", file=sys.stderr)
    sys.exit(1)


def _headers():
    return {
        "Authorization": f"Bearer {ACCESS_KEY}",
        "Content-Type": "application/json",
    }


def api_post(path: str, body: dict) -> dict:
    """POST 璇锋眰 agent-im OpenAPI"""
    url = f"{IM_BASE.rstrip('/')}{path}"
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers=_headers(),
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8") if e.fp else ""
        print(f"API 閿欒 {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"缃戠粶閿欒: {e.reason}", file=sys.stderr)
        sys.exit(1)


def api_get(path: str) -> dict:
    """GET 璇锋眰 agent-im OpenAPI"""
    url = f"{IM_BASE.rstrip('/')}{path}"
    req = urllib.request.Request(url, method="GET", headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8") if e.fp else ""
        print(f"API 閿欒 {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"缃戠粶閿欒: {e.reason}", file=sys.stderr)
        sys.exit(1)


def create_session(session_id: str = "", message: str = "") -> dict:
    """
    鍒涘缓浼氳瘽鎴栧悜宸叉湁浼氳瘽鍙戞秷鎭€?    杩斿洖 data: { projectUuid, sessionId }銆?    """
    body = {}
    if session_id:
        body["sessionId"] = session_id
    if message:
        body["message"] = message
    resp = api_post("/openapi/session", body)
    return resp.get("data", {})


def query_session(session_id: str, after_seq: int = 0) -> dict:
    """
    鏌ヨ浼氳瘽娑堟伅鍒楄〃銆?    杩斿洖 data: { messages: [...] }銆?    """
    path = f"/openapi/session/{session_id}"
    if after_seq > 0:
        path += f"?afterSeq={after_seq}"
    resp = api_get(path)
    return resp.get("data", {})


def change_project() -> dict:
    """
    鍒囨崲褰撳墠 accessKey 缁戝畾鐨勯」鐩紙璋冪敤 libtv 鍒囨崲椤圭洰锛屽悗缁?create_session 灏嗕娇鐢ㄦ柊椤圭洰锛夈€?    杩斿洖 data: { projectUuid }銆?    """
    resp = api_post("/openapi/session/change-project", {})
    return resp.get("data", {})
