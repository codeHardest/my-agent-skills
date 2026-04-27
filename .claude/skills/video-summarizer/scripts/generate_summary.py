#!/usr/bin/env python3
"""
Generate video summary using Claude API with retry logic.
Windows: Use `uv run python scripts/generate_summary.py ...`

Usage (Windows):
    uv run python scripts/generate_summary.py <TRANSCRIPT_FILE> <OUTPUT_FILE> [OPTIONS]

Arguments:
    TRANSCRIPT_FILE: Path to transcript.txt file
    OUTPUT_FILE: Path to save summary.md
    --title: Video title (default: "Unknown")
    --url: Video URL (default: "")
    --duration: Video duration in seconds (default: "")
    --author: Video author/uploader (default: "")
    --view-count: View count (default: 0)
    --like-count: Like count (default: 0)
    --coin-count: Coin count (default: 0)
    --favorite-count: Favorite count (default: 0)
    --share-count: Share count (default: 0)
    --danmaku-count: Danmaku (bullet chat) count (default: 0)
    --subtitle-json: Path to original subtitle JSON file (default: "")
    --timestamps: Timestamps string from subtitles (default: "")
"""

import argparse
import json
import os
import sys
import time
import anthropic
from anthropic import RateLimitError
from anthropic._exceptions import OverloadedError


def read_transcript(transcript_path):
    """Read transcript file with UTF-8 encoding."""
    with open(transcript_path, 'r', encoding='utf-8') as f:
        return f.read()


def read_subtitle_json(subtitle_json_path):
    """Read original subtitle JSON file to extract timestamps."""
    if not subtitle_json_path or not os.path.exists(subtitle_json_path):
        return ""
    try:
        with open(subtitle_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Extract timestamps from subtitle body
        if 'body' in data and isinstance(data['body'], list):
            timestamps = []
            for item in data['body']:
                if 'from' in item and 'to' in item and 'content' in item:
                    start = item['from']
                    end = item['to']
                    content = item['content'].replace('\n', ' ')
                    timestamps.append(f"[{start:.2f}s - {end:.2f}s] {content}")
            return '\n'.join(timestamps[:500])  # Limit to first 500 entries
        return ""
    except Exception as e:
        print(f"Warning: Could not read subtitle JSON: {e}")
        return ""


def format_count(count, default=0):
    """Format large numbers in human-readable form."""
    if not count:
        count = default
    if isinstance(count, str):
        try:
            count = int(count)
        except:
            return str(count)
    if count >= 100000000:
        return f"{count / 100000000:.1f}亿"
    elif count >= 100000:
        return f"{count / 10000:.1f}万"
    return str(count)


def generate_summary_with_retry(transcript, title, url, duration, author="", view_count=0, like_count=0,
                                coin_count=0, favorite_count=0, share_count=0, danmaku_count=0,
                                subtitle_json="", timestamps="", max_retries=3, initial_delay=2):
    """
    Generate summary using Claude API with exponential backoff retry.

    Raises:
        Exception: If all retries fail after max_retries attempts.
    """
    client = anthropic.Anthropic()

    duration_str = f"{int(duration)}秒 (约{int(duration)//60}分钟)" if duration else "未知"
    duration_short = f"{int(duration)}秒" if duration else "未知"
    download_time = time.strftime("%Y-%m-%d %H:%M:%S")
    word_count = len(transcript)
    char_count = len(transcript.replace('\n', ''))

    # Build metadata block
    metadata_parts = []
    if author:
        metadata_parts.append(f"- **作者/UP主**: {author}")
    if view_count:
        metadata_parts.append(f"- **播放量**: {format_count(view_count)}")
    if like_count:
        metadata_parts.append(f"- **点赞数**: {format_count(like_count)}")
    if coin_count:
        metadata_parts.append(f"- **投币数**: {format_count(coin_count)}")
    if favorite_count:
        metadata_parts.append(f"- **收藏数**: {format_count(favorite_count)}")
    if share_count:
        metadata_parts.append(f"- **分享数**: {format_count(share_count)}")
    if danmaku_count:
        metadata_parts.append(f"- **弹幕数**: {format_count(danmaku_count)}")
    metadata_block = '\n'.join(metadata_parts) if metadata_parts else "- (无额外元数据)"

    # Read timestamps from subtitle JSON if available
    if timestamps and subtitle_json:
        ts_data = read_subtitle_json(subtitle_json)
        if ts_data:
            timestamps = ts_data

    subtitle_count = len(timestamps.split('\n')) if timestamps else 0

    prompt = f'''你是一个专业的视频内容总结专家。请根据以下视频字幕/录音转写内容生成一份结构化的中文摘要。**请保留所有原始数据，不要省略任何信息。**

## 视频信息
- **标题**: {title}
- **来源**: Bilibili
- **URL**: {url}
- **时长**: {duration_str}
- **语言**: 中文
- **下载时间**: {download_time}

## 原始元数据
{metadata_block}

## 字幕/Transcript 内容
{transcript}

## 时间戳信息 (前500条)
{timestamps if timestamps else "(无时间戳信息)"}

---

## 请生成以下格式的摘要，**保留所有原始数据**：

# 视频摘要：{title}

## 基本信息
- **来源**: Bilibili
- **URL**: {url}
- **时长**: {duration_str}
- **语言**: 中文
- **下载时间**: {download_time}

## 原始元数据
{metadata_block}

## 输出文件
- video.mp4 - 原始视频文件
- audio.mp3 - 音频文件
- subtitle.vtt - 带时间戳的字幕文件
- subtitle_ai-zh.json - 原始AI字幕JSON
- transcript.txt - 纯文本转录
- summary.md - 本摘要文件

## 内容概述
[2-3句话概括主要内容]

## 核心要点
1. [要点1]
2. [要点2]
3. [要点3]
... (根据内容提取3-15个核心要点，尽可能全面)

## 详细内容（保留所有原始信息）

### [主题1]
[详细展开，包含所有支持细节]

### [主题2]
[详细展开，包含所有支持细节]

### [主题3]
[详细展开，包含所有支持细节]

... (根据实际内容添加更多章节，覆盖所有话题)

## 完整字幕原文
```
{transcript}
```

## 关键引述/重要观点
> "[重要引述1]" [对应时间戳]

> "[重要引述2]" [对应时间戳]

> "[重要引述3]" [对应时间戳]

... (提取所有重要引述)

## 相关话题/关键词
- [关键词1]
- [关键词2]
- [关键词3]
... (从全部内容中提取)

## 技术信息
- 字幕字数: {word_count}
- 字幕字符数: {char_count}
- 时间戳条目数: {subtitle_count}
- 处理时间: {download_time}
'''

    last_error = None

    def extract_text_from_content(content):
        """Extract text from API response content, handling different block types."""
        if isinstance(content, str):
            return content
        if hasattr(content, 'text'):
            return content.text
        if hasattr(content, 'type'):
            if content.type == 'text':
                return content.text
            elif content.type == 'thinking':
                return ''  # Skip thinking blocks
        # Try iterating over content blocks
        result = []
        try:
            for block in content:
                if hasattr(block, 'text'):
                    result.append(block.text)
                elif hasattr(block, 'type') and block.type == 'text':
                    result.append(block.text)
        except:
            pass
        return '\n'.join(result) if result else ''

    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model='claude-haiku-4-5-20251001',
                max_tokens=4096,
                messages=[{
                    'role': 'user',
                    'content': prompt
                }]
            )
            text = extract_text_from_content(response.content)
            if text:
                return text
            # If no text extracted, raise error to trigger fallback
            raise ValueError("No text content in response")

        except (OverloadedError, RateLimitError) as e:
            last_error = e
            delay = initial_delay * (2 ** attempt)
            print(f"  API error (attempt {attempt + 1}/{max_retries}): {type(e).__name__}")
            print(f"  Retrying in {delay}s...")
            time.sleep(delay)

        except Exception as e:
            last_error = e
            print(f"  Unexpected error: {e}")
            break

        except Exception as e:
            last_error = e
            print(f"  Unexpected error: {e}")
            break

    raise Exception(f"Failed after {max_retries} retries. Last error: {last_error}")


def generate_transcript_summary(transcript, title, url, duration, author="", view_count=0, like_count=0,
                                coin_count=0, favorite_count=0, share_count=0, danmaku_count=0):
    """
    Generate a basic summary directly from transcript (fallback when API fails).
    Preserves all original metadata.
    """
    lines = [l.strip() for l in transcript.split('\n') if l.strip()]

    # Take first ~50 lines as overview excerpt
    excerpt = '\n'.join(lines[:50]) if len(lines) > 50 else transcript
    full_transcript = transcript

    duration_str = f"{int(duration)}秒 (约{int(duration)//60}分钟)" if duration else "未知"
    duration_min = int(duration) // 60 if duration else 0
    excerpt_preview = lines[5][:50] + "..." if len(lines) > 5 else "详见全文"
    download_time = time.strftime("%Y-%m-%d %H:%M:%S")
    word_count = len(transcript)
    char_count = len(transcript.replace('\n', ''))

    # Build metadata block
    metadata_parts = []
    if author:
        metadata_parts.append(f"- **作者/UP主**: {author}")
    if view_count:
        metadata_parts.append(f"- **播放量**: {format_count(view_count)}")
    if like_count:
        metadata_parts.append(f"- **点赞数**: {format_count(like_count)}")
    if coin_count:
        metadata_parts.append(f"- **投币数**: {format_count(coin_count)}")
    if favorite_count:
        metadata_parts.append(f"- **收藏数**: {format_count(favorite_count)}")
    if share_count:
        metadata_parts.append(f"- **分享数**: {format_count(share_count)}")
    if danmaku_count:
        metadata_parts.append(f"- **弹幕数**: {format_count(danmaku_count)}")
    metadata_block = '\n'.join(metadata_parts) if metadata_parts else "- (无额外元数据)"

    return f'''# 视频摘要：{title}

## 基本信息
- **来源**: Bilibili
- **URL**: {url}
- **时长**: {duration_str}
- **语言**: 中文
- **下载时间**: {download_time}
- **备注**: 此为由机器人生成的自动摘要（API不可用时生成）

## 原始元数据
{metadata_block}

## 输出文件
- video.mp4 - 原始视频文件
- audio.mp3 - 音频文件
- subtitle.vtt - 带时间戳的字幕文件
- subtitle_ai-zh.json - 原始AI字幕JSON
- transcript.txt - 纯文本转录
- summary.md - 本摘要文件

## 内容概述
本视频时长约{duration_min}分钟，内容涉及{excerpt_preview}等话题。完整内容请查看transcript.txt。

## 核心要点
(由于API不可用，无法生成核心要点。请参考完整字幕内容。)

## 完整字幕原文
```
{full_transcript}
```

## 重要摘录（前50行字幕）
```
{excerpt}
```

## 技术信息
- 字幕字数: {word_count}
- 字幕字符数: {char_count}
- 处理时间: {download_time}

---

*注意：这是基于完整字幕自动生成的摘要。如需更详细的人工智能摘要，请稍后重试。*
'''


def main():
    parser = argparse.ArgumentParser(description="Generate video summary using Claude API")
    parser.add_argument('transcript_file', help='Path to transcript.txt')
    parser.add_argument('output_file', help='Path to save summary.md')
    parser.add_argument('--title', default='Unknown Video', help='Video title')
    parser.add_argument('--url', default='', help='Video URL')
    parser.add_argument('--duration', type=float, default=0, help='Video duration in seconds')
    parser.add_argument('--author', default='', help='Video author/uploader')
    parser.add_argument('--view-count', type=int, default=0, help='View count')
    parser.add_argument('--like-count', type=int, default=0, help='Like count')
    parser.add_argument('--coin-count', type=int, default=0, help='Coin count')
    parser.add_argument('--favorite-count', type=int, default=0, help='Favorite count')
    parser.add_argument('--share-count', type=int, default=0, help='Share count')
    parser.add_argument('--danmaku-count', type=int, default=0, help='Danmaku (bullet chat) count')
    parser.add_argument('--subtitle-json', default='', help='Path to original subtitle JSON file')
    parser.add_argument('--max-retries', type=int, default=3, help='Max API retry attempts')

    args = parser.parse_args()

    if not os.path.exists(args.transcript_file):
        print(f"Error: Transcript file not found: {args.transcript_file}", file=sys.stderr)
        sys.exit(1)

    print(f"Reading transcript: {args.transcript_file}")
    transcript = read_transcript(args.transcript_file)
    print(f"Transcript length: {len(transcript)} characters")

    # Read timestamps from subtitle JSON if provided
    timestamps = ""
    if args.subtitle_json:
        print(f"Reading subtitle JSON: {args.subtitle_json}")
        timestamps = read_subtitle_json(args.subtitle_json)
        if timestamps:
            print(f"Extracted {len(timestamps.split(chr(10)))} timestamp entries")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(args.output_file) or '.', exist_ok=True)

    print("\nGenerating summary with Claude API...")
    try:
        summary = generate_summary_with_retry(
            transcript,
            args.title,
            args.url,
            args.duration,
            author=args.author,
            view_count=args.view_count,
            like_count=args.like_count,
            coin_count=args.coin_count,
            favorite_count=args.favorite_count,
            share_count=args.share_count,
            danmaku_count=args.danmaku_count,
            subtitle_json=args.subtitle_json,
            timestamps=timestamps,
            max_retries=args.max_retries
        )
    except Exception as e:
        print(f"\nWarning: API summary failed: {e}")
        print("Generating fallback transcript-based summary...")
        summary = generate_transcript_summary(
            transcript, args.title, args.url, args.duration,
            author=args.author,
            view_count=args.view_count,
            like_count=args.like_count,
            coin_count=args.coin_count,
            favorite_count=args.favorite_count,
            share_count=args.share_count,
            danmaku_count=args.danmaku_count
        )

    # Save summary
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"\nSummary saved to: {args.output_file}")


if __name__ == '__main__':
    main()
