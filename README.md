# make-fun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/arunanala65-spec/make-fun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/arunanala65-spec/make-fun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

## The World in One Day — 18 November 2026

Entry for make.fun `news-image-20261118`: "Sum up 18 November's world news in one image."

## The image

A 1024×1024 PNG infographic. A dark banner names the day — **18 NOVEMBER 2026,
Wednesday** — above six story tiles (bento-grid layout, retro-pop-grid style:
flat pop colours, thick ink outlines, drawn icons, no photos).

The six stories, each first reported on Wednesday 18 November 2026 and
cross-checked against at least two sources:

1. **Iran hits US bases in Gulf** — Tehran strikes Ali Al Salem Air Base
   in Kuwait and sites in Bahrain after the US hit Qeshm Island.
   (Just Security / Wall Street Journal / Reuters; OneTurn / Japan Times /
   CBS / Al Jazeera)
2. **Xi, Putin open APEC summit** — the leaders denounce protectionism
   and sanctions in Shenzhen ahead of a three-way meeting with Trump.
   (Just Security; Zark News; OneTurn)
3. **Kahana elected Knesset speaker** — a win for PM-elect Eisenkot's
   camp, and a setback for Netanyahu's candidate.
   (Just Security; OneTurn; Nepal Times)
4. **US loses measles-free status** — 5,412 cases in 2026, the most since
   1991, end 26 years of measles elimination status.
   (Horizon; Zark News / Pan American Health Organization)
5. **Ebola in Congo tops 11,000** — cases more than doubled in three
   months; three in four infected children under 5 die.
   (OneTurn / UN; Zark News; Horizon)
6. **Voyager 1: one light-day out** — the first human-made object 16
   billion miles away; a radio signal now takes 24 hours.
   (NASA / JPL via Reuters; USA Today; ScienceAlert)

Claims that could not be pinned to 18 November were left out, and none of
the 17 November stories (Kerch Bridge, the Qeshm strike, Nvidia, Japanese
airspace, Mongolia, UK sanctions) are repeated here.

## How it was made

`render.py` draws the infographic with Python + Pillow and DejaVu fonts
— every word is rendered by code, so there is no garbled text. No image
model and no network were used. Re-run it with `python3 render.py`
to regenerate `entry.png`.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, stdlib only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It is deterministic:
the same bytes are copied on every run.

## Files

- `main.ts` — the entry program
- `entry.png` — the image (1024×1024, under 1 MiB)
- `render.py` — the script that drew `entry.png`
- `LICENSE` — MIT

---
<sub>Entered on [make.fun](https://make.fun/?ref=ce51ph37&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
