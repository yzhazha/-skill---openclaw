#!/usr/bin/env python3
"""涓婁紶鍥剧墖/瑙嗛鍒?OSS锛歅OST /openapi/upload锛坢ultipart/form-data锛?""

import argparse
import json
import mimetypes
import os
import sys
import uuid
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(__file__))
from _common import IM_BASE, ACCESS_KEY

# 鍏佽鐨?MIME 绫诲瀷鍓嶇紑
ALLOWED_PREFIXES = ("image/", "video/")


def upload_file(file_path: str) -> dict:
    """
    涓婁紶鏈湴鏂囦欢鍒?agent-im OSS銆?    杩斿洖 data: { url }銆?    """
    if not os.path.isfile(file_path):
        print(f"閿欒锛氭枃浠朵笉瀛樺湪: {file_path}", file=sys.stderr)
        sys.exit(1)

    # 妫€鏌?MIME 绫诲瀷
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type and not any(mime_type.startswith(p) for p in ALLOWED_PREFIXES):
        print(f"閿欒锛氫笉鏀寔鐨勬枃浠剁被鍨? {mime_type}锛屼粎鏀寔鍥剧墖鍜岃棰?, file=sys.stderr)
        sys.exit(1)

    # 鏋勫缓 multipart/form-data 璇锋眰浣?    boundary = f"----PythonUpload{uuid.uuid4().hex}"
    filename = os.path.basename(file_path)

    body_parts = []

    # accessKey 瀛楁
    body_parts.append(f"--{boundary}\r\n".encode())
    body_parts.append(b'Content-Disposition: form-data; name="accessKey"\r\n\r\n')
    body_parts.append(f"{ACCESS_KEY}\r\n".encode())

    # file 瀛楁
    content_type = mime_type or "application/octet-stream"
    body_parts.append(f"--{boundary}\r\n".encode())
    body_parts.append(
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'.encode()
    )
    body_parts.append(f"Content-Type: {content_type}\r\n\r\n".encode())
    with open(file_path, "rb") as f:
        body_parts.append(f.read())
    body_parts.append(b"\r\n")

    # 缁撴潫杈圭晫
    body_parts.append(f"--{boundary}--\r\n".encode())

    data = b"".join(body_parts)

    url = f"{IM_BASE.rstrip('/')}/openapi/upload"
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {ACCESS_KEY}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            return result.get("data", {})
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8") if e.fp else ""
        print(f"API 閿欒 {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"缃戠粶閿欒: {e.reason}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="涓婁紶鍥剧墖鎴栬棰戞枃浠跺埌 OSS",
        epilog="""
鐜鍙橀噺:
  LIBTV_ACCESS_KEY  蹇呭～锛孊earer 閴存潈
  OPENAPI_IM_BASE 鎴?IM_BASE_URL  鍙€夛紝榛樿 https://im.liblib.tv

绀轰緥:
  # 涓婁紶鍥剧墖
  python3 upload_file.py /path/to/image.png

  # 涓婁紶瑙嗛
  python3 upload_file.py /path/to/video.mp4
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "file",
        help="瑕佷笂浼犵殑鍥剧墖鎴栬棰戞枃浠惰矾寰?,
    )
    args = parser.parse_args()

    data = upload_file(args.file)
    oss_url = data.get("url", "")

    if not oss_url:
        print("閿欒锛氭湭杩斿洖 OSS 鍦板潃", file=sys.stderr)
        sys.exit(1)

    out = {"url": oss_url}
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
