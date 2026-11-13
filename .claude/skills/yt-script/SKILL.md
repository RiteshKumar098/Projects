---
name: yt-script
description: >-
  Write a YouTube video script from a raw idea - hook options off 21
  formulas, scored, then the full spoken script with the retention beats
  marked. Use whenever the user wants a video script, a hook, an opening
  line, "what should I say", "write my next video", or is about to record
  and does not have the first fifteen seconds yet.
---

# yt-script

One idea into a script somebody finishes.

Use the hook scoring tool; do not eyeball the hook.

```bash
python3 .claude/skills/yt-script/hookscore.py hooks.txt
python3 .claude/skills/yt-script/hookscore.py --hook "one line"
```

## Before you write

1. Read `.claude/youtube/voice.md` if it exists. If it does not, ask for three of the creator's own videos and infer the voice before writing.
2. Never invent a number, a result or a source. If a figure would strengthen it and you do not have one, ask for it or write the line without it.

## The shape

**The first 15 seconds is the whole job.** It does three things or the video leaks: confirm the click the title promised, open a question the viewer cannot close, and prove the payoff exists.

1. **Hook.** Write five options against the 21 formulas in `hooks.json`, run them through the scorer, keep the top two, and show both with scores. Never hand over one hook.
2. **The turn** (0:15-0:45). Say what the video is going to do in one sentence, and start doing it. No channel intro, no "before we get started", no subscribe pitch.
3. **The body.** One idea per beat. Mark each beat with what is ON SCREEN, not just what is said.
4. **The payoff.** Deliver the thing the hook promised, explicitly.
5. **The close.** One ask. Not three.

## What to hand back

- The two best hooks with their scored panels.
- The script, beat by beat, with `[ON SCREEN: ...]` on every beat.
- The runtime estimate at 150 words per minute.
- One line naming which formula the winning hook used and why it fits this idea.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user copies and the last line asks: **ship it, or change it?**
