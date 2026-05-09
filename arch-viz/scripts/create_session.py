#!/usr/bin/env python3
"""Create session / Send message to session: POST /openapi/session"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from _common import create_session, build_project_url


def main():
    parser = argparse.ArgumentParser(
        description="Create session or send message to existing session (for image/video generation)",
        epilog="""
Environment Variables:
  LIBTV_ACCESS_KEY  Required, Bearer Auth
  OPENAPI_IM_BASE or IM_BASE_URL  Optional, default https://im.liblib.tv

Examples:
  # Create new session and send "generate anime video"
  python3 create_session.py "generate anime video"

  # Send message to existing session
  python3 create_session.py "generate landscape image" --session-id 90f05e0c-5d08-4148-be40-e30fc7c7bedf

  # Create/bind session only, no message
  python3 create_session.py
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "message",
        nargs="?",
        default="",
        help="Message content to send (image/video generation description), empty to skip SendMessage",
    )
    parser.add_argument(
        "--session-id",
        default="",
        help="Existing session ID, omit to create new session",
    )
    args = parser.parse_args()

    data = create_session(session_id=args.session_id or "", message=args.message or "")
    project_uuid = data.get("projectUuid", "")
    session_id = data.get("sessionId", "")

    if not session_id:
        print("Error: No sessionId returned", file=sys.stderr)
        sys.exit(1)

    project_url = build_project_url(project_uuid)
    out = {
        "projectUuid": project_uuid,
        "sessionId": session_id,
        "projectUrl": project_url,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
