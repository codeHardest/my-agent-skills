# Bilibili Video Summarization Method

## Overview

Bilibili videos require login cookies to download AI-generated subtitles (自动字幕). The workflow uses the Bilibili API to fetch subtitles after extracting video metadata.

## Prerequisites

### Cookie Setup

1. Install "Get Cookies" or "Cookie-Editor" Chrome extension
2. Go to bilibili.com and log in
3. Export cookies using the extension
4. Save to: `downloads/bilibili/bilibili-cookies.txt`

**Cookie format**: Netscape format (standard cookie export format)

### Dependencies

```bash
bash "$SKILL_DIR/scripts/install_deps.sh"
```

## Workflow

### Step 1: Get Video Info

Extract BVID and create output directory:

```python
import yt_dlp
import requests

def get_video_info(bvid):
    """Get video info via Bilibili API (more reliable than yt-dlp for Chinese encoding)."""
    url = f'https://api.bilibili.com/x/web-interface/view?bvid={bvid}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://www.bilibili.com'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    aid = data['data']['aid']
    cid = data['data']['cid']
    title = data['data']['title']
    duration = data['data']['duration']
    return aid, cid, title, duration

# Usage
bvid = "BV1qv6eBZErD"
aid, cid, title, duration = get_video_info(bvid)
```

### Step 2: Get AID and CID

**IMPORTANT**: Requires valid login cookies. Cookies expire periodically — re-export if subtitle download fails.

```bash
python "$SKILL_DIR/scripts/get_bilibili_subtitle.py" \
    "$AID" \
    "$CID" \
    "$OUTPUT_DIR" \
    "./downloads/bilibili/bilibili-cookies.txt"
```

### Step 4: Convert Subtitles

Convert JSON subtitles to VTT and TXT formats:

```bash
python "$SKILL_DIR/scripts/convert_subtitle.py" \
    "$OUTPUT_DIR/subtitle_ai-zh.json" \
    "$OUTPUT_DIR"
```

**Output files:**
- `subtitle_ai-zh.json` - Original AI subtitle JSON
- `subtitle.vtt` - WebVTT format with timestamps
- `subtitle.txt` - Plain text transcript

### Step 5: Download Video/Audio (Optional)

```bash
# Download video (best quality up to 1080p)
yt-dlp -f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best" \
    --merge-output-format mp4 \
    -o "$OUTPUT_DIR/video.%(ext)s" "$VIDEO_URL"

# Download audio only
yt-dlp -x --audio-format mp3 -o "$OUTPUT_DIR/audio.%(ext)s" "$VIDEO_URL"
```

### Step 6: Generate Summary

Use the `generate_summary.py` script with retry logic:

```bash
python "$SKILL_DIR/scripts/generate_summary.py" \
    "$OUTPUT_DIR/transcript.txt" \
    "$OUTPUT_DIR/summary.md" \
    --title "$TITLE" \
    --url "https://www.bilibili.com/video/$BVID" \
    --duration "$DURATION"
```

The script will:
- Retry API calls up to 3 times with exponential backoff on 529/429 errors
- Fall back to transcript-based summary if API fails completely
- Handle encoding properly (UTF-8)

## API Details

### Bilibili Subtitle API

```
GET https://api.bilibili.com/x/player/wbi/v2?aid={AID}&cid={CID}
```

**Headers required:**
- `User-Agent`: Mozilla/5.0
- `Referer`: https://www.bilibili.com
- `Cookie`: Login cookies from bilibili.com

**Response:**
```json
{
  "data": {
    "subtitle": {
      "subtitles": [
        {
          "lan": "ai-zh",
          "subtitle_url": "//i0.hdslb.com/bfs/subtitle/..."
        }
      ]
    }
  }
}
```

### Cookie File Format

Netscape format (same as curl/wget exports):
```
# Netscape HTTP Cookie File
.domain.com	TRUE	/	FALSE	0	cookie_name	cookie_value
```

Only cookies containing "bilibili" in the domain are used.

## Output Structure

```
./downloads/bilibili/{bvid}/
├── video.mp4           # Original video (optional)
├── audio.mp3           # Audio file (optional)
├── subtitle_ai-zh.json # Raw AI subtitle JSON
├── subtitle.vtt       # VTT subtitles with timestamps
├── transcript.txt      # Plain text transcript
└── summary.md          # AI summary
```

## Bilibili Series/Playlist Handling

For multi-part videos (e.g., `BV1173jzNELG_p2`):

1. Extract all episode BVIDs using yt-dlp:
```bash
yt-dlp --print "%(id)s" --flat-playlist "https://www.bilibili.com/series/BV1W2cgzREUj"
```

2. Process each part individually:
```bash
for BVID in "${BV_LIST[@]}"; do
    # Get AID, CID for each
    # Download subtitles
    # Generate summary
done
```

3. Create series summary combining all parts:
```
./downloads/bilibili/{series-name}/
├── 01-part-title.json
├── 01-part-title-summary.md
├── 02-part-title.json
├── 02-part-title-summary.md
└── series-summary.md
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| "Cookie file not found" | Cookies not exported | Export cookies from Chrome |
| "No subtitles found" | Not logged in / cookies expired | Re-export cookies |
| "need_login_subtitle=true" | Cookies expired | Refresh cookies in browser |
| Empty subtitle file | API rate limit | Wait and retry |
| Chinese garbled | Encoding issue | Use UTF-8 when saving |

## Cookie Refresh Checklist

1. Clear bilibili.com cookies in browser
2. Log in again
3. Export cookies using extension
4. Overwrite `downloads/bilibili/bilibili-cookies.txt`
5. Retry subtitle download

## Quick Reference

```bash
# Full workflow (using Python API for reliability)
BVID="BV1qv6eBZErD"
OUTPUT_DIR="./downloads/bilibili/$BVID"
mkdir -p "$OUTPUT_DIR"

# Get video info using Python API (handles Chinese encoding better)
python -c "
import requests
url = 'https://api.bilibili.com/x/web-interface/view?bvid=${BVID}'
headers = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://www.bilibili.com'}
data = requests.get(url, headers=headers).json()
print(f'AID={data[\"data\"][\"aid\"]}')
print(f'CID={data[\"data\"][\"cid\"]}')
print(f'TITLE={data[\"data\"][\"title\"]}')
print(f'DURATION={data[\"data\"][\"duration\"]}')
"

# Download subtitles (requires cookies)
python "$SKILL_DIR/scripts/get_bilibili_subtitle.py" "$AID" "$CID" "$OUTPUT_DIR"

# Convert JSON to VTT/TXT
python "$SKILL_DIR/scripts/convert_subtitle.py" "$OUTPUT_DIR/subtitle_ai-zh.json" "$OUTPUT_DIR"

# Generate summary with retry logic
python "$SKILL_DIR/scripts/generate_summary.py" "$OUTPUT_DIR/transcript.txt" "$OUTPUT_DIR/summary.md" --title "$TITLE" --url "https://www.bilibili.com/video/$BVID" --duration "$DURATION"
```
