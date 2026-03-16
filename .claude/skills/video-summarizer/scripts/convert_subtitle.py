#!/usr/bin/env python3
"""
Convert Bilibili JSON subtitles to VTT and TXT formats.

Usage:
    python convert_subtitle.py <JSON_FILE> <OUTPUT_DIR>

Arguments:
    JSON_FILE: Path to the JSON subtitle file
    OUTPUT_DIR: Output directory for subtitle files
"""

import json
import sys
import os


def convert_subtitle(json_file, output_dir):
    """Convert JSON subtitle to VTT and TXT formats."""

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    body = data.get('body', [])
    print(f'Converted {len(body)} subtitle lines')

    # Convert to VTT format
    vtt_file = os.path.join(output_dir, 'subtitle.vtt')
    with open(vtt_file, 'w', encoding='utf-8') as f:
        f.write('WEBVTT\n\n')
        for line in body:
            start = line.get('from', 0)
            end = line.get('to', 0)
            content = line.get('content', '')

            # Convert to VTT time format
            start_vtt = f'{int(start)//3600:02d}:{(int(start)%3600)//60:02d}.{int(start*1000)%1000:03d}'
            end_vtt = f'{int(end)//3600:02d}:{(int(end)%3600)//60:02d}.{int(end*1000)%1000:03d}'

            f.write(f'{start_vtt} --> {end_vtt}\n')
            f.write(f'{content}\n\n')

    print(f'Created: {vtt_file}')

    # Convert to plain text
    txt_file = os.path.join(output_dir, 'transcript.txt')
    with open(txt_file, 'w', encoding='utf-8') as f:
        for line in body:
            content = line.get('content', '')
            f.write(content + '\n')

    print(f'Created: {txt_file}')
    return vtt_file, txt_file


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    json_file = sys.argv[1]
    output_dir = sys.argv[2]

    if not os.path.exists(json_file):
        print(f'Error: JSON file not found: {json_file}')
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    convert_subtitle(json_file, output_dir)
    print('\nConversion complete!')


if __name__ == '__main__':
    main()
