# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This repository stores custom Claude Code skills. Skills are folders containing instructions that teach Claude how to complete specific tasks in a repeatable way.

## Adding New Skills

Create a new folder with your skill name, then add a `SKILL.md` file inside:

```
my-skill/
└── SKILL.md
```

### SKILL.md Format

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

The frontmatter requires:
- `name` - Unique identifier (lowercase, hyphens for spaces)
- `description` - What the skill does and when Claude should use it

## Reference

- Skills specification: https://agentskills.io/specification
- Official skills repository with examples: `P:/AI/skills/`
- Skill template: `P:/AI/skills/template/SKILL.md`

## Using Skills in Claude Code

After adding skills to this repository, you can use them by:
1. Invoking `/skill your-skill-name` in Claude Code
2. Or asking Claude to use a specific skill by name

## Related Resources

- Course materials: `P:/AI/sc-agent-skills-files/`
- What are skills: https://support.claude.com/en/articles/12512176-what-are-skills
- Creating custom skills: https://support.claude.com/en/articles/12512198-creating-custom-skills
