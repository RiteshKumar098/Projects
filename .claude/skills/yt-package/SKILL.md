---
name: yt-package
description: >-
  Write and lint the title and thumbnail for a YouTube video as one pairing,
  checking truncation, duplication and vagueness before publish. Use for
  "title ideas", "what should I call this", "thumbnail text", "my CTR is
  bad", packaging, or any request to rename or repackage an existing video.
---

# yt-package

The title and the thumbnail are ONE unit. Writing them separately is why most packaging fails: the thumbnail repeats the title, and half the click surface says the same thing twice.

```bash
python3 .claude/skills/yt-package/title.py --title "..." --thumb "AI RAN IT"
python3 .claude/skills/yt-package/title.py titles.txt
```

## Before you write

1. Read `.claude/youtube/voice.md` if it exists. If it does not, ask for three of the creator's own videos and infer the voice before writing.
2. Never invent a number, a result or a source. If a figure would strengthen it and you do not have one, ask for it or write the line without it.

## Rules the tool enforces, and why

- **60 characters** is where desktop search truncates, **40** is a mobile home feed.
- The thumbnail should not repeat the title; use different words for the same promise.
- Three words maximum on the thumbnail is a useful guideline at feed size.
- A number, a name or a date often beats an unsupported adjective.
- Two all-caps words is the ceiling before a title reads as spam.

## Write ten, keep two

Generate ten titles, run them all through `title.py`, show the user the top three with scores and specific issues. For the winner, write a thumbnail brief.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user copies and the last line asks: **ship it, or change it?**
