#!/usr/bin/env python3
"""
Generate video summary using Claude API with retry logic.

Usage:
    python generate_summary.py <TRANSCRIPT_FILE> <OUTPUT_FILE> [--title TITLE] [--url URL] [--duration DURATION]

Arguments:
    TRANSCRIPT_FILE: Path to transcript.txt file
    OUTPUT_FILE: Path to save summary.md
    --title: Video title (default: "Unknown")
    --url: Video URL (default: "")
    --duration: Video duration in seconds (default: "")
"""

import argparse
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


def generate_summary_with_retry(transcript, title, url, duration, max_retries=3, initial_delay=2):
    """
    Generate summary using Claude API with exponential backoff retry.

    Raises:
        Exception: If all retries fail after max_retries attempts.
    """
    client = anthropic.Anthropic()

    duration_str = f"{int(duration)}秒 (约{int(duration)//60}分钟)" if duration else "未知"
    duration_short = f"{int(duration)}秒" if duration else "未知"

    prompt = f'''你是一个专业的视频内容总结专家。请根据以下视频字幕/录音转写内容生成一份结构化的中文摘要。

## 视频信息
- **标题**: {title}
- **来源**: Bilibili
- **URL**: {url}
- **时长**: {duration_str}
- **语言**: 中文
- **下载时间**: {time.strftime("%Y-%m-%d")}

## 字幕/Transcript 内容
{transcript}

---

## 请生成以下格式的摘要：

# 视频摘要

## 基本信息
- **来源**: Bilibili
- **URL**: {url}
- **时长**: {duration_short}
- **语言**: 中文

## 内容概述
[2-3句话概括主要内容]

## 核心要点
1. [要点1]
2. [要点2]
3. [要点3]
... (根据内容提取3-10个核心要点)

## 详细内容
[按主题分段详细展开，每个主题2-5句话]

## 关键观点/结论
- [结论1]
- [结论2]
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


def generate_transcript_summary(transcript, title, url, duration):
    """
    Generate a basic summary directly from transcript (fallback when API fails).
    """
    lines = [l.strip() for l in transcript.split('\n') if l.strip()]

    # Take first ~20 lines as overview excerpt
    excerpt = '\n'.join(lines[:20]) if len(lines) > 20 else transcript

    duration_str = f"{int(duration)}秒 (约{int(duration)//60}分钟)" if duration else "未知"
    duration_min = int(duration) // 60 if duration else 0
    excerpt_preview = lines[5][:50] + "..." if len(lines) > 5 else "详见全文"

    return f'''# 视频摘要

## 基本信息
- **来源**: Bilibili
- **URL**: {url}
- **时长**: {duration_str}
- **语言**: 中文
- **备注**: 此为由机器人生成的自动摘要（API不可用时生成）

## 内容概述
本视频时长约{duration_min}分钟，内容涉及{excerpt_preview}等话题。完整内容请查看transcript.txt。

## 核心要点
(由于API不可用，无法生成核心要点。请参考完整字幕内容。)

## 重要摘录（前50行字幕）

```
{excerpt}
```

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
    parser.add_argument('--max-retries', type=int, default=3, help='Max API retry attempts')

    args = parser.parse_args()

    if not os.path.exists(args.transcript_file):
        print(f"Error: Transcript file not found: {args.transcript_file}", file=sys.stderr)
        sys.exit(1)

    print(f"Reading transcript: {args.transcript_file}")
    transcript = read_transcript(args.transcript_file)
    print(f"Transcript length: {len(transcript)} characters")

    # Ensure output directory exists
    os.makedirs(os.path.dirname(args.output_file) or '.', exist_ok=True)

    print("\nGenerating summary with Claude API...")
    try:
        summary = generate_summary_with_retry(
            transcript,
            args.title,
            args.url,
            args.duration,
            max_retries=args.max_retries
        )
    except Exception as e:
        print(f"\nWarning: API summary failed: {e}")
        print("Generating fallback transcript-based summary...")
        summary = generate_transcript_summary(transcript, args.title, args.url, args.duration)

    # Save summary
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"\nSummary saved to: {args.output_file}")


if __name__ == '__main__':
    main()
