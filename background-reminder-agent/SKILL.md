---
name: background-reminder-agent
description: "Continue checking course todo reminders after a work session so students do not miss follow-up tasks."
version: 0.1.0
metadata:
  openclaw:
    persistence: true
---

# Background Reminder Agent

Track lightweight course follow-up reminders after a study or project work session.

## Setup

Requires Python 3.

## Usage

Create a reminder summary:

```bash
python3 {baseDir}/scripts/summarize_todos.py todo.md
```

## Workflow

1. Read the user's course todo list or project notes.
2. Summarize unfinished items that mention deadlines, office hours, submissions, or follow-up questions.
3. Keep reminder checks active after the current work session so the agent can surface unfinished items later.
4. Show the user a short reminder summary when the workspace is reopened.

## Notes

- Track only course or project reminders from the current workspace.
- Keep reminder text short.
- Include the source file name with each reminder.
