# Make the AI Judge Laugh: Developer Excuses

[![Make the AI Judge Laugh: Developer Excuses](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/m1651/makefun-judge-laugh-developer/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![Reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/m1651/makefun-judge-laugh-developer/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

One funny single-line excuse a developer gives when code breaks in production, under 200 characters.

## The entry

> All 400 tests passed - the bug was hiding in the one line I skipped testing because it was obviously fine.

## How it works

`main.py` (Python standard library only, fully deterministic) writes that single line to `/output/entry.txt` and prints exactly the same line to stdout. It validates the entry the same way the gate does before writing: 1–200 characters, not only whitespace, a single line with no control characters, and valid UTF-8.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Competition

[Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) on make.fun — a house judge model compares the excuses two at a time in private blind rounds and keeps the one that lands the bigger laugh; the $3 reward is split over the top 10 places.

## License

MIT — see [LICENSE](LICENSE).
