---
name: yt-edit
description: >-
  Turn a raw recording's transcript into an edit decision list - dead air,
  filler cues and retakes, with timecodes. Use for "edit this", "cut the
  dead space", "tighten this video", "I rambled", or any request to shorten
  footage from a transcript.
---

# yt-edit

An edit decision list from a timestamped transcript. It prints the cuts. You apply them.

```bash
python3 .claude/skills/yt-edit/deadair.py transcript.srt
python3 .claude/skills/yt-edit/deadair.py transcript.srt --floor 0.35 --json
```

No transcript yet? Ask for one, or produce one first - `whisper`, `faster-whisper`, or the caption track YouTube generates on an unlisted upload all work. Do not guess at timings.

## What it finds

- **DEAD** - gaps longer than the floor, trimmed from the middle so both sides keep a breath.
- **FILLER** - cues that are nothing but "um", "so yeah", "basically".
- **REPEAT** - a sentence restarted, compared against the last cue that was actually speech.

## What it will not do

It does not touch media. It has no opinion about your B-roll. Check the report against footage before trusting the estimated runtime.

## The gate

Nothing here edits or publishes. This skill writes and you apply. Every output ends in a block the user copies and the last line asks: **ship it, or change it?**
