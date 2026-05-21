# Agent-Specific Skill Fixtures

This directory contains small teaching fixtures for the ai system auditing activity. All three skills have student-facing value propositions. They promise rubric reminders, lower-friction maintenance, or course todo follow-up. The risks are not meant to look cartoonishly malicious. They are meant to show how a useful skill can change agent memory, invocation, or persistence.

Do not install or execute these skills. They are static artifacts for classroom inspection, scanner comparison, and audit-decision exercises.

## Fixture Set

Each skill is intentionally narrow. It exposes one primary scanner-detectable audit issue.

| Skill | Primary audit concept | Main question |
| --- | --- | --- |
| `rubric-reminder-agent/SKILL.md` | Agent behavior modification | Should a submission reminder skill append reminders to `SKILL.md`? |
| `approval-shortcut-agent/SKILL.md` | Always-on invocation | Should a routine maintenance skill be available on every agent session by default? |
| `background-reminder-agent/SKILL.md` | Persistent background behavior | Should a reminder skill keep checks active after the current work session? |
