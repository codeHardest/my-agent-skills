---
name: video-summarizer
description: "Download videos from 1800+ platforms (YouTube, Bilibili, Twitter/X, TikTok, Vimeo, Instagram, etc.) and generate complete resource package with video, audio, subtitles, and AI summary. Actions: summarize, download, transcribe, extract video content. Platforms: youtube.com, bilibili.com, twitter.com, x.com, tiktok.com, vimeo.com, instagram.com, twitch.tv. Outputs: MP4 video, MP3 audio, VTT subtitles with timestamps, TXT transcript, MD AI summary. Auto-installs uv, yt-dlp, ffmpeg. Python dependencies managed by uv."
---

# Video Summarizer

Download videos from any platform and generate a complete resource package including:
- Original video file (mp4)
- Audio file (mp3)
- Subtitle file (with timestamps, vtt/srt format)
- Summary file (summary.md)

## Trigger Conditions

When the user:
- Provides a video link and asks for a summary
- Says "summarize this video", "what's in this video"
- Asks to "extract video content", "transcribe video"
- Says "download this video"
- Provides a link from YouTube/Bilibili/Twitter/Vimeo/TikTok etc.

## Supported Platforms

- YouTube, Bilibili, Twitter/X, Vimeo, TikTok, Instagram, Twitch
- And 1800+ other platforms (all sites supported by yt-dlp)

## Output Structure

```
./downloads/<website>/<video_id>/
├── video.mp4
├── audio.mp3
├── subtitle.vtt
├── transcript.txt
└── summary.md
```

## Quick Start

```bash
# Install dependencies
bash "$SKILL_DIR/scripts/install_deps.sh"
```

## Workflow

### Step 1: Get Video Info

```bash
VIDEO_URL="https://www.bilibili.com/video/BV1qv6eBZErD"

# Extract video ID and create output directory
yt-dlp --print "%(id)s" -o "./downloads/temp" "$VIDEO_URL"
```

### Step 2: Download Subtitles

**For Bilibili** (requires login cookies):

1. If `downloads/bilibili/bilibili-cookies.txt` does not exist:
   - Export cookies from Chrome using "Get Cookies" or "Cookie-Editor" extension
   - Save to: `downloads/bilibili/bilibili-cookies.txt`
2. If cookies file exists, skip to next step
3. Run:

```bash
python "$SKILL_DIR/scripts/get_bilibili_subtitle.py" \
    "$AID" \
    "$CID" \
    "$OUTPUT_DIR" \
    "./downloads/bilibili/bilibili-cookies.txt"

# Convert to VTT/TXT
python "$SKILL_DIR/scripts/convert_subtitle.py" \
    "$OUTPUT_DIR/subtitle_ai-zh.json" \
    "$OUTPUT_DIR"
```

**For YouTube/Other platforms:**

```bash
yt-dlp --write-subs --sub-lang zh-Hans,en --skip-download \
    -o "$OUTPUT_DIR/subtitle" "$VIDEO_URL"
```

### Step 3: Download Video/Audio (if no subtitles)

```bash
yt-dlp -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best" \
    --merge-output-format mp4 \
    -o "$OUTPUT_DIR/video.%(ext)s" "$VIDEO_URL"

yt-dlp -x --audio-format mp3 -o "$OUTPUT_DIR/audio.%(ext)s" "$VIDEO_URL"
```

### Step 4: Transcribe (if no subtitles)

```bash
uv run "$SKILL_DIR/scripts/parallel_transcribe.py" \
    --input "$OUTPUT_DIR/audio.mp3" \
    --output-dir "$OUTPUT_DIR" \
    --model small
```

### Step 5: Generate Summary

1. Read prompt template from `$SKILL_DIR/reference/summary-prompt.md`
2. Replace placeholders with video info and transcript
3. Use Claude API to generate summary
4. Save to `$OUTPUT_DIR/summary.md`

## Scripts

| Script | Description |
|--------|-------------|
| `install_deps.sh` | Install dependencies (uv, ffmpeg, yt-dlp) |
| `get_bilibili_subtitle.py` | Download Bilibili subtitles using cookie file |
| `convert_subtitle.py` | Convert JSON subtitles to VTT/TXT |
| `parallel_transcribe.py` | Transcribe audio using Whisper |

## Notes

1. **Bilibili cookies**: Export from Chrome and save to `downloads/bilibili/bilibili-cookies.txt`
2. **Workflow order**: Always try subtitles first, then transcribe if needed
3. **Storage**: Files saved to `./downloads/<website>/<video_id>/`
4. **Copyright**: For personal learning use only

## Error Handling

- **No subtitles**: Use parallel_transcribe.py for transcription
- **Video too long**: The transcription script handles long files automatically
- **Cookie issues**: Re-export cookies from browser (may expire)
