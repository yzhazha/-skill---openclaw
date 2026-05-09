"""agent-im OpenAPI Common Module: Create session, query session (Auth: Bearer <access_key>)"""

import json
import os
import sys
import urllib.request
import urllib.error

# Default IM environment
IM_BASE = os.environ.get("OPENAPI_IM_BASE", os.environ.get("IM_BASE_URL", "https://im.liblib.tv"))
ACCESS_KEY = os.environ.get("LIBTV_ACCESS_KEY", "")

# Project canvas URL prefix
PROJECT_CANVAS_BASE = "https://www.liblib.tv/canvas?projectId="


def build_project_url(project_id: str) -> str:
    """Build project URL from projectId"""
    if not project_id:
        return ""
    return PROJECT_CANVAS_BASE + project_id.strip()

if not ACCESS_KEY:
    print("Error: Please set LIBTV_ACCESS_KEY environment variable", file=sys.stderr)
    sys.exit(1)


def _headers():
    return {
        "Authorization": f"Bearer {ACCESS_KEY}",
        "Content-Type": "application/json",
    }


def api_post(path: str, body: dict) -> dict:
    """POST request to agent-im OpenAPI"""
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
        print(f"API Error {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def api_get(path: str) -> dict:
    """GET request to agent-im OpenAPI"""
    url = f"{IM_BASE.rstrip('/')}{path}"
    req = urllib.request.Request(url, method="GET", headers=_headers())
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8") if e.fp else ""
        print(f"API Error {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def create_session(session_id: str = "", message: str = "") -> dict:
    """
    Create session or send message to existing session.
    Returns data: { projectUuid, sessionId }.
    """
    body = {}
    if session_id:
        body["sessionId"] = session_id
    if message:
        body["message"] = message
    resp = api_post("/openapi/session", body)
    return resp.get("data", {})


def query_session(session_id: str, after_seq: int = 0) -> dict:
    """
    Query session message list.
    Returns data: { messages: [...] }.
    """
    path = f"/openapi/session/{session_id}"
    if after_seq > 0:
        path += f"?afterSeq={after_seq}"
    resp = api_get(path)
    return resp.get("data", {})


def change_project() -> dict:
    """
    Switch project bound to current accessKey.
    Returns data: { projectUuid }.
    """
    resp = api_post("/openapi/session/change-project", {})
    return resp.get("data", {})
