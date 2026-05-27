#!/usr/bin/env python3
"""Batch generate summaries for all videos in the course."""
import subprocess
import os
import time

OUT_DIR = "P:/AI/my-agent-skills/downloads/deeplearning-ai/generative-ai-for-everyone/"
PYTHON = "C:/Users/chandlernie/AppData/Local/Programs/Python/Python313/python.exe"
SKILL_DIR = "P:/AI/my-agent-skills/.claude/skills/video-summarizer"

videos = [
    (639,  "Welcome",                                      "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/ieb07/welcome",                                     423),
    (640,  "How Generative AI works",                     "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/dh0t1/how-generative-ai-works",                        490),
    (641,  "LLMs as a thought partner",                   "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/q5lai/llms-as-a-thought-partner",                  286),
    (642,  "AI is a general purpose technology",          "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/putz2/ai-is-a-general-purpose-technology",         393),
    (643,  "Writing",                                      "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/yp2f3/writing",                                        323),
    (644,  "Reading",                                      "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/t6fsb/reading",                                       472),
    (645,  "Chatting",                                     "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/u12zr/chatting",                                      419),
    (646,  "What LLMs can and cannot do",                  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/a2sc1/what-llms-can-and-cannot-do",            660),
    (647,  "Tips for prompting",                           "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/yc58w/tips-for-prompting",                           387),
    (648,  "Image generation",                            "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/p0ssv/image-generation",                             397),
    (649,  "Using generative AI in software applications","https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/ukffi/using-generative-ai-in-software-applications", 347),
    (681,  "Trying generative AI code yourself (Week 2)","https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/qvgwx/trying-generative-ai-code-yourself",         183),
    (10134999, "Trying generative AI code yourself (L5)","https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/kt2pg/trying-generative-ai-code-yourself",         186),
    (651,  "Lifecycle of a generative AI project",         "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/nakmz/lifecycle-of-a-generative-ai-project",  427),
    (652,  "Cost intuition",                               "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/gf9n9/cost-intuition",                              349),
    (653,  "Retrieval Augmented Generation (RAG)",       "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/k44k0/retrieval-augmented-generation-rag",      462),
    (654,  "Fine-tuning",                                  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/fpxbj/fine-tuning",                               652),
    (655,  "Pretraining an LLM",                           "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/mym30/pretraining-an-llm",                           160),
    (656,  "Choosing a model",                             "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/okgpg/choosing-a-model",                             379),
    (657,  "How LLMs follow instructions: Instruction tuning and RLHF", "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/dtzpx/how-llms-follow-instructions-instruction-tuning-and-rlhf", 393),
    (658,  "Tool use and agents",                          "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/eveia/tool-use-and-agents",                        387),
    (659,  "Day-to-day usage of web UI LLMs",             "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/ynkzr/day-to-day-usage-of-web-ui-llms",        180),
    (660,  "Task analysis of jobs",                         "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/t5kxh/task-analysis-of-jobs",                   532),
    (661,  "Additional job analysis examples",            "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/lzm2f/additional-job-analysis-examples",        294),
    (662,  "New workflows and new opportunities",          "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/drnsm/new-workflows-and-new-opportunities",     550),
    (663,  "Teams to build generative AI software",        "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/uel68/teams-to-build-generative-ai-software",  299),
    (664,  "Automation potential across sectors",          "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/k1fzg/automation-potential-across-sectors",   366),
    (665,  "Concerns about AI",                            "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/l1opx/concerns-about-ai",                            724),
    (666,  "Artificial General Intelligence",              "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/h4u3p/artificial-general-intelligence",          235),
    (667,  "Responsible AI",                               "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/svk7y/responsible-ai",                             282),
    (668,  "Course Summary",                              "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/xy6rr/course-summary",                           119),
    (669,  "Building a more intelligent world",            "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/h7s4i/building-a-more-intelligent-world",     196),
]

# Filter out video_notebook types (681, 10134999 have no real transcript content)
video_list = [(vid, title, url, dur) for vid, title, url, dur in videos]

failed = []
for i, (vid, title, url, dur) in enumerate(video_list):
    t_file = os.path.join(OUT_DIR, f"transcript_{vid}.txt")
    s_file = os.path.join(OUT_DIR, f"summary_{vid}.md")

    if not os.path.exists(t_file):
        print(f"[{i+1}/{len(video_list)}] SKIP {vid} - no transcript")
        continue

    print(f"[{i+1}/{len(video_list)}] Processing {vid}: {title}")
    cmd = [
        PYTHON,
        os.path.join(SKILL_DIR, "scripts", "generate_summary.py"),
        t_file, s_file,
        "--title", title,
        "--url", url,
        "--duration", str(dur),
        "--pubdate", "2024-01-01"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"  -> OK: {s_file}")
    else:
        print(f"  -> ERR {vid}: {result.stderr[:200]}")
        failed.append(vid)
    time.sleep(2)  # avoid rate limiting

print(f"\nDone. Failed: {failed}")