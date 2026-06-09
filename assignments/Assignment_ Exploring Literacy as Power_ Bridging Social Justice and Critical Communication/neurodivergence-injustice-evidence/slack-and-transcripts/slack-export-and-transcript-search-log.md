# Slack Export and Transcript Search Log

## Search Goal

The user remembered downloading Slack records and asked for them to be placed in the EDU498 assignment evidence folder. The search therefore looked for:

- Slack export archives or folders.
- Slack export marker files such as `channels.json`, `users.json`, `dms.json`, `mpims.json`, and `integration_logs.json`.
- BIOL550 local records that mention Slack, team communication, professor-related issues, accommodations, peer evaluation, or neurodivergence.

## Search Scope

Local paths searched:

- `/Users/pitergarcia/Downloads`
- `/Users/pitergarcia/Desktop`
- `/Users/pitergarcia/Documents`
- `/Users/pitergarcia/DataScience`
- `/Users/pitergarcia/Library/CloudStorage`

Focused content search:

```text
rg -n -i "slack|rit\.org\.slack\.com|aaaas6tkzywllbfoqhw4zry7vm|osier|peer evaluation|handwritten|hand-written|accommodation|neurodivergent|vague instructions|professor" /Users/pitergarcia/DataScience/Semester5/BIOL550
```

## Result

No verified Slack export archive or standard Slack export folder was located during this pass.

The final marker search returned only unrelated files:

- `/Users/pitergarcia/Library/CloudStorage/GoogleDrive-garciapiterz@gmail.com/.tmp/5802/Portafolio/Projects-Code/opc-python/BestVacation/Django-1.5.5.tar/dist/Django-1.5.5/Django-1.5.5/tests/regressiontests/admin_custom_urls/fixtures/users.json`
- `/Users/pitergarcia/Library/CloudStorage/GoogleDrive-garciapiterz@gmail.com/.tmp/5802/Portafolio/Projects-Code/opc-python/BestVacation/django-facebook-5.2.10/django-facebook-5.2.10/django_facebook/fixtures/users.json`
- `/Users/pitergarcia/Library/CloudStorage/GoogleDrive-garciapiterz@gmail.com/.tmp/5802/Portafolio/Projects-Code/opc-python/BestVacation/django-facebook-5.2.10/django-facebook-5.2.10/build/lib/django_facebook/fixtures/users.json`
- `/Users/pitergarcia/Library/CloudStorage/GoogleDrive-garciapiterz@gmail.com/Other computers/My MacBook Pro/Downloads/Slack-4.29.149-macOS.dmg`
- `/Users/pitergarcia/Library/CloudStorage/GoogleDrive-garciapiterz@gmail.com/.shortcut-targets-by-id/1pY_fQ54nHKvFABNRGYAr5bQ3su_tUDAi/DataScience/Semester2/DSCI644/Group2/data_lake/raw_data/requests_requests-oauthlib_slack.py`
- `/Users/pitergarcia/Library/CloudStorage/GoogleDrive-garciapiterz@gmail.com/.tmp/5802/Portafolio/Work-Projects/opw-trueinteraction/Slack.lnk`
- `/Users/pitergarcia/Library/CloudStorage/GoogleDrive-garciapiterz@gmail.com/.tmp/5802/Portafolio/Work-Projects/opw-trueinteraction/SlackSetup.exe`

The search did locate BIOL550 transcripts and email-derived Zoom summaries that directly reference Slack and team communication. Those transcript records were copied into this folder so the assignment has durable local evidence even without the separate Slack export.

## Copied Transcript Records

| Copied file | Original local source | Why it was copied |
|---|---|---|
| `2026-03-24-student-project-meeting-professor-issues-transcript.txt` | `/Users/pitergarcia/DataScience/Semester5/BIOL550/transcripts/2026-03-24 Student Project Meeting_ Addressing Professor-Related Issues and Planning Next Steps-transcript.txt` | Strongest team record: professor-related issues, vague requirements, handwritten requirement, advisor/DSO mention, neurodivergence/accommodation framing, Slack updates, and peer validation. |
| `2026-03-25-peer-evaluations-feedback-transcript.txt` | `/Users/pitergarcia/DataScience/Semester5/BIOL550/transcripts/2026-03-25 Lecture_ Peer Evaluations and Feedback Mechanisms-transcript.txt` | Captures class discussion about peer evaluation, handwriting, feedback mechanisms, and access concerns. |
| `2026-03-31-team-meeting-course-participation-transcript.txt` | `/Users/pitergarcia/DataScience/Semester5/BIOL550/transcripts/2026-03-31 Team Meeting_ RNA-seq NovaSeq 6000 Analysis, Presentation Prep, and Course Participation Decision-transcript.txt` | Shows later team conversation after support-system contact, including the student's decision-making about continuing in the course and using other faculty support. |
| `2026-04-07-team-conflicts-paper-structure-data-pipeline-transcript.txt` | `/Users/pitergarcia/DataScience/Semester5/BIOL550/transcripts/2026-04-07 Weekly Meeting_ Team Conflicts, Paper Structure, and Data Pipeline-transcript.txt` | Captures Slack/team conflict, documentation overload, AI/transcript notes, Google Drive, unclear expectations, and peer communication behavior. |

## Gmail / Zoom Records That Mention Slack

| Date | Gmail ID | Evidence value |
|---|---|---|
| 2026-03-24 | `19d227783c3c04c2` | Zoom summary says the team discussed professor conduct, accommodations for neurodivergence, and project next steps; it also says Piter would share updates/results in Slack. |
| 2026-03-31 | `19d46c84bb009e60` | Zoom summary says the team discussed course-related challenges, possible course withdrawal/continuation, professor communication, and transition to other faculty support. |
| 2026-02 project coordination | `19c2146a7ad494fb` | Email thread references a Slack channel/task tracker as part of the team's coordination infrastructure. |

## Important Boundary

These copied transcripts are not a verified Slack export. They are local records that discuss Slack and team communication. If the actual Slack export is later found, add it under this folder and update this log with:

- original source path,
- copied target path,
- channels included,
- date range,
- whether direct messages/private channels are present,
- privacy/redaction concerns.

## Assignment Use

The Slack/transcript evidence supports a communication-literacy argument:

- Slack can be an access tool when it creates durable written records, task memory, and asynchronous participation.
- Slack can also intensify harm when messages are misread, indirect, or used without shared norms.
- Neurodivergent access requires more than "use a tool"; it requires explicit norms for how the tool will hold requirements, decisions, feedback, conflict, and responsibility.
