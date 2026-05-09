#!/usr/bin/env python3
"""Query session progress: GET /openapi/session/:sessionId, returns message list"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from _common import query_session, build_project_url


def main():
    parser = argparse.ArgumentParser(
        description="Query session message list (session progress)",
        epilog="""
Environment Variables:
  LIBTV_ACCESS_KEY  Required, Bearer Auth
  OPENAPI_IM_BASE or IM_BASE_URL  Optional, default https://im.liblib.tv

Examples:
  python3 query_session.py 90f05e0c-5d08-4148-be40-e30fc7c7bedf
  python3 query_session.py 90f05e0c-5d08-4148-be40-e30fc7c7bedf --after-seq 5
  python3 query_session.py SESSION_ID --project-id PROJECT_UUID   # Results include projectUrl
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("session_id", help="Session ID (from create_session)")
    parser.add_argument(
        "--after-seq",
        type=int,
        default=0,
        help="Only return messages with seq greater than this value (for incremental fetch, default 0)",
    )
    parser.add_argument(
        "--project-id",
        default="",
        help="Project ID (projectUuid from create_session), results will include projectUrl",
    )
    args = parser.parse_args()

    data = query_session(args.session_id, after_seq=args.after_seq)
    messages = data.get("messages", [])

    out = {"messages": messages}
    if args.project_id:
        out["projectUrl"] = build_project_url(args.project_id)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
