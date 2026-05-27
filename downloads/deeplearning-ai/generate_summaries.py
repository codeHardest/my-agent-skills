import json
import os
import sys

# Video metadata from the course API
VIDEOS = [
    {"slug": "ldn5c3", "name": "Introduction", "videoId": 10145001, "time": 166, "type": "video"},
    {"slug": "bv2ekh", "name": "Why Use Skills - Part I", "videoId": 10145002, "time": 676, "type": "video_reading"},
    {"slug": "eg4sac", "name": "Why Use Skills - Part II", "videoId": 10145003, "time": 513, "type": "video_reading"},
    {"slug": "9iovmn", "name": "Skills vs Tools, MCP, and Subagents", "videoId": 10145004, "time": 454, "type": "video_reading"},
    {"slug": "cniu9q", "name": "Exploring Pre-Built Skills", "videoId": 10145005, "time": 1113, "type": "video_reading"},
    {"slug": "txwyf5", "name": "Creating Custom Skills", "videoId": 10145006, "time": 975, "type": "video_reading"},
    {"slug": "3sq9za", "name": "Skills with the Claude API", "videoId": 10145007, "time": 1045, "type": "video_reading"},
    {"slug": "cniu9b", "name": "Skills with Claude Code", "videoId": 10145008, "time": 1492, "type": "video_reading"},
    {"slug": "rmykgh", "name": "Skills with the Claude Agent SDK", "videoId": 10145009, "time": 1223, "type": "video_reading"},
    {"slug": "dea3n4", "name": "Conclusion", "videoId": 10145010, "time": 43, "type": "video"},
]

COURSE_SLUG = "agent-skills-with-anthropic"
COURSE_NAME = "Agent Skills with Anthropic"
BASE_DIR = "P:/AI/my-agent-skills/downloads/deeplearning-ai/agent-skills-with-anthropic"
COURSE_URL = f"https://learn.deeplearning.ai/courses/{COURSE_SLUG}"


def load_transcript(video_id):
    """Load and concatenate transcript from caption JSON."""
    caption_path = os.path.join(BASE_DIR, f"{video_id}_caption.json")
    try:
        with open(caption_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        captions = data.get('data', {}).get('captions', [])
        # Sort by start time and concatenate
        transcript = " ".join([c["text"] for c in sorted(captions, key=lambda x: x["startInSeconds"])])
        return transcript
    except Exception as e:
        print(f"Error loading caption for {video_id}: {e}")
        return ""


def format_time(seconds):
    """Format seconds to MM:SS."""
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins}:{secs:02d}"


# Load all transcripts
print("Loading transcripts...")
video_data = []
for video in VIDEOS:
    video_id = video["videoId"]
    transcript = load_transcript(video_id)
    video_data.append({
        **video,
        "transcript": transcript,
        "duration": format_time(video["time"]),
        "lesson_url": f"{COURSE_URL}/lesson/{video['slug']}"
    })
    print(f"  Loaded {video['name']}: {len(transcript)} chars")

print(f"\nTotal videos: {len(video_data)}")
print("Transcripts loaded successfully!")
