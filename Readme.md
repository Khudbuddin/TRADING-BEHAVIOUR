# 📊 Hyperliquid Trader Behavior & Bitcoin Market Sentiment Analysis

An end-to-end data science study analyzing how macro psychological market regimes dictate decentralized exchange (DEX) trader risk parameters, efficiency, and net profitability capture on Hyperliquid.

---

## 📁 Repository Structure
```text
├── data/
│   ├── historical_data.csv                 # Raw execution log data (Excl. from Git)
│   ├── fear_greed_index.csv                # Raw daily sentiment log (Excl. from Git)
│   └── cleaned_merged_trading_data.csv    # Consolidated master dataset (Excl. from Git)
├── plots/
│   ├── trader_capital_sizing_trap.png      # Chart: Average Position Sizing across Sentiment
│   └── sentiment_profitability_analysis.png# Chart: Net PnL vs Execution Win Rate
├── preprocessing.py                 # Data extraction, alignment, and cleaning pipeline
├── analysis.py                      # Vectorized metrics and performance analytics engine
├── visualizations.py                # Seaborn visualization script
└── README.md                               # Comprehensive project report & documentation

### 1. Executive Summary
An analysis of $211,218$ discrete trade execution logs spanning a 2-year window (May 2023 – May 2025) was cross-referenced against daily Bitcoin Fear & Greed Index data points. The objective was to determine whether macro psychological market states dictate decentralized exchange (DEX) trader risk parameters, efficiency, and overall capture of Net Realized Profit ($PnL$).

The data reveals a stark, counter-intuitive behavioral paradox: while traders exhibit their highest execution accuracy ($89.17\%$ win rate) during macro Extreme Greed environments, they systematically over-allocate capital and take their highest risk exposure via large position sizes during periods of Fear, significantly deteriorating capital efficiency.

---

### 2. Consolidated Performance Metric Matrix
To normalize and analyze the execution patterns, raw granular transactional times (Timestamp IST) were unified into daily standard dates (YYYY-MM-DD) and inner-joined with daily sentiment brackets.

| Market Sentiment State | Total Executed Trades | Aggregate Volume (USD) | Average Position Size (USD) | Total Net Realized PnL (USD) | Execution Win Rate | Total Protocol Fees Paid (USD) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Extreme Fear** | 21,400 | \$114,484,261.44 | \$5,349.73 | \$739,110.25 | $76.22\%$ | \$23,888.63 |
| **Fear** | 61,837 | \$483,324,789.79 | \$7,816.11 | \$3,357,155.44 | $87.29\%$ | \$92,456.95 |
| **Neutral** | 37,686 | \$180,242,063.08 | \$4,782.73 | \$1,292,920.68 | $82.39\%$ | \$39,374.27 |
| **Greed** | 50,303 | \$288,582,494.72 | \$5,736.88 | \$2,150,129.27 | $76.89\%$ | \$63,098.69 |
| **Extreme Greed** | 39,992 | \$124,465,164.57 | \$3,112.25 | \$2,715,171.31 | $89.17\%$ | \$27,030.67 |

---

### 3. Core Analytical Discoveries & Hidden Patterns

#### 💡 Alpha Insight A: The Sizing Distortion Trap (Risk-Reversal Bias)
The most significant operational pattern discovered centers around how traders scale position sizes relative to emotional environments. In standard **Fear** cycles, the average position size peaks drastically at \$7,816.11 per trade—resulting in a massive aggregate volume cluster of \$483.32 Million. Conversely, when the market transitions into **Extreme Greed**, traders dramatically scale down their risk profiles, lowering their average position size by over $60\%$ down to \$3,112.25.

<p align="center">
  <img src="trader_capital_sizing_trap.png" alt="Traders Risk Exposure Profile" width="600"/>
</p>

*Psychological Inference:* Traders frequently suffer from over-confidence when catching down-trending prices ("buying the dip" aggressively), scaling up their positions prematurely during Fear. In contrast, they display clear profit-taking hesitation and exposure minimization during powerful macro uptrends (Extreme Greed).

#### 💡 Alpha Insight B: The Extreme Greed Efficiency Miracle
Conventional trading wisdom suggests that retail traders lose money by FOMO-ing during periods of high greed. However, the transactional data on Hyperliquid reveals that trades executed during **Extreme Greed** achieve a stellar $89.17\%$ win rate, generating \$2.71 Million in realized profits on a modest volume of \$124.46 Million.

Conversely, when the market drops into **Extreme Fear**, execution accuracy breaks down completely, hitting a baseline floor of $76.22\%$ win rate. This highlights a severe breakdown in risk management or heavy cascade liquidation events during deep panic conditions.

<p align="center">
  <img src="sentiment_profitability_analysis.png" alt="Trading Profitability & Efficiency" width="600"/>
</p>

---

### 4. Data Science & Engineering Methodology
To execute this analysis cleanly, an end-to-end Python preprocessing and analytics pipeline was deployed:
1. **Datetime Mapping:** Standardized non-uniform Indian Standard Time string stamps (`%d-%m-%Y %H:%M`) within the historical transaction data into a stripped `datetime.date` index.
2. **Data Integrity Filtration:** Missing dates or unparseable timestamps were handled via coerced transformations (`errors='coerce'`) to insulate the inner merge from dropping critical alpha features. 
3. **Vectorized Metrics:** Created binary logical arrays (`is_win` / `is_loss`) to isolate execution efficiency dynamically from non-zero closing transaction rows.
4. **Data Visualizations:** Built and exported dual-axis matplotlib/seaborn plots to evaluate the visual intersections of sentiment value fluctuations against underlying wallet metrics.

---

### 5. Algorithmic Recommendations for Smarter Trading Strategies
Based on the empirical evidence extracted from the Hyperliquid records, Primetrade.ai can exploit these system inefficiencies to build robust trading models:

* **Implement Dynamic, Sentiment-Based Position Sizing:** Rather than letting human traders scale up size into down-trends, the automated system should force position sizes to scale *down* dynamically when the daily index reads "Fear" or "Extreme Fear" to preserve capital.
* **Automate Trend-Continuation Momentum Modules:** Given the high efficiency ($89.17\%$ win rate) during Extreme Greed, algorithm configurations should optimize for short-horizon breakout and momentum tracking strategies. Momentum plays during high sentiment states capture high-probability continuation moves far better than mean-reversion attempts during heavy sell-offs.
* **Adaptive Fee Optimization:** With over \$245k spent across the system in protocol trading fees, execution modules should deploy passive limit-order strategies (maker instead of taker executions) during high-volume Fear clusters to severely reduce transaction drag.