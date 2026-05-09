#!/usr/bin/env python3
"""Download generation results: Extract all image/video URLs from session and batch download to local"""

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
    """Extract all image and video result URLs from session messages"""
    urls = []
    url_pattern = re.compile(r'https://libtv-res\.liblib\.art/[^\s"\'<>]+\.(?:png|jpg|jpeg|webp|mp4|mov|webm)')

    for msg in messages:
        content = msg.get("content", "")
        if not content or not isinstance(content, str):
            continue

        # Extract from task_result (toolmsg returned results)
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

        # Extract URL from assistant text messages
        if msg.get("role") == "assistant":
            found = url_pattern.findall(content)
            urls.extend(found)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            unique.append(u)
    return unique


def download_file(url, filepath):
    """Download single file"""
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
        description="Download generated images/videos from session to local",
        epilog="""
Usage:
  # Extract and download all results from session
  python3 download_results.py SESSION_ID

  # Specify output directory
  python3 download_results.py SESSION_ID --output-dir ~/Desktop/my_project

  # Specify filename prefix
  python3 download_results.py SESSION_ID --prefix "storyboard"

  # Directly download specified URL list
  python3 download_results.py --urls URL1 URL2 URL3 --output-dir ./output
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("session_id", nargs="?", default="", help="Session ID, auto-extract all generation result URLs")
    parser.add_argument("--urls", nargs="+", default=[], help="Directly specify URL list to download (no session_id needed)")
    parser.add_argument("--output-dir", default="", help="Output directory (default ~/Downloads/libtv_results/)")
    parser.add_argument("--prefix", default="", help="Filename prefix (e.g., 'storyboard' -> storyboard_01.png)")
    parser.add_argument("--workers", type=int, default=5, help="Parallel download threads (default 5)")
    args = parser.parse_args()

    # Collect URLs
    urls = list(args.urls)
    if args.session_id:
        data = query_session(args.session_id)
        messages = data.get("messages", [])
        extracted = extract_urls_from_messages(messages)
        urls.extend(extracted)

    if not urls:
        print(json.dumps({"error": "No downloadable image/video URLs found", "downloaded": []}, ensure_ascii=False, indent=2))
        sys.exit(1)

    # Prepare output directory
    output_dir = args.output_dir or os.path.expanduser("~/Downloads/libtv_results")
    os.makedirs(output_dir, exist_ok=True)

    # Build download tasks
    tasks = []
    for i, url in enumerate(urls, 1):
        ext = os.path.splitext(url.split("?")[0])[-1] or ".png"
        if args.prefix:
            filename = f"{args.prefix}_{i:02d}{ext}"
        else:
            filename = f"{i:02d}{ext}"
        filepath = os.path.join(output_dir, filename)
        tasks.append((url, filepath))

    # Parallel download
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

    # Sort results by filename
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
