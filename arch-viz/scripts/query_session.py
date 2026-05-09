#!/usr/bin/env python3
"""鏌ヨ浼氳瘽杩涘睍锛欸ET /openapi/session/:sessionId锛岃繑鍥炴秷鎭垪琛?""

import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from _common import query_session, build_project_url


def main():
    parser = argparse.ArgumentParser(
        description="鏌ヨ浼氳瘽娑堟伅鍒楄〃锛堜細璇濊繘灞曪級",
        epilog="""
鐜鍙橀噺:
  LIBTV_ACCESS_KEY  蹇呭～锛孊earer 閴存潈
  OPENAPI_IM_BASE 鎴?IM_BASE_URL  鍙€夛紝榛樿 https://im.liblib.tv

绀轰緥:
  python3 query_session.py 90f05e0c-5d08-4148-be40-e30fc7c7bedf
  python3 query_session.py 90f05e0c-5d08-4148-be40-e30fc7c7bedf --after-seq 5
  python3 query_session.py SESSION_ID --project-id PROJECT_UUID   # 缁撴灉涓檮甯?projectUrl
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("session_id", help="浼氳瘽 ID锛堢敱 create_session 杩斿洖锛?)
    parser.add_argument(
        "--after-seq",
        type=int,
        default=0,
        help="鍙繑鍥?seq 澶т簬璇ュ€肩殑娑堟伅锛岀敤浜庡閲忔媺鍙栵紙榛樿 0锛?,
    )
    parser.add_argument(
        "--project-id",
        default="",
        help="椤圭洰 ID锛堝嵆 create_session 杩斿洖鐨?projectUuid锛夛紝浼犲叆鍒欑粨鏋滀腑闄勫甫 projectUrl 渚夸簬灞曠ず",
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
