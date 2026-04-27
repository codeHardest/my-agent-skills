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

## Environment (Windows)

When running on Windows with uv and Python installed via winget/pip:

- **uv**: `C:\Users\chandlernie\AppData\Local\Microsoft\WinGet\Packages\astral-sh.uv_Microsoft.Winget.Source_8wekyb3d8bbwe\uv.exe`
- **Python**: `C:\Users\chandlernie\AppData\Local\Programs\Python\Python313\python.exe`

**Important**: `uv run python` may fail with "No Python" error. If so, use direct Python path:
```bash
"C:\Users\chandlernie\AppData\Local\Programs\Python\Python313\python.exe" <script.py>
```

Or use PowerShell:
```powershell
& "C:\Users\chandlernie\AppData\Local\Programs\Python\Python313\python.exe" script.py
```

## Workflow

### Step 1: Get Video Info

```bash
VIDEO_URL="https://www.bilibili.com/video/BV1qv6eBZErD"
VIDEO_ID="BV1qv6eBZErD"

# Create output directory
mkdir -p "./downloads/bilibili/${VIDEO_ID}/"
```

### Step 2: Download Subtitles

**Platform-specific methods:**

- **Bilibili**: See `$SKILL_DIR/reference/bilibili-method.md`
- **deepLearning.AI**: See `$SKILL_DIR/reference/deeplearning-ai-course-method.md`
- **YouTube/Other platforms**: Use PowerShell with direct paths

### Step 3: Download Video/Audio (if no subtitles)

```powershell
# Use PowerShell with full paths
& "C:\Users\chandlernie\AppData\Local\Programs\Python\Python313\python.exe" -m yt_dlp -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best" --merge-output-format mp4 -o "$OUTPUT_DIR/video.%(ext)s" "$VIDEO_URL"
```

### Step 4: Transcribe (if no subtitles)

```powershell
& python313 "$SKILL_DIR/scripts/parallel_transcribe.py" --input "$OUTPUT_DIR/audio.mp3" --output-dir "$OUTPUT_DIR" --model small
```

### Step 5: Generate Summary

```powershell
& python313 "$SKILL_DIR/scripts/generate_summary.py" "$OUTPUT_DIR/transcript.txt" "$OUTPUT_DIR/summary.md" --title "视频标题" --url "$VIDEO_URL" --duration 视频时长秒数
```

Where `python313` is shorthand for `C:\Users\chandlernie\AppData\Local\Programs\Python\Python313\python.exe`

## Scripts

| Script | Description | Usage (Windows PowerShell) |
|--------|-------------|---------------------------|
| `get_bilibili_subtitle.py` | Download Bilibili subtitles using cookie file | `& python313 scripts/get_bilibili_subtitle.py <AID> <CID> <OUTPUT_DIR> [COOKIE_FILE]` |
| `convert_subtitle.py` | Convert JSON subtitles to VTT/TXT | `& python313 scripts/convert_subtitle.py <INPUT_JSON> <OUTPUT_VTT>` |
| `parallel_transcribe.py` | Transcribe audio using Whisper | `& python313 scripts/parallel_transcribe.py --input <AUDIO> --output-dir <DIR>` |
| `generate_summary.py` | Generate AI summary with retry logic and fallback | `& python313 scripts/generate_summary.py <TRANSCRIPT> <OUTPUT> [OPTIONS]` |

## Notes

1. **Windows**: Use PowerShell with `& python313` or direct Python path — NOT `uv run python` which fails
2. **Paths**: Use forward slashes in paths (/) or double quotes; avoid backslash escaping issues
3. **Bilibili**: See `$SKILL_DIR/reference/bilibili-method.md` for cookie setup and full workflow
4. **DeepLearning.AI**: See `$SKILL_DIR/reference/deeplearning-ai-course-method.md`
5. **Workflow order**: Always try subtitles first, then transcribe if needed
6. **Storage**: Files saved to `./downloads/<website>/<video_id>/`
7. **Copyright**: For personal learning use only

## Error Handling

- **No subtitles**: Use parallel_transcribe.py for transcription
- **Video too long**: The transcription script handles long files automatically
- **Bilibili cookie issues**: See `$SKILL_DIR/reference/bilibili-method.md` for cookie refresh steps
- **DeepLearning.AI captions fail**: Fall back to VTT URL from `subtitleUrl` field
- **API 529/Overloaded**: Retry with exponential backoff (3 attempts), fall back to transcript-only summary if all fail
- **Encoding errors**: Always specify `encoding='utf-8'` when reading/writing files
