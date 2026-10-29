# DeepLearning.AI Course Summarization Method

## Overview

DeepLearning.AI courses (learn.deeplearning.ai) provide structured lesson transcripts through a caption API. The API endpoint pattern is:
```
https://platform-api.dlai.link/videos/{video_id}/caption.json
```

**Important**: The `video_id` in the API is NOT the lesson slug from the URL. It is a separate numeric `videoId` field (e.g., 1199188, 1199189, etc.) that must be obtained from the course structure API.

Video IDs can be found in the course URL: `/courses/.../lesson/{lesson-id}/{lesson-slug}` but for API calls, use the `videoId` from the course metadata.

## Finding All Lessons in a Course

### Step 1: Get Course Structure

Fetch the course API to get all lesson metadata:
```
GET https://platform-api.dlai.link/courses/{course-slug}
```

Example: `https://platform-api.dlai.link/courses/retrieval-augmented-generation`

Response includes:
```json
{
  "data": {
    "lessons": {
      "rrngb": { "slug": "rrngb", "name": "A conversation with Andrew Ng", "type": "video", "videoId": 1199188, "time": 489 },
      "qq2xz": { "slug": "qq2xz", "name": "Module 1 introduction", "type": "video", "videoId": 1199189, "time": 89 }
    },
    "subtopics": { ... }
  }
}
```

### Step 2: Identify Video Lessons

Filter lessons where `type === "video"`. Other types include:
- `notebook` - Interactive code notebooks (no video)
- `quiz` - Graded quizzes
- `reading_material` - Reading materials

### Step 3: Download Transcripts

For each video lesson, fetch captions using the numeric `videoId`:
```bash
# Correct: Use videoId (1199188)
curl -s "https://platform-api.dlai.link/videos/1199188/caption.json"

# Wrong: Using lesson slug (rrngb) will fail with 422
curl -s "https://platform-api.dlai.link/videos/rrngb/caption.json"  # 422 error!
```

### Step 4: Generate Module/Course Summary

For multi-video courses (like Module 1), create a combined summary with:

```markdown
# Module X: [Title] (课程总结)

**课程来源**: DeepLearning.AI
**课程名称**: [Course Name]
**课程链接**: https://learn.deeplearning.ai/courses/{course-slug}
**Module X**: [Module Name]

---

## Module X 概述

[2-3 sentences about module purpose]

**视频列表**:

---

## 视频 1: [Title]
**时长**: ~X min
**链接**: https://learn.deeplearning.ai/courses/{course-slug}/lesson/{lesson-id}/{slug}
**视频 ID**: {videoId}

### 内容总结

[Summary in Chinese]

---

## 视频 2: [Title]
...

---

## Module X 完整视频列表

| 序号 | 视频标题 | 时长 | 链接 | 视频 ID |
|------|---------|------|------|---------|
| 1 | Title | ~X min | URL | videoId |
...

---

## Module X 关键概念总结

### 核心概念
- [Concept 1]
- [Concept 2]

---

*此总结由 AI 自动生成，仅供学习参考使用*
```

## Caption API Response Format

```json
{
  "code": 200,
  "result": true,
  "data": {
    "captions": [
      {
        "startInSeconds": 0,
        "endInSeconds": 9,
        "text": "Welcome to the course..."
      }
    ],
    "subtitleUrl": "https://video.deeplearning.ai/..."
  }
}
```

### Concatenating Transcript
```python
# Simple concatenation preserving order
transcript = " ".join([c["text"] for c in sorted(captions, key=lambda x: x["startInSeconds"])])
```

### Timestamps in Summary
Group content by time segments (every 30-60 seconds) for better structure:
```
[0:00-0:30] - Course introduction
[0:30-2:00] - Problem statement
...
```

## Error Handling

- **422 Unprocessable Entity**: Usually means wrong video ID format - verify you're using numeric `videoId`, not the lesson slug
- **Socket closed / Connection reset**: Retry the caption request - some requests fail intermittently
- **Missing captions**: Try VTT URL from `subtitleUrl` field as fallback
- **Network errors**: Retry with exponential backoff

## Quick Reference

```
Course URL: https://learn.deeplearning.ai/courses/{course-slug}
Course API: https://platform-api.dlai.link/courses/{course-slug}
Caption API: https://platform-api.dlai.link/videos/{videoId}/caption.json
Lesson URL: https://learn.deeplearning.ai/courses/{course-slug}/lesson/{module}/{lesson-slug}
```

## Course Structure Analysis

### Typical Course Structure
- **Module 1**: Overview/Introduction (~5-8 video lessons)
- **Modules 2-N**: Core content (10-15 video lessons each)
- **Each Module includes**:
  - Introduction video
  - Core lesson videos
  - Optional notebook exercises
  - Quiz (locked)
  - Module conclusion video

### Lesson Types
| Type | Has Video | Has Transcript | Notes |
|------|-----------|---------------|-------|
| video | Yes | Yes (caption.json) | Main learning content |
| notebook | No | No | Interactive code exercises |
| quiz | No | No | Graded assessment |
| reading_material | No | No | Supplementary materials |
| graded_notebook | No | No | Coding assignments |