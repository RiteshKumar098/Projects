---
name: yt-viral
description: >-
  Find what is actually working in the user's niche on YouTube and rank it
  by how far each video beat its own channel, then name the formula. Use for
  "what's working right now", "find viral videos in my niche", "why did this
  blow up", competitor research, or a swipe file.
---

# yt-viral

Raw view counts rank channel size, not ideas. This ranks by **multiple over each channel's own median**, which is the only version of the question that is about the video.

```bash
python3 .claude/skills/yt-viral/swipe.py collected.json --min 2.0
```

## Collecting the input

You need at least **four videos per channel** or a median means nothing, and the tool will skip the channel and tell you. Collect public listings only, never a logged-in session or account credentials.

```json
[{"channel":"...","title":"...","views":412000,"url":"...","duration":613}]
```

## Reading the output

The multiple is the signal. The formula line is a judgement about the title, matched against `.claude/skills/yt-script/hooks.json` - it is not a claim about why the video worked, and say so when presenting it.

Hand back the top five with their multiples, the formula each used, and the ONE structural thing they share; then say which the user could make this week.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user copies and the last line asks: **ship it, or change it?**
