# DeepLearning.AI Course Summarization Method

## Overview

DeepLearning.AI courses (learn.deeplearning.ai) provide structured lesson transcripts through a caption API. The API endpoint pattern is:
```
https://platform-api.dlai.link/videos/{video_id}/caption.json
```

Video IDs can be found in the course URL: `/courses/.../lesson/{lesson-id}/{lesson-slug}`

## Finding All Lessons in a Course

1. Visit the course page at `https://learn.deeplearning.ai/courses/{course-slug}/information`
2. All lessons are listed with their Video IDs (e.g., 10149001, 10149002, etc.)
3. Courses typically include 7-9 lessons (video lessons + reading + quiz)

## Caption API Method

### API Endpoint
```
GET https://platform-api.dlai.link/videos/{video_id}/caption.json
```

### Response Format
```json
{
  "code": 200,
  "result": true,
  "data": {
    "captions": [
      {
        "startInSeconds": 0,
        "endInSeconds": 3,
        "text": "Welcome to the course..."
      }
    ],
    "subtitleUrl": "https://video.deeplearning.ai/..."
  }
}
```

### How to Download Captions
1. Fetch the caption.json for each video
2. Extract the `captions` array containing timestamps and text
3. Optionally also fetch the VTT file from `subtitleUrl` for time-stamped subtitles

## Course Structure Analysis

### Typical Course Structure
- **Lesson 1**: Introduction/Overview (~2 mins)
- **Lessons 2-N**: Core content (15-25 mins each, with code examples)
- **Final Lesson**: Conclusion (~1 min)
- **Extra Resources**: Reading materials
- **Quiz**: Graded quiz

### Video Duration Patterns
| Lesson Type | Typical Duration |
|-------------|-----------------|
| Introduction | 1-3 mins |
| Core Lesson (with code) | 15-25 mins |
| Conclusion | 1-2 mins |
| Reading/Quiz | N/A |

## Summarization Workflow for DeepLearning.AI Courses

### Step 1: Identify Course Structure
1. Fetch the course information page to get all lesson titles and video IDs
2. Note the course syllabus (number of lessons, lesson types)

### Step 2: Download All Transcripts
For each video lesson, fetch:
```bash
# For each video_id (e.g., 10149001, 10149002, ...)
curl -s "https://platform-api.dlai.link/videos/{video_id}/caption.json" \
  -o "./downloads/deeplearning/{course-slug}/{lesson-number}-{lesson-title}.json"
```

### Step 3: Organize Output Directory
```
./downloads/deeplearning/{course-slug}/
├── 01-introduction.json        # Transcript for lesson 1
├── 02-lesson-title.json        # Transcript for lesson 2
├── ...
├── course-summary.md           # Full course summary (Chinese)
└── course-syllabus.md          # Course outline
```

### Step 4: Generate Per-Lesson Summaries
For each lesson transcript:
1. Parse the captions array
2. Group captions by topic/timestamp segments
3. Identify chapter markers (usually indicated by natural pauses or topic shifts)

### Step 5: Generate Course-Level Summary
Create `course-summary.md` with:
- Course overview and objectives
- Per-chapter summaries (in Chinese)
- Key concepts and patterns
- File manifest

## Transcript Parsing

### From caption.json
The captions array contains objects with:
- `startInSeconds`: Start time (integer)
- `endInSeconds`: End time (integer)
- `text`: The spoken text (English for English courses)

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

## Language Handling

- **Original Language**: English transcripts
- **Summary Language**: Chinese (as per user request)
- **Format**: Structured markdown with chapter divisions

## Summary Template for Course Videos

```markdown
# Course Title

**Course Source**: DeepLearning.AI
**Course URL**: https://learn.deeplearning.ai/courses/{course-slug}
**Instructors**: [Instructor Names]
**Partner**: [Partner Company if any]

---

## Course Overview
[2-3 sentences about the course purpose and what students will learn]

---

## Chapter X: [Lesson Title]
**Duration**: ~XX mins

### Content Summary
[Detailed summary of the lesson content in Chinese]

### Key Concepts
- [Concept 1]
- [Concept 2]

### Code Examples (if applicable)
[Any code patterns or implementations discussed]

---

## File Manifest

| File | Description |
|------|-------------|
| `01-introduction.json` | Lesson 1 transcript |
| ... | ... |
```

## Special Considerations

### Multi-Part Courses
Some courses span multiple modules (e.g., "Agent Memory" course with 7 video lessons):
1. Treat each video as a separate lesson
2. Generate individual lesson summaries
3. Create a master course summary

### Courses with Code Notebooks
DeepLearning.AI courses often include embedded code examples:
1. Note when the instructor mentions "code" or "demo"
2. Reference the code patterns without reproducing the full code
3. Focus on the architectural concepts

### VTT Subtitles
For time-exact reference, also fetch the VTT file:
```
https://video.deeplearning.ai/Oracle/{module}/{lesson}/subtitle/eng/sc-{project}-{module}-{lesson}-eng.vtt
```

## Error Handling

- **Network errors**: Retry with exponential backoff
- **Missing captions**: Try VTT URL as fallback
- **Long transcripts**: Process in chunks of ~500 captions per API call

## Quick Reference: API Pattern

```
Course URL: https://learn.deeplearning.ai/courses/{course-slug}/information
Caption API: https://platform-api.dlai.link/videos/{video_id}/caption.json
VTT URL: https://video.deeplearning.ai/{org}/{course}/{lesson}/subtitle/eng/{file}.vtt
```
