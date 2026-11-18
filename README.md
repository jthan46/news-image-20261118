# news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/jthan46/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/jthan46/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image sums up Wednesday 18 November 2026: the APEC summit opens in Shenzhen, the U.S. strikes an Iranian missile site, Ukraine hits the Crimea bridge, America loses measles-free status, a Category 5 cyclone and Congo's Ebola milestone.

The entry is a single front page — "The World in One Image" — dated Wednesday 18 November 2026 in a banner no reader can miss. Six panels cover the day's most consequential stories across diplomacy, conflict, war, public health and weather, each with its own editorial illustration (in `assets/`), a short factual headline and a one-line explainer, composed programmatically by `tools/compose.py` so every word is crisp. `main.ts` simply copies the finished `entry.png` to the output directory, byte for byte, every run.

## The stories

- **APEC summit opens in Shenzhen** — Xi Jinping opened the APEC summit in Shenzhen, urging AI partnership and free trade, while Donald Trump met Quad partners in Manila ahead of a first U.S.–China–Russia trilateral. (FeedCast Daily Brief, reporting Africanews and Rio Times Online)
- **U.S. strikes an Iranian missile site; Iran answers with drones** — U.S. jets struck a Revolutionary Guard missile launch site on Qeshm Island, and Iran fired drones at Bahrain and Kuwait; Bahrain said it intercepted attacks on the country hosting the U.S. Fifth Fleet. (Reuters; CBS News, Al Jazeera and Japan Times via One Turn)
- **Ukraine hits the Crimea bridge again** — Ukraine struck the Kerch Bridge to Crimea for a second day; open-source reports said a road span fell into the strait and Russia closed road traffic. (One Turn)
- **U.S. measles-free status ends** — The Pan American Health Organization announced measles is no longer eliminated in the United States, ending a 26-year status, with more than 5,400 cases reported in 2026. (FeedCast Daily Brief, reporting PAHO and CNA)
- **Category 5 Cyclone Xavier batters the Northern Cook Islands** — Xavier reached the Northern Cook Islands on 18 November with sustained winds of about 220 km/h and gusts up to 315 km/h; shelters were activated. (RNZ; Fiji Meteorological Service and MetService bulletins)
- **Ebola passes 11,000 cases in DR Congo** — The WHO Director-General said the Bundibugyo Ebola outbreak has more than doubled in three months, passing 11,000 cases and 5,400 deaths across eight provinces. (UN News)

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=bjydwhj1&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
