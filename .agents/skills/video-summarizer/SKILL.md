---
name: video-summarizer
description: "Summarize or download videos from 1800+ platforms (YouTube, Bilibili, Twitter/X, TikTok, Vimeo, Instagram, etc.). Uses a subtitle-first workflow: when subtitles exist, generate VTT subtitles, a TXT transcript, and an MD summary without downloading or transcoding media; download MP4/audio only when subtitles are unavailable for transcription or the user explicitly requests media files."
---

# Video Summarizer

Extract and summarize videos from supported platforms. The default deliverables are subtitles, transcript, and summary. Download video/audio only when transcription is required because subtitles are unavailable, or when the user explicitly asks for media files.

Default outputs when subtitles are available:
- Subtitle file (with timestamps, vtt/srt format)
- Transcript file (txt)
- Summary file (summary.md)

Conditional outputs:
- Original video file (mp4) — only on explicit request or when needed by a fallback workflow
- Audio file (mp3/m4a) — only when subtitles are unavailable and transcription is required, or on explicit request

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
├── subtitle.vtt
├── transcript.txt
├── summary.md
├── video.mp4       # optional
└── audio.mp3       # optional
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

### Step 3: Download Video/Audio (only if no subtitles or explicitly requested)

**Critical rule**: If platform subtitles were downloaded successfully, do not download, extract, merge, or transcode video/audio by default. Proceed directly to summary generation. Media processing is unnecessary in the subtitle-first workflow and wastes time, bandwidth, CPU, and disk space.

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
& python313 "$SKILL_DIR/scripts/generate_summary.py" "$OUTPUT_DIR/transcript.txt" "$OUTPUT_DIR/summary.md" --title "视频标题" --url "$VIDEO_URL" --duration 视频时长秒数 --pubdate "YYYY-MM-DD"
```

**Important**: Use `--pubdate` to pass the video's actual publish date (from API), not the download date. This ensures catalog is sorted by publish order.

Where `python313` is shorthand for `C:\Users\chandlernie\AppData\Local\Programs\Python\Python313\python.exe`

### Step 6: Update Catalog

After generating the summary, automatically add the video to the catalog:

```powershell
& python313 "$SKILL_DIR/scripts/update_catalog.py" "$OUTPUT_DIR/summary.md" "$CATALOG_PATH"
```

The `update_catalog.py` script will:
1. Extract metadata (title, pubdate/date, url) from summary.md
2. **Use 发布时间 (pubdate) for sorting** - falls back to 下载时间 if pubdate not available
3. Add a new entry to catalog.md under the appropriate date section
4. Update the "最后更新" timestamp

## Scripts

| Script | Description | Usage (Windows PowerShell) |
|--------|-------------|---------------------------|
| `get_bilibili_subtitle.py` | Download Bilibili subtitles using cookie file | `& python313 scripts/get_bilibili_subtitle.py <AID> <CID> <OUTPUT_DIR> [COOKIE_FILE]` |
| `convert_subtitle.py` | Convert JSON subtitles to VTT/TXT | `& python313 scripts/convert_subtitle.py <INPUT_JSON> <OUTPUT_VTT>` |
| `parallel_transcribe.py` | Transcribe audio using Whisper | `& python313 scripts/parallel_transcribe.py --input <AUDIO> --output-dir <DIR>` |
| `generate_summary.py` | Generate AI summary with retry logic and fallback | `& python313 scripts/generate_summary.py <TRANSCRIPT> <OUTPUT> [OPTIONS]` |
| `update_catalog.py` | Add video entry to catalog.md (sorted by pubdate) | `& python313 scripts/update_catalog.py <SUMMARY_MD> <CATALOG_MD>` |

## Notes

1. **Windows**: Use PowerShell with `& python313` or direct Python path — NOT `uv run python` which fails
2. **Paths**: Use forward slashes in paths (/) or double quotes; avoid backslash escaping issues
3. **Bilibili**: See `$SKILL_DIR/reference/bilibili-method.md` for cookie setup and full workflow
4. **DeepLearning.AI**: See `$SKILL_DIR/reference/deeplearning-ai-course-method.md`
5. **Workflow order**: Always try subtitles first. If subtitles exist, skip all video/audio downloading and transcoding unless the user explicitly requested media. Only download audio/video and transcribe when subtitles are unavailable.
6. **Storage**: Files saved to `./downloads/<website>/<video_id>/`
7. **Copyright**: For personal learning use only

## Error Handling

- **No subtitles**: Use parallel_transcribe.py for transcription
- **Video too long**: The transcription script handles long files automatically
- **Bilibili cookie issues**: See `$SKILL_DIR/reference/bilibili-method.md` for cookie refresh steps
- **DeepLearning.AI captions fail**: Fall back to VTT URL from `subtitleUrl` field
- **API 529/Overloaded**: Retry with exponential backoff (3 attempts), fall back to transcript-only summary if all fail
- **Encoding errors**: Always specify `encoding='utf-8'` when reading/writing files
- **Model 401 "not supported" / empty 400 response**: `generate_summary.py` first tries `deepseek-v4.1-flash`, then the optional `ANTHROPIC_MODEL`, then `deepseek-v4-flash` and `deepseek-v4-pro`, skipping duplicate model IDs. Retain this fallback chain because gateway availability and model support can change.
- **Truncated summary (ends mid-list)**: generate_summary.py checks both `stop_reason` (`max_tokens`/`length`) and structural completeness. A result is incomplete unless it contains the required closing sections—关键引述/重要观点、相关话题/关键词、技术信息—with 技术信息 near the end. Incomplete output escalates through 4096→8192→16384→32768 tokens even when the gateway incorrectly reports a normal stop. The summary must not duplicate the full transcript; `transcript.txt` is the canonical raw text, keeping long-video summaries within practical non-streaming limits.
- **`update_catalog.py` has no dedup**: do NOT re-run it for an already-catalogued video after regenerating summary.md — it would add a duplicate row. Edit the existing row manually (e.g., to add the author).
- **Gateway 400 "MissingSessionID"**: the OpenCode gateway requires an `x-opencode-session` header on every request. `generate_summary.py` resolves it from `OPENCODE_SESSION_ID`, then `CLAUDE_CODE_SESSION_ID`; if neither exists, it creates one random ID for the script run. The value is routing metadata, not an authentication secret.
- **Gateway authentication**: `generate_summary.py` explicitly reads `OPENCODE_API_KEY` first and falls back to `ANTHROPIC_API_KEY` for compatibility. It also prefers `OPENCODE_BASE_URL`, then `ANTHROPIC_BASE_URL`, before using the SDK default endpoint. A terminal `/v1` is removed because the Anthropic SDK appends `/v1/messages`; this prevents accidental `/v1/v1/messages` requests. Credentials are passed without being logged. If neither key variable is set, the script emits a clear missing-credentials error and uses its transcript-based fallback.

<!-- Evolution: 2026-09-08 | source: BV1UobN66EyM | skill: video-summarizer -->
**Pattern Added (2026-09-08)**: Subprocess API calls to the gateway failed with `400 MissingSessionID — Request is missing x-opencode-session` even after the model fallback chain — every model attempt failed the same way and the run silently produced the transcript-only fallback summary. Root cause: the opencode gateway started requiring the `x-opencode-session` routing header, which Claude Code adds to its own requests but child Python processes don't have. Fix: build the client with `default_headers={'x-opencode-session': os.environ.get('CLAUDE_CODE_SESSION_ID')}` when the env var is present. Verified with a minimal messages call, then a full summary run completed via deepseek-v4-flash at max_tokens=16384.

<!-- Evolution: 2026-08-20 | source: ep-2026-08-20-002 | skill: video-summarizer -->
**Historical pattern (2026-08-20)**: A single hardcoded model ID previously failed with `401`; a configurable model and fallback chain restored summary generation. The current preferred model and ordering are documented above.

<!-- Evolution: 2026-08-20 | source: ep-2026-08-20-003 | skill: video-summarizer -->
**Pattern Refined (2026-08-20)**: The env-var model itself (`gpt-5.6-luna`) can be broken through the gateway — it returned an empty `400` with `content: [{type: text, text: ''}]`. Added a multi-model fallback chain (`ANTHROPIC_MODEL` → `deepseek-v4-flash` → `deepseek-v4-pro`) so a single broken model no longer degrades the summary to the fallback. Verified: gpt-5.6-luna failed, deepseek-v4-flash produced the full summary.

<!-- Evolution: 2026-09-01 | source: BV1m7th6uEH3 | skill: video-summarizer -->
**Pattern Added (2026-09-01)**: `generate_summary.py` silently saved truncated output. A 68-min video (20,628-char transcript) truncated at `max_tokens=4096` — summary.md ended mid-list at "6." with no error. Fix: check `response.stop_reason` for `max_tokens`/`length` and escalate through token levels [4096, 8192, 16384, 32768]; models that exhaust the budget get skipped. Observed: deepseek-v4-flash truncates even at 16384; deepseek-v4-pro completes at 8192. Also: max_tokens=32768 triggers the gateway's "Streaming is required" error — cap escalation at 16384 for non-streaming calls, or enable streaming.

## Bilibili-Specific Notes

- **Console garbled Chinese**: Use Python API to get video title - console output may show garbled text but Python handles UTF-8 correctly
- **Pubdate for sorting**: Always pass `--pubdate YYYY-MM-DD` to generate_summary.py - catalog sorts by video publish date, not download date
- **Title verification**: Verify title from API response, not from console output

<!-- Correction: 2026-10-29 | source: user feedback during BV1cFnd6VEgQ | reason: unnecessary media transcoding after subtitles were already available -->
**Workflow Correction (2026-10-29)**: Successful subtitle retrieval is a terminal condition for media acquisition in summary-only requests. Generate `subtitle.vtt`, `transcript.txt`, and `summary.md`, then stop. Do not download or transcode video/audio unless subtitles are missing or the user explicitly requests those files.

<!-- Evolution: 2026-10-29 | source: user feedback during BV1cFnd6VEgQ | skill: video-summarizer -->
**Authentication Update (2026-10-29)**: Standalone summary generation now prefers `OPENCODE_API_KEY` / `OPENCODE_BASE_URL` and retains `ANTHROPIC_API_KEY` / `ANTHROPIC_BASE_URL` as compatibility fallbacks. Pass the resolved configuration explicitly to the Anthropic-compatible client; keep the session routing header, model fallback chain, and retry behavior unchanged.

<!-- Evolution: 2026-10-29 | source: user feedback | skill: video-summarizer -->
**Model preference**: Try `deepseek-v4.1-flash` first for video summaries. If unavailable or unable to produce a complete summary, continue through the configured and existing fallback models. Explicit user preference supersedes the previous environment-first order.
