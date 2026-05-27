import json
import os
import subprocess

PYTHON = r"C:\Users\chandlernie\AppData\Local\Programs\Python\Python313\python.exe"
SKILL_DIR = r"P:\AI\my-agent-skills\.claude\skills\video-summarizer"
SCRIPT_DIR = os.path.join(SKILL_DIR, "scripts")
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

def load_transcript(video_id):
    caption_path = os.path.join(BASE_DIR, f"{video_id}_caption.json")
    with open(caption_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    captions = data.get('data', {}).get('captions', [])
    return " ".join([c["text"] for c in sorted(captions, key=lambda x: x["startInSeconds"])])

def format_time(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins}:{secs:02d}"

# Create transcript files
print("Creating transcript files...")
for video in VIDEOS:
    vid = video["videoId"]
    transcript = load_transcript(vid)
    transcript_path = os.path.join(BASE_DIR, f"{vid}_transcript.txt")
    with open(transcript_path, 'w', encoding='utf-8') as f:
        f.write(transcript)
    print(f"  Created {vid}_transcript.txt ({len(transcript)} chars)")

print("\nTranscript files created. Now generating summaries...")
print("=" * 60)

# Generate summaries
for video in VIDEOS:
    vid = video["videoId"]
    name = video["name"]
    slug = video["slug"]
    duration = video["time"]
    lesson_url = f"{COURSE_URL}/lesson/{slug}/{slug}"

    transcript_path = os.path.join(BASE_DIR, f"{vid}_transcript.txt")
    summary_path = os.path.join(BASE_DIR, f"{vid}_summary.md")

    print(f"\nGenerating summary for: {name}")
    print(f"  URL: {lesson_url}")
    print(f"  Duration: {format_time(duration)}")

    cmd = [
        PYTHON,
        os.path.join(SCRIPT_DIR, "generate_summary.py"),
        transcript_path,
        summary_path,
        "--title", name,
        "--url", lesson_url,
        "--duration", str(duration),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  SUCCESS: {summary_path}")
    else:
        print(f"  ERROR: {result.stderr[:200] if result.stderr else 'Unknown error'}")

print("\n" + "=" * 60)
print("All summaries generated!")
