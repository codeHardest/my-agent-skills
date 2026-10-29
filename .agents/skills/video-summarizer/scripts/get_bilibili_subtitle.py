#!/usr/bin/env python3
"""
Download Bilibili subtitles using cookies from a file.

Usage:
    python get_bilibili_subtitle.py <AID> <CID> <OUTPUT_DIR> [COOKIE_FILE]

Arguments:
    AID: Bilibili video AID (e.g., 115981733136330)
    CID: Bilibili video CID for specific page
    OUTPUT_DIR: Output directory for subtitle files
    COOKIE_FILE: Path to cookie file (default: ./downloads/bilibili/bilibili-cookies.txt)
"""

import sys
import os
import json
import urllib.request


def load_cookies(cookie_file):
    """Parse Netscape cookie file format."""
    cookies = []

    # Try different encodings
    for encoding in ['utf-16', 'utf-8', 'utf-8-sig', 'latin-1']:
        try:
            with open(cookie_file, 'r', encoding=encoding) as f:
                lines = f.readlines()
            break
        except UnicodeDecodeError:
            continue
    else:
        # Fallback: read as binary and decode
        with open(cookie_file, 'rb') as f:
            content = f.read().decode('utf-16', errors='ignore')
            lines = content.split('\n')

    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            parts = line.split('\t')
            if len(parts) >= 7:
                domain, flag, path, secure, expiration, name, value = parts[:7]
                # Only include bilibili cookies
                if 'bilibili' in domain.lower():
                    cookies.append((name, value, domain))

    return cookies


def get_subtitle(aid, cid, output_dir, cookie_file='./downloads/bilibili/bilibili-cookies.txt'):
    """Download subtitle from Bilibili API."""

    # Check cookie file exists
    if not os.path.exists(cookie_file):
        print(f'Cookie file not found: {cookie_file}')
        print('Please export cookies from Chrome using Get Cookies or Cookie-Editor extension')
        return None

    # Load cookies
    cookies = load_cookies(cookie_file)
    print(f'Loaded {len(cookies)} bilibili cookies')

    if not cookies:
        print('No bilibili cookies found in cookie file')
        return None

    # Build cookie header
    cookie_header = '; '.join([f'{c[0]}={c[1]}' for c in cookies])

    # Make API request
    url = f'https://api.bilibili.com/x/player/wbi/v2?aid={aid}&cid={cid}'
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    req.add_header('Referer', 'https://www.bilibili.com')
    req.add_header('Accept', 'application/json')
    req.add_header('Cookie', cookie_header)

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            subtitle = data.get('data', {}).get('subtitle', {})
            subtitles = subtitle.get('subtitles', [])

            if subtitles:
                downloaded = []
                for s in subtitles:
                    lan = s.get('lan', '')
                    subtitle_url = s.get('subtitle_url', '')
                    print(f'Found subtitle: {lan}')

                    # Download subtitle if it contains Chinese or is ai-zh
                    if 'zh' in lan.lower() or lan == 'ai-zh':
                        filename = os.path.join(output_dir, f'subtitle_{lan}.json')
                        urllib.request.urlretrieve(f'https:{subtitle_url}', filename)
                        print(f'Downloaded: {filename}')
                        downloaded.append(filename)
                return downloaded
            else:
                print('No subtitles found')
                # Debug: check login status
                login_status = data.get('data', {}).get('login_mid', 0)
                need_login = data.get('data', {}).get('need_login_subtitle', False)
                print(f'Debug: login_mid={login_status}, need_login_subtitle={need_login}')
                return None

    except Exception as e:
        print(f'Error: {e}')
        return None


def get_video_info(bvid):
    """Get video AID and CID from BVID."""
    import requests

    url = f'https://api.bilibili.com/x/web-interface/view?bvid={bvid}'
    response = requests.get(url)
    data = response.json()

    aid = data.get('data', {}).get('aid')
    cid = data.get('data', {}).get('cid')
    title = data.get('data', {}).get('title')
    duration = data.get('data', {}).get('duration')

    return aid, cid, title, duration


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    aid = sys.argv[1]
    cid = sys.argv[2]
    output_dir = sys.argv[3]
    cookie_file = sys.argv[4] if len(sys.argv) > 4 else './downloads/bilibili/bilibili-cookies.txt'

    os.makedirs(output_dir, exist_ok=True)

    print(f'AID: {aid}, CID: {cid}')
    print(f'Output: {output_dir}')
    print(f'Cookies: {cookie_file}')
    print()

    result = get_subtitle(aid, cid, output_dir, cookie_file)

    if result:
        print(f'\nSuccess! Downloaded {len(result)} subtitle file(s)')
    else:
        print('\nFailed to download subtitles')
        sys.exit(1)


if __name__ == '__main__':
    main()
