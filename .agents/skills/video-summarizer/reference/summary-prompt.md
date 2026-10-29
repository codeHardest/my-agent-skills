# Video Summary Prompt Template

Generate a structured summary based on the following video transcript and metadata. **Preserve all original data** — do not omit any information from the input.

## Video Information (Original Metadata)
{{VIDEO_INFO}}

## Transcript Content (Full Original)
{{TRANSCRIPT}}

## Original Subtitle Timestamps (if available)
{{TIMESTAMPS}}

---

## Please generate summary in the following format:

# Video Summary: {{TITLE}}

## Basic Information
- **Source**: {{PLATFORM}}
- **URL**: {{URL}}
- **Duration**: {{DURATION}}
- **Language**: {{LANGUAGE}}
- **Download Time**: {{DOWNLOAD_TIME}}

## Video Metadata (All Original Fields)
{{METADATA_BLOCK}}

## Output Files
- video.mp4 - Original video
- audio.mp3 - Audio file
- subtitle.vtt - Subtitles (with timestamps)
- subtitle_ai-zh.json - Original AI subtitle JSON
- transcript.txt - Plain text transcript
- summary.md - This summary file

## Overview
[2-3 sentences summarizing the main content]

## Key Points
1. [Point 1]
2. [Point 2]
3. [Point 3]
... (extract 3-15 key points based on content length)

## Detailed Content (Preserve ALL original information)

### [Topic 1]
[Detailed explanation with all supporting details from the original content]

### [Topic 2]
[Detailed explanation with all supporting details from the original content]

### [Topic 3]
[Detailed explanation with all supporting details from the original content]

... (add more sections as needed to cover all topics)

## Complete Transcript (Full Original Text)
```
{{FULL_TRANSCRIPT}}
```

## Notable Quotes / Key Statements
> "[Important quote 1 with timestamp if available]"

> "[Important quote 2 with timestamp if available]"

> "[Important quote 3 with timestamp if available]"

... (extract all notable quotes)

## Related Topics / Keywords
- [Related topic 1]
- [Related topic 2]
- [Related topic 3]
... (derive from all content)

## Technical Notes
- Transcript word count: {{WORD_COUNT}}
- Transcript character count: {{CHAR_COUNT}}
- Original subtitle entries: {{SUBTITLE_COUNT}}
- Processing date: {{DOWNLOAD_TIME}}
