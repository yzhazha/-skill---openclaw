#!/usr/bin/env python3
"""鍒囨崲褰撳墠 accessKey 缁戝畾鐨勯」鐩細POST /openapi/session/change-project"""

import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from _common import change_project, build_project_url


def main():
    data = change_project()
    project_uuid = data.get("projectUuid", "")

    if not project_uuid:
        print("閿欒锛氭湭杩斿洖 projectUuid", file=sys.stderr)
        sys.exit(1)

    project_url = build_project_url(project_uuid)
    out = {
        "projectUuid": project_uuid,
        "projectUrl": project_url,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
