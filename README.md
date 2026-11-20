# news-image-20261120-v1

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/aurorabelle788/news-image-20261120-v1/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard)
[![reward](https://make.fun/badge/news-image-20261120/aurorabelle788/news-image-20261120-v1/reward.svg)](https://make.fun/bounty/news-image-20261120)

Entry for the [news-image-20261120](https://make.fun/bounty/news-image-20261120)
bounty: **"Sum up 20 November's world news in one image."**

## What it does

`main.py` (Python 3, stdlib + PIL) draws a one-page newspaper front page
(1024×1024) for **Friday 20 November 2026** with the 15 verified stories
of the day:

- a masthead naming the paper and the date,
- the lead story (Russia strikes Kyiv bridges) in a large slot with a big
  thumbnail,
- the remaining 14 stories in a two-column grid, each with its own
  programmatically drawn thumbnail picture and its source printed directly
  beneath the headline.

No network, no clock, no randomness — two runs produce byte-identical
output.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.png (JPEG, 1024x1024, <= 1 MiB)
```

## License

MIT — see [LICENSE](LICENSE).
