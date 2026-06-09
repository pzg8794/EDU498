# Gmail Search Log

## Account

Gmail connector profile was checked before collecting records.

- Name: Piter Garcia
- Email: `pzg8794@g.rit.edu`
- Purpose: collect email evidence for the EDU498 "Literacy as Power" assignment, focused on neurodivergence, accessibility, and communication injustice.

## Main Queries

Primary professor/course search:

```text
osier -in:spam -in:trash
```

Focused accessibility/course search:

```text
(osier OR mvoscl@rit.edu) (accommodation OR DSO OR health OR "Flex Plan" OR hand-written OR handwritten OR "Unable to Attend" OR "peer eval" OR syllabus OR verbally OR "first ten" OR "Google documents" OR "group dynamics") after:2026/01/01 before:2026/06/10 -in:spam -in:trash
```

Advisor-support search:

```text
(Megan OR Lehman OR mdlsse OR advisor) (Osier OR BIOL550 OR BIOL-550 OR DSO OR accommodation OR peer evaluation OR inaccessible OR neurodivergent OR Flex) after:2026/01/01 before:2026/06/10 -in:spam -in:trash
```

Focused Megan/advisor search:

```text
(from:melics@rit.edu OR to:melics@rit.edu OR "Megan Lehman") (Osier OR BIOL550 OR BIOL-550 OR bioinformatics OR DSO OR accommodation OR Ombuds OR formal OR withdraw OR withdrawal OR drop OR dropping) after:2026/01/01 before:2026/06/10 -in:spam -in:trash
```

## Located Thread Clusters

| Cluster | Representative Gmail IDs | Why it matters |
|---|---|---|
| Early accommodation and health context | `19bd52d570313c82`, `19bbe0d93bd467ef`, `19bb1db5f68d5e0d` | Establishes that health, ADHD, and accommodations were communicated early rather than after the conflict escalated. |
| Health-related absences and Flex Plan tension | `19d0567c99c1018d`, `19d3ce2eb1832a00`, `19dba444d2c535ca` | Shows absences framed through health/DSO context, plus later concern about the Flex Plan missed-class limit. |
| Handwritten/peer-evaluation issue | `19d06d7ff03e6511`, `19d06d4e6b7d5bb8`, `19d300b208d83530` | Central access issue: the student reported that the handwritten requirement was not in written instructions or transcripts. |
| Weekly report and "first ten" ambiguity | `19c9bf16182ba2d1`, `19dd22e7765d5dd6` | Shows confusion over grading policy and whether "10 out of 12" meant first ten or best ten. |
| Course communication and assignment-submission confusion | `19c521efa7707b7c`, `19c442184a942740`, `19c336b748a80ac5`, `19c3292f17abca5c`, `19c2146a7ad494fb` | Useful for assignment-literacy analysis: formats, verbal announcements, Google Docs/flat files, group dynamics, and multiple communication channels. |
| Advisor support and escalation navigation | `19d2f2b7d473fe9e`, `19d304632b34a926`, `19d3fe2bb99ca8bf` | Megan Lehman helps frame the issue as accessibility/systemic and suggests formal follow-up and Ombuds. |
| Team meeting summaries with Slack references | `19d227783c3c04c2`, `19d46c84bb009e60` | Zoom-generated summaries of team meetings mention Slack updates, professor-related concerns, dropping/continuing decisions, and team communication patterns. |

## Notes

- The Gmail connector did not provide a raw `.eml` export function in this workflow. This folder therefore preserves a curated local index with Gmail message/thread IDs, Gmail display links in the detailed indexes, source summaries, and selected evidence excerpts.
- For any formal use beyond the EDU498 assignment, reopen the Gmail messages directly and verify quotations against the original email.
