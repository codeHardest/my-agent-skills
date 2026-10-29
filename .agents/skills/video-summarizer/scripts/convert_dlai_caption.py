#!/usr/bin/env python3
"""
Convert DeepLearning.AI caption.json to subtitle.vtt and transcript.txt.

DeepLearning.AI caption format:
{
  "code": 200,
  "data": {
    "captions": [
      {"startInSeconds": 0, "endInSeconds": 9, "text": "..."},
      ...
    ],
    "subtitleUrl": "https://..."
  }
}
"""

import json
import os
import sys


def to_vtt_time(secs: float) -> str:
    h = int(secs) // 3600
    m = (int(secs) % 3600) // 60
    s = int(secs) % 60
    ms = int(round((secs - int(secs)) * 1000))
    if ms == 1000:
        s += 1
        ms = 0
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def main():
    if len(sys.argv) < 3:
        print("Usage: convert_dlai_caption.py <caption.json> <output_dir>")
        sys.exit(1)

    json_file = sys.argv[1]
    out_dir = sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    captions = data.get("data", {}).get("captions", [])
    print(f"Loaded {len(captions)} caption segments")

    vtt_path = os.path.join(out_dir, "subtitle.vtt")
    with open(vtt_path, "w", encoding="utf-8") as f:
        f.write("WEBVTT\n\n")
        for c in captions:
            start = to_vtt_time(c["startInSeconds"])
            end = to_vtt_time(c["endInSeconds"])
            f.write(f"{start} --> {end}\n")
            f.write(c["text"].strip() + "\n\n")
    print(f"Wrote {vtt_path}")

    txt_path = os.path.join(out_dir, "transcript.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        for c in captions:
            f.write(c["text"].strip() + " ")
    print(f"Wrote {txt_path}")

    url = data.get("data", {}).get("subtitleUrl")
    if url:
        print(f"subtitleUrl: {url}")


if __name__ == "__main__":
    main()
