import json
import os
import re

BASE_DIR = r"P:\AI\my-agent-skills\downloads\deeplearning-ai\agent-skills-with-anthropic"

VIDEOS = [
    {"slug": "ldn5c3", "name": "Introduction", "videoId": 10145001, "time": 166},
    {"slug": "bv2ekh", "name": "Why Use Skills - Part I", "videoId": 10145002, "time": 676},
    {"slug": "eg4sac", "name": "Why Use Skills - Part II", "videoId": 10145003, "time": 513},
    {"slug": "9iovmn", "name": "Skills vs Tools, MCP, and Subagents", "videoId": 10145004, "time": 454},
    {"slug": "cniu9q", "name": "Exploring Pre-Built Skills", "videoId": 10145005, "time": 1113},
    {"slug": "txwyf5", "name": "Creating Custom Skills", "videoId": 10145006, "time": 975},
    {"slug": "3sq9za", "name": "Skills with the Claude API", "videoId": 10145007, "time": 1045},
    {"slug": "cniu9b", "name": "Skills with Claude Code", "videoId": 10145008, "time": 1492},
    {"slug": "rmykgh", "name": "Skills with the Claude Agent SDK", "videoId": 10145009, "time": 1223},
    {"slug": "dea3n4", "name": "Conclusion", "videoId": 10145010, "time": 43},
]

COURSE_URL = "https://learn.deeplearning.ai/courses/agent-skills-with-anthropic"

def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    if mins >= 60:
        hours = mins // 60
        mins = mins % 60
        return f"{hours}:{mins:02d}:{secs:02d}"
    return f"{mins}:{secs:02d}"

def parse_summary_json(content):
    """Parse JSON format summary."""
    try:
        # Extract JSON from markdown code block
        content = content.strip()
        if content.startswith('```json'):
            content = content[7:]
        if content.startswith('```'):
            content = content[3:]
        content = content.strip()

        # Find JSON boundaries
        start = content.find('{')
        end = content.rfind('}') + 1
        if start >= 0 and end > start:
            json_str = content[start:end]
            data = json.loads(json_str)
            return {
                'content_overview': data.get('content_overview', ''),
                'core_points': data.get('core_points', [])
            }
    except Exception as e:
        print(f"JSON parse error: {e}")
    return {'content_overview': '', 'core_points': []}

def parse_summary_markdown(content):
    """Parse markdown format summary."""
    result = {'content_overview': '', 'core_points': []}

    # Find content overview
    if "## 内容概述" in content:
        lines = content.split('\n')
        in_overview = False
        overview_lines = []
        for line in lines:
            if line.strip() == "## 内容概述":
                in_overview = True
                continue
            if in_overview:
                if line.startswith('## '):
                    break
                if line.strip():
                    overview_lines.append(line.strip())
        result['content_overview'] = ' '.join(overview_lines)

    # Find core points
    lines = content.split('\n')
    in_core_points = False
    for line in lines:
        if line.strip() == "## 核心要点":
            in_core_points = True
            continue
        if in_core_points:
            if line.startswith('## '):
                break
            if line.strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.')):
                point = line.strip()
                point = re.sub(r'^\d+\.\s*', '', point)
                point = re.sub(r'\*\*(.*?)\*\*', r'\1', point)
                result['core_points'].append(point)

    return result

def extract_summary(video_id):
    """Extract summary content from summary file."""
    summary_path = os.path.join(BASE_DIR, f"{video_id}_summary.md")
    try:
        with open(summary_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()

        content = content.strip()
        if content.startswith('{') or content.startswith('```'):
            return parse_summary_json(content)
        else:
            return parse_summary_markdown(content)
    except Exception as e:
        print(f"Error reading {video_id}: {e}")
        return {'content_overview': '', 'core_points': []}

# Build the combined markdown
output = []
output.append("# Agent Skills with Anthropic - 课程总结")
output.append("")
output.append("**课程来源**: DeepLearning.AI")
output.append("**课程链接**: https://learn.deeplearning.ai/courses/agent-skills-with-anthropic")
output.append("**课程简介**: Equip agents with expert on-demand knowledge to enable reliable coding, research, and data analysis workflows")
output.append("")
output.append("---")
output.append("")

# Video list table
output.append("## 视频列表")
output.append("")
output.append("| 序号 | 视频标题 | 时长 | 链接 |")
output.append("|------|---------|------|------|")
for i, video in enumerate(VIDEOS, 1):
    lesson_url = f"{COURSE_URL}/lesson/{video['slug']}/{video['slug']}"
    output.append(f"| {i} | {video['name']} | {format_time(video['time'])} | [链接]({lesson_url}) |")
output.append("")
output.append("---")
output.append("")

# Process each video
for i, video in enumerate(VIDEOS, 1):
    video_id = video["videoId"]
    name = video["name"]
    slug = video["slug"]
    duration = format_time(video["time"])
    lesson_url = f"{COURSE_URL}/lesson/{slug}/{slug}"

    summary = extract_summary(video_id)
    content_overview = summary['content_overview']
    core_points = summary['core_points']

    output.append(f"## 视频 {i}: {name}")
    output.append("")
    output.append(f"**时长**: {duration}")
    output.append(f"**链接**: {lesson_url}")
    output.append("")

    if content_overview:
        output.append("### 内容总结")
        output.append("")
        output.append(content_overview)
        output.append("")

    if core_points:
        output.append("### 核心知识点")
        output.append("")
        for point in core_points:
            output.append(f"- {point}")
        output.append("")

    output.append("---")
    output.append("")

# Write the output file
output_path = os.path.join(BASE_DIR, "course_summary.md")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print(f"Course summary created: {output_path}")
print(f"Total videos processed: {len(VIDEOS)}")
