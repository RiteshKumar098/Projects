# YouTube agent skills for Claude Code

Project-local installation of [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill), an MIT-licensed set of 11 YouTube creator skills. Source imported on 2026-11-13; source license is preserved in this folder.

## Use in Claude Code

From this repository, start or restart Claude Code and invoke a skill by name, for example:

- `/yt-script` — draft and score a video script.
- `/yt-package` — create/lint a title and thumbnail pairing.
- `/yt-edit` — make an edit decision list from a timestamped transcript.
- `/yt-comment` — triage comments and draft replies.
- `/yt-plan` — plan a realistic publishing week.
- `/yt-viral` — analyze a supplied collection of public video listings.
- `/yt-retention` — review a YouTube Studio retention export.
- `/yt-shorts` — find self-contained short-form moments in a transcript.
- `/yt-seo` — draft search-facing description and tags.
- `/yt-chapters` — draft validated chapter boundaries from a transcript.
- `/yt-audit` — audit a channel and identify one priority fix.

The complete skill sources and supporting scripts are in `.claude/skills/yt-*`. Python tools use Python 3 and the standard library only. Run them from the repository root using the paths in the skill instructions.

## Creator voice profile

Fill in `.claude/youtube/voice.md` with your audience, natural speaking style, words to avoid/use, claims you will not make, and format. The skills refer to this project-local file. Do not put credentials or private account data in it.

## Python tool examples

```bash
python3 .claude/skills/yt-script/hookscore.py --hook "one line"
python3 .claude/skills/yt-package/title.py --title "..." --thumb "..."
python3 .claude/skills/yt-edit/deadair.py transcript.srt
python3 .claude/skills/yt-chapters/chapters.py transcript.srt
python3 .claude/skills/yt-retention/retention.py retention.csv --duration 600
python3 .claude/skills/yt-viral/swipe.py collected.json --min 2.0
```

These tools analyze input and produce suggestions; they do not publish videos, edit media, log into YouTube, or access credentials. Review all generated material before using it. The hook scorer is heuristic, not a predictor; consult the upstream README for limitations.

## Upstream

- Source: https://github.com/Jakeschincariol/youtube-agent-skill
- MIT License: `.claude/skills/youtube-agent-skill/LICENSE`
- Skills source: https://github.com/Jakeschincariol/youtube-agent-skill/tree/main/skills
