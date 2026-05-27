#!/usr/bin/env python3
"""Compile all individual summaries into a single course markdown file."""
import os
import re

OUT_DIR = "P:/AI/my-agent-skills/downloads/deeplearning-ai/generative-ai-for-everyone/"

week1_videos = [
    (639,  "Welcome",                                       "~7min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/ieb07/welcome"),
    (640,  "How Generative AI works",                      "~8min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/dh0t1/how-generative-ai-works"),
    (641,  "LLMs as a thought partner",                    "~5min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/q5lai/llms-as-a-thought-partner"),
    (642,  "AI is a general purpose technology",           "~7min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/putz2/ai-is-a-general-purpose-technology"),
    (643,  "Writing",                                      "~5min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/yp2f3/writing"),
    (644,  "Reading",                                      "~8min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/t6fsb/reading"),
    (645,  "Chatting",                                     "~7min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/u12zr/chatting"),
    (646,  "What LLMs can and cannot do",                 "~11min", "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/a2sc1/what-llms-can-and-cannot-do"),
    (647,  "Tips for prompting",                          "~6min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/yc58w/tips-for-prompting"),
    (648,  "Image generation (Optional)",                 "~7min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/p0ssv/image-generation"),
]

week2_videos = [
    (649,  "Using Generative AI in Software Applications", "~6min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/ukffi/using-generative-ai-in-software-applications"),
    (651,  "Lifecycle of a Generative AI Project",        "~7min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/nakmz/lifecycle-of-a-generative-ai-project"),
    (652,  "Cost Intuition",                              "~6min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/gf9n9/cost-intuition"),
    (653,  "Retrieval Augmented Generation (RAG)",         "~8min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/k44k0/retrieval-augmented-generation-rag"),
    (654,  "Fine-tuning",                                  "~11min", "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/fpxbj/fine-tuning"),
    (655,  "Pretraining an LLM",                           "~3min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/mym30/pretraining-an-llm"),
    (656,  "Choosing a Model",                            "~6min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/okgpg/choosing-a-model"),
    (657,  "How LLMs Follow Instructions: Instruction Tuning and RLHF (Optional)", "~7min", "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/dtzpx/how-llms-follow-instructions-instruction-tuning-and-rlhf"),
    (658,  "Tool Use and Agents (Optional)",              "~6min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/eveia/tool-use-and-agents"),
]

week3_videos = [
    (659,  "Day-to-day Usage of Web UI LLMs",              "~3min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/ynkzr/day-to-day-usage-of-web-ui-llms"),
    (660,  "Task Analysis of Jobs",                        "~9min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/t5kxh/task-analysis-of-jobs"),
    (661,  "Additional Job Analysis Examples",            "~5min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/lzm2f/additional-job-analysis-examples"),
    (662,  "New Workflows and New Opportunities",         "~9min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/drnsm/new-workflows-and-new-opportunities"),
    (663,  "Teams to Build Generative AI Software",        "~5min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/uel68/teams-to-build-generative-ai-software"),
    (664,  "Automation Potential Across Sectors",         "~6min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/k1fzg/automation-potential-across-sectors"),
    (665,  "Concerns about AI",                           "~12min", "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/l1opx/concerns-about-ai"),
    (666,  "Artificial General Intelligence",              "~4min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/h4u3p/artificial-general-intelligence"),
    (667,  "Responsible AI",                               "~5min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/svk7y/responsible-ai"),
    (668,  "Course Summary",                              "~2min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/xy6rr/course-summary"),
    (669,  "Building a More Intelligent World",           "~3min",  "https://learn.deeplearning.ai/courses/generative-ai-for-everyone/lesson/h7s4i/building-a-more-intelligent-world"),
]

def extract_body(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    match = re.search(r'^## ', content, re.MULTILINE)
    if match:
        return content[match.start():]
    return content

def build_video_section(vid, title, duration, url):
    summary_file = os.path.join(OUT_DIR, "summary_%d.md" % vid)
    if not os.path.exists(summary_file):
        return "## %s\n\n*摘要文件不存在: summary_%d.md*\n\n---\n" % (title, vid)

    body = extract_body(summary_file)

    lines = [
        "## %s" % title,
        "",
        "**时长**: %s | **链接**: %s" % (duration, url),
        "",
        body,
        "",
        "---",
        "",
    ]
    return "\n".join(lines)

def build_week(title, videos):
    sections = ["# %s\n" % title]
    for vid, name, dur, url in videos:
        sections.append(build_video_section(vid, name, dur, url))
    return "\n".join(sections)

header_parts = [
    "# Generative AI for Everyone - 课程总结",
    "",
    "**课程来源**: DeepLearning.AI",
    "**课程链接**: https://learn.deeplearning.ai/courses/generative-ai-for-everyone",
    "**课程时长**: 约 3 周",
    "**授课教师**: Andrew Ng",
    "",
    "---",
    "",
]

footer = "\n---\n\n*此总结由 AI 自动生成，仅供学习参考使用*\n"

all_content = []
all_content.extend(header_parts)
all_content.append(build_week("Week 1: Introduction to Generative AI（生成式 AI 简介）", week1_videos))
all_content.append("")
all_content.append(build_week("Week 2: Generative AI Projects（生成式 AI 项目）", week2_videos))
all_content.append("")
all_content.append(build_week("Week 3: Generative AI in Business and Society（生成式 AI 与商业和社会）", week3_videos))
all_content.append(footer)

output_path = os.path.join(OUT_DIR, "course_summary.md")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(all_content))

print("Done. Output: %s" % output_path)
print("File size: %d bytes" % os.path.getsize(output_path))