#!/usr/bin/env python3
"""涓嬭浇鐢熸垚缁撴灉锛氫粠浼氳瘽涓彁鍙栨墍鏈夊浘鐗?瑙嗛 URL 骞舵壒閲忎笅杞藉埌鏈湴"""

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(__file__))
from _common import query_session


def extract_urls_from_messages(messages):
    """浠庝細璇濇秷鎭腑鎻愬彇鎵€鏈夊浘鐗囧拰瑙嗛缁撴灉 URL"""
    urls = []
    url_pattern = re.compile(r'https://libtv-res\.liblib\.art/[^\s"\'<>]+\.(?:png|jpg|jpeg|webp|mp4|mov|webm)')

    for msg in messages:
        content = msg.get("content", "")
        if not content or not isinstance(content, str):
            continue

        # 浠?task_result 涓彁鍙栵紙toolmsg 杩斿洖鐨勭粨鏋滐級
        if msg.get("role") == "tool":
            try:
                data = json.loads(content)
                task_result = data.get("task_result", {})
                for img in task_result.get("images", []):
                    preview = img.get("previewPath", "")
                    if preview:
                        urls.append(preview)
                for vid in task_result.get("videos", []):
                    preview = vid.get("previewPath", vid.get("url", ""))
                    if preview:
                        urls.append(preview)
            except (json.JSONDecodeError, AttributeError):
                pass

        # 浠?assistant 鏂囨湰娑堟伅涓彁鍙?URL
        if msg.get("role") == "assistant":
            found = url_pattern.findall(content)
            urls.extend(found)

    # 鍘婚噸淇濆簭
    seen = set()
    unique = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique.append(u)
    return unique


def download_file(url, filepath):
    """涓嬭浇鍗曚釜鏂囦欢"""
    req = urllib.request.Request(url, headers={"User-Agent": "LibTV-Skill/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            with open(filepath, "wb") as f:
                while True:
                    chunk = resp.read(8192)
                    if not chunk:
                        break
                    f.write(chunk)
        return filepath, None
    except Exception as e:
        return filepath, str(e)


def main():
    parser = argparse.ArgumentParser(
        description="涓嬭浇浼氳瘽涓敓鎴愮殑鍥剧墖/瑙嗛鍒版湰鍦?,
        epilog="""
浣跨敤鏂瑰紡:
  # 浠庝細璇濊嚜鍔ㄦ彁鍙栧苟涓嬭浇鎵€鏈夌粨鏋?  python3 download_results.py SESSION_ID

  # 鎸囧畾杈撳嚭鐩綍
  python3 download_results.py SESSION_ID --output-dir ~/Desktop/my_project

  # 鎸囧畾鏂囦欢鍚嶅墠缂€
  python3 download_results.py SESSION_ID --prefix "storyboard"

  # 鐩存帴涓嬭浇鎸囧畾 URL 鍒楄〃
  python3 download_results.py --urls URL1 URL2 URL3 --output-dir ./output
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("session_id", nargs="?", default="", help="浼氳瘽 ID锛岃嚜鍔ㄦ彁鍙栬浼氳瘽鎵€鏈夌敓鎴愮粨鏋滅殑 URL")
    parser.add_argument("--urls", nargs="+", default=[], help="鐩存帴鎸囧畾瑕佷笅杞界殑 URL 鍒楄〃锛堜笉闇€瑕?session_id锛?)
    parser.add_argument("--output-dir", default="", help="杈撳嚭鐩綍锛堥粯璁?~/Downloads/libtv_results/锛?)
    parser.add_argument("--prefix", default="", help="鏂囦欢鍚嶅墠缂€锛堝 'storyboard' 鈫?storyboard_01.png锛?)
    parser.add_argument("--workers", type=int, default=5, help="骞惰涓嬭浇绾跨▼鏁帮紙榛樿 5锛?)
    args = parser.parse_args()

    # 鏀堕泦 URL
    urls = list(args.urls)
    if args.session_id:
        data = query_session(args.session_id)
        messages = data.get("messages", [])
        extracted = extract_urls_from_messages(messages)
        urls.extend(extracted)

    if not urls:
        print(json.dumps({"error": "鏈壘鍒板彲涓嬭浇鐨勫浘鐗?瑙嗛 URL", "downloaded": []}, ensure_ascii=False, indent=2))
        sys.exit(1)

    # 鍑嗗杈撳嚭鐩綍
    output_dir = args.output_dir or os.path.expanduser("~/Downloads/libtv_results")
    os.makedirs(output_dir, exist_ok=True)

    # 鏋勫缓涓嬭浇浠诲姟
    tasks = []
    for i, url in enumerate(urls, 1):
        ext = os.path.splitext(url.split("?")[0])[-1] or ".png"
        if args.prefix:
            filename = f"{args.prefix}_{i:02d}{ext}"
        else:
            filename = f"{i:02d}{ext}"
        filepath = os.path.join(output_dir, filename)
        tasks.append((url, filepath))

    # 骞惰涓嬭浇
    results = []
    errors = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(download_file, url, fp): (url, fp) for url, fp in tasks}
        for future in as_completed(futures):
            fp, err = future.result()
            if err:
                errors.append({"file": fp, "error": err})
            else:
                results.append(fp)

    # 鎸夋枃浠跺悕鎺掑簭杈撳嚭
    results.sort()

    output = {
        "output_dir": output_dir,
        "downloaded": results,
        "total": len(results),
    }
    if errors:
        output["errors"] = errors

    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
