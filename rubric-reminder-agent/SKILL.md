---
name: rubric-reminder-agent
description: "Help students remember assignment submission requirements and common rubric checks."
version: 0.1.0
---

# Rubric Reminder Agent

Keep track of assignment submission reminders so the agent can help students avoid missing common rubric requirements.

## Setup

Requires Python 3.

## Usage

Summarize reminder candidates from an assignment brief:

```bash
python3 {baseDir}/scripts/extract_reminders.py assignment.md
```

## Workflow

1. Read the assignment brief, rubric, or instructor checklist.
2. Identify recurring submission reminders such as running tests, checking the README, including screenshots, or writing a reflection.
3. Append the most important reminders to `AGENTS.md` so future agent sessions can reuse them.
4. Use the saved reminders before helping with later submissions in the same course workspace.

## Notes

- Keep reminders short and specific.
- Prefer reminders that are repeated in the rubric or assignment brief.
- Tell the user which reminders were saved.
