#!/usr/bin/env python3
"""鍒涘缓浼氳瘽 / 鍚戜細璇濆彂閫佹秷鎭紙鐢熷浘銆佺敓瑙嗛绛夛級锛歅OST /openapi/session"""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from _common import create_session, build_project_url


def main():
    parser = argparse.ArgumentParser(
        description="鍒涘缓浼氳瘽鎴栧悜宸叉湁浼氳瘽鍙戦€佹秷鎭紙鐢ㄤ簬鐢熷浘銆佺敓瑙嗛锛?,
        epilog="""
鐜鍙橀噺:
  LIBTV_ACCESS_KEY  蹇呭～锛孊earer 閴存潈
  OPENAPI_IM_BASE 鎴?IM_BASE_URL  鍙€夛紝榛樿 https://im.liblib.tv

绀轰緥:
  # 鍒涘缓鏂颁細璇濆苟鍙戦€併€岀敓涓€涓姩婕棰戙€?  python3 create_session.py "鐢熶竴涓姩婕棰?

  # 鍚戝凡鏈変細璇濆彂閫佹秷鎭?  python3 create_session.py "鍐嶇敓鎴愪竴寮犻鏅浘" --session-id 90f05e0c-5d08-4148-be40-e30fc7c7bedf

  # 鍙垱寤?缁戝畾浼氳瘽锛屼笉鍙戞秷鎭?  python3 create_session.py
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "message",
        nargs="?",
        default="",
        help="瑕佸彂閫佺殑娑堟伅鍐呭锛堢敓鍥?鐢熻棰戞弿杩扮瓑锛夛紝涓嶄紶鍒欎笉璋冪敤 SendMessage",
    )
    parser.add_argument(
        "--session-id",
        default="",
        help="宸叉湁浼氳瘽 ID锛屼笉浼犲垯鍒涘缓鏂颁細璇濇垨杩斿洖宸叉湁榛樿浼氳瘽",
    )
    args = parser.parse_args()

    data = create_session(session_id=args.session_id or "", message=args.message or "")
    project_uuid = data.get("projectUuid", "")
    session_id = data.get("sessionId", "")

    if not session_id:
        print("閿欒锛氭湭杩斿洖 sessionId", file=sys.stderr)
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
