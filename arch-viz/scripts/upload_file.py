#!/usr/bin/env python3
"""Upload image/video to OSS: POST /openapi/upload (multipart/form-data)"""

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

# Allowed MIME type prefixes
ALLOWED_PREFIXES = ("image/", "video/")


def upload_file(file_path: str) -> dict:
    """
    Upload local file to agent-im OSS.
    Returns data: { url }.
    """
    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    # Check MIME type
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type and not any(mime_type.startswith(p) for p in ALLOWED_PREFIXES):
        print(f"Error: Unsupported file type: {mime_type}, only image and video supported", file=sys.stderr)
        sys.exit(1)

    # Build multipart/form-data request
    boundary = f"----PythonUpload{uuid.uuid4().hex}"
    filename = os.path.basename(file_path)

    body_parts = []

    # accessKey field
    body_parts.append(f"--{boundary}\r\n".encode())
    body_parts.append(b'Content-Disposition: form-data; name="accessKey"\r\n\r\n')
    body_parts.append(f"{ACCESS_KEY}\r\n".encode())

    # file field
    content_type = mime_type or "application/octet-stream"
    body_parts.append(f"--{boundary}\r\n".encode())
    body_parts.append(
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'.encode()
    )
    body_parts.append(f"Content-Type: {content_type}\r\n\r\n".encode())
    with open(file_path, "rb") as f:
        body_parts.append(f.read())
    body_parts.append(b"\r\n")

    # End boundary
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
        print(f"API Error {e.code}: {err_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Upload image or video file to OSS",
        epilog="""
Environment Variables:
  LIBTV_ACCESS_KEY  Required, Bearer Auth
  OPENAPI_IM_BASE or IM_BASE_URL  Optional, default https://im.liblib.tv

Examples:
  # Upload image
  python3 upload_file.py /path/to/image.png

  # Upload video
  python3 upload_file.py /path/to/video.mp4
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "file",
        help="Path to image or video file to upload",
    )
    args = parser.parse_args()

    data = upload_file(args.file)
    oss_url = data.get("url", "")

    if not oss_url:
        print("Error: No OSS URL returned", file=sys.stderr)
        sys.exit(1)

    out = {"url": oss_url}
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
