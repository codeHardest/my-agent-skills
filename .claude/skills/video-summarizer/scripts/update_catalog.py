#!/usr/bin/env python3
"""
Update catalog.md with a new video entry from summary.md
Parses summary.md metadata and adds entry to catalog.md under the correct date section.
"""

import re
import sys
from datetime import datetime
from pathlib import Path


def extract_metadata(summary_path: str) -> dict:
    """Extract metadata from summary.md file."""
    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()

    metadata = {}

    # Extract title from first heading (format: "# 视频摘要：xxx")
    title_match = re.search(r'^#\s*视频摘要[：:]\s*(.+)$', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip()

    # Extract URL
    url_match = re.search(r'\*\*URL\*\*:\s*(.+)', content)
    if url_match:
        metadata['url'] = url_match.group(1).strip()

    # Extract author/uploader
    author_match = re.search(r'\*\*作者/UP主\*\*:\s*(.+)', content)
    if author_match:
        metadata['author'] = author_match.group(1).strip()

    # Extract publish date (优先使用发布时间)
    pubdate_match = re.search(r'\*\*发布时间\*\*:\s*(\d{4}-\d{2}-\d{2})', content)
    if pubdate_match:
        metadata['date'] = pubdate_match.group(1).strip()
    else:
        # Fallback to download date if pubdate not available
        date_match = re.search(r'\*\*下载时间\*\*:\s*(\d{4}-\d{2}-\d{2})', content)
        if date_match:
            metadata['date'] = date_match.group(1).strip()

    return metadata


def detect_platform(url: str) -> str:
    """Detect platform directory name from URL."""
    if not url:
        return 'other'
    url_lower = url.lower()
    if "bilibili.com" in url_lower or "b23.tv" in url_lower:
        return 'bilibili'
    if "youtube.com" in url_lower or "youtu.be" in url_lower:
        return 'youtube'
    if "twitter.com" in url_lower or "x.com" in url_lower:
        return 'twitter'
    if "tiktok.com" in url_lower:
        return 'tiktok'
    if "vimeo.com" in url_lower:
        return 'vimeo'
    if "instagram.com" in url_lower:
        return 'instagram'
    if "twitch.tv" in url_lower:
        return 'twitch'
    return 'other'


def extract_video_id(url: str) -> str:
    """Extract platform-specific video ID from URL."""
    if not url:
        return ''
    # YouTube: watch?v=XXXXX or youtu.be/XXXXX or shorts/XXXXX
    yt_match = re.search(r'(?:v=|youtu\.be/|shorts/|live/)([A-Za-z0-9_-]{6,})', url)
    if yt_match:
        return yt_match.group(1)
    # Bilibili: /BVxxxx or /av12345
    bv_match = re.search(r'/(BV[\w]+)', url)
    if bv_match:
        return bv_match.group(1)
    av_match = re.search(r'/(av\d+)', url)
    if av_match:
        return av_match.group(1)
    # Vimeo/TikTok/Twitter: trailing numeric or path segment
    tail_match = re.search(r'/([^/?#]+)/?$', url)
    if tail_match:
        return tail_match.group(1)
    return ''


def format_catalog_entry(metadata: dict) -> str:
    """Format a single catalog entry line."""
    title = metadata.get('title', '未知标题')
    url = metadata.get('url', '')
    author = metadata.get('author', '')

    platform = detect_platform(url)
    video_id = extract_video_id(url)

    link = f"[summary.md](../../downloads/{platform}/{video_id}/summary.md)" if video_id else ''

    return f"| {author} | {title} | {link} |"


def find_section_insert_pos(catalog_content: str, target_date: str) -> int:
    """
    Find the correct position to insert a new date section.
    Returns the character position.
    """
    year = target_date[:4]
    target_date_str = target_date[5:]  # MM-DD

    # Find the year section
    year_pattern = rf'## {year}年\n'
    year_match = re.search(year_pattern, catalog_content)

    if not year_match:
        # Year doesn't exist, find where to insert
        # Find first year section after target year
        next_year_pos = None
        for y in range(int(year) + 1, 9999):
            m = re.search(rf'## {y}年\n', catalog_content)
            if m:
                next_year_pos = m.start()
                break

        if next_year_pos:
            return next_year_pos
        else:
            # Add before final ---
            return catalog_content.rfind('\n---\n') + 1

    # Year exists, find the correct position within the year
    year_start = year_match.end()

    # Find all date sections in this year
    date_pattern = rf'### \d{{4}}-\d{{2}}-\d{{2}}\n'
    pos = year_start
    insert_pos = None

    while True:
        match = re.search(date_pattern, catalog_content[pos:])
        if not match:
            break

        section_date = match.group()[4:14]  # Extract YYYY-MM-DD
        if section_date < target_date:
            # Move past this section's content
            next_section = re.search(r'\n## |\n### \d{4}', catalog_content[pos + match.end():])
            if next_section:
                pos += match.end() + next_section.start()
            else:
                pos = len(catalog_content)
                break
        else:
            insert_pos = pos + match.start()
            break

    if insert_pos is None:
        # Append at end of year section
        # Find next ## or end of file
        next_year = re.search(r'\n## \d{4}年\n', catalog_content[year_start:])
        if next_year:
            insert_pos = year_start + next_year.start()
        else:
            # Find closing ---
            end_match = re.search(r'\n---\n', catalog_content[year_start:])
            if end_match:
                insert_pos = year_start + end_match.start()
            else:
                insert_pos = len(catalog_content)

    return insert_pos


def update_catalog(summary_path: str, catalog_path: str):
    """Update catalog.md with entry from summary.md."""
    summary_path = Path(summary_path)
    catalog_path = Path(catalog_path)

    # Extract metadata
    metadata = extract_metadata(str(summary_path))

    if not metadata.get('date'):
        print("Error: Could not extract date from summary.md")
        sys.exit(1)

    if not metadata.get('url'):
        print("Error: Could not extract URL from summary.md")
        sys.exit(1)

    # Read catalog
    with open(catalog_path, 'r', encoding='utf-8') as f:
        catalog_content = f.read()

    # Find where to insert
    insert_pos = find_section_insert_pos(catalog_content, metadata['date'])

    # Create new section content (include year header if section doesn't exist yet)
    year = metadata['date'][:4]
    year_exists = re.search(rf'^## {year}年$', catalog_content, re.MULTILINE)
    year_header = f"## {year}年\n\n" if not year_exists else ""
    new_section = f"\n{year_header}### {metadata['date']}\n\n| 发布者 | 标题 | 链接 |\n|--------|------|------|\n"
    new_entry = format_catalog_entry(metadata) + '\n\n'

    # Insert
    catalog_content = catalog_content[:insert_pos] + new_section + new_entry + catalog_content[insert_pos:]

    # Update "最后更新" timestamp
    today = datetime.now().strftime('%Y-%m-%d')
    catalog_content = re.sub(
        r'\*最后更新:\s*\d{4}-\d{2}-\d{2}\*',
        f'*最后更新: {today}*',
        catalog_content
    )

    # Write updated catalog
    with open(catalog_path, 'w', encoding='utf-8') as f:
        f.write(catalog_content)

    print(f"Added to catalog: {metadata['title']}")
    print(f"Date: {metadata['date']}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: update_catalog.py <summary.md> <catalog.md>")
        sys.exit(1)

    update_catalog(sys.argv[1], sys.argv[2])