# 📊 Hyperliquid Trader Behavior & Bitcoin Market Sentiment Analysis

## Overview

This project analyzes the relationship between Bitcoin market sentiment and trader behavior on Hyperliquid. By combining historical trading activity with the Bitcoin Fear & Greed Index, the study investigates how different market sentiment regimes influence trading performance, risk-taking behavior, position sizing, and profitability.

The objective is to uncover actionable insights that can support the development of more effective trading and risk-management strategies.

---

## Project Objectives

* Analyze trader performance across different market sentiment states.
* Measure the impact of Fear and Greed on profitability and execution efficiency.
* Identify behavioral patterns related to position sizing and risk exposure.
* Generate data-driven recommendations for algorithmic trading strategies.

---

## Repository Structure

```text
├── data/
│   ├── historical_data.csv
│   ├── fear_greed_index.csv
│   └── cleaned_merged_trading_data.csv

├── plots/
│   ├── trader_capital_sizing_trap.png
│   └── sentiment_profitability_analysis.png

├── preprocessing.py
├── analysis.py
├── visualizations.py
├── requirements.txt
└── README.md
```

---

## Dataset Description

### 1. Bitcoin Fear & Greed Index

Daily market sentiment classification categorized into:

* Extreme Fear
* Fear
* Neutral
* Greed
* Extreme Greed

### 2. Hyperliquid Historical Trading Data

Key fields include:

* Account
* Symbol
* Execution Price
* Position Size
* Side
* Timestamp
* Closed PnL
* Leverage
* Transaction Fees

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## Data Processing Pipeline

### Step 1: Data Cleaning

* Converted timestamps into standardized date format.
* Handled invalid or missing date values using `errors='coerce'`.
* Removed incomplete records where necessary.

### Step 2: Dataset Integration

* Aggregated trade records at the daily level.
* Merged Hyperliquid trade data with Fear & Greed sentiment data using date-based joins.

### Step 3: Feature Engineering

Created analytical metrics such as:

* Win/Loss Indicator
* Daily Profitability
* Average Position Size
* Trading Volume
* Protocol Fee Consumption

### Step 4: Exploratory Data Analysis

Analyzed:

* Profitability by sentiment regime
* Win rate by sentiment regime
* Position sizing behavior
* Trading volume distribution

---

# Executive Summary

A total of **211,218 trade executions** spanning **May 2023 to May 2025** were analyzed and cross-referenced against daily Bitcoin Fear & Greed Index values.

The analysis reveals a notable behavioral pattern:

* Traders achieve their highest win rate during **Extreme Greed** conditions.
* Traders deploy their largest average position sizes during **Fear** conditions.
* Larger position sizes during Fear do not necessarily translate into superior capital efficiency.
* Market sentiment appears strongly associated with both risk-taking behavior and trading performance.

---

# Performance Summary

| Market Sentiment | Total Trades | Aggregate Volume (USD) | Avg Position Size (USD) | Net Realized PnL (USD) | Win Rate | Fees Paid (USD) |
| ---------------- | ------------ | ---------------------- | ----------------------- | ---------------------- | -------- | --------------- |
| Extreme Fear     | 21,400       | $114,484,261.44        | $5,349.73               | $739,110.25            | 76.22%   | $23,888.63      |
| Fear             | 61,837       | $483,324,789.79        | $7,816.11               | $3,357,155.44          | 87.29%   | $92,456.95      |
| Neutral          | 37,686       | $180,242,063.08        | $4,782.73               | $1,292,920.68          | 82.39%   | $39,374.27      |
| Greed            | 50,303       | $288,582,494.72        | $5,736.88               | $2,150,129.27          | 76.89%   | $63,098.69      |
| Extreme Greed    | 39,992       | $124,465,164.57        | $3,112.25               | $2,715,171.31          | 89.17%   | $27,030.67      |

---

# Key Insights

## Insight 1: Position Sizing Peaks During Fear

The highest average position size was observed during **Fear** periods at **$7,816.11**, accompanied by the largest aggregate trading volume.

In contrast, traders significantly reduced position sizes during **Extreme Greed**, where the average position size fell to **$3,112.25**.

This suggests that traders tend to increase risk exposure during fearful market conditions, potentially attempting to capitalize on anticipated market reversals.

### Visualization

![Position Size Analysis](plots/trader_capital_sizing_trap.png)

---

## Insight 2: Trading Efficiency Peaks During Extreme Greed

Trades executed during **Extreme Greed** achieved the highest win rate of **89.17%**, generating approximately **$2.71 million** in realized profits.

Meanwhile, **Extreme Fear** recorded the lowest win rate at **76.22%**.

These findings suggest that bullish market environments may provide clearer directional trends and more favorable trading conditions.

### Visualization

![Profitability Analysis](plots/sentiment_profitability_analysis.png)

---

# Business Recommendations

## 1. Dynamic Sentiment-Based Position Sizing

Reduce position sizes during Fear and Extreme Fear conditions to limit downside exposure and improve capital preservation.

## 2. Momentum-Oriented Strategy Deployment

Given the strong performance observed during Extreme Greed periods, momentum-based trading strategies may outperform mean-reversion approaches in highly bullish environments.

## 3. Trading Fee Optimization

High-volume Fear periods generated the largest protocol fee expenditure. Implementing passive order execution mechanisms could reduce transaction costs and improve net profitability.

---

# Limitations

While the analysis provides valuable insights, several limitations should be considered:

* The study identifies correlations rather than causal relationships.
* Daily sentiment values may not fully capture intraday market psychology.
* Trader-level segmentation was not performed.
* External macroeconomic and geopolitical events were not incorporated into the analysis.
* Risk-adjusted performance metrics such as Sharpe Ratio were not evaluated.

---

# Future Improvements

Potential extensions of this project include:

* Trader segmentation analysis (Top vs Bottom Performers)
* Correlation and statistical significance testing
* Risk-adjusted return analysis
* Machine learning models for sentiment-driven trade prediction
* Time-series forecasting of trader profitability

---

# Conclusion

The study demonstrates a clear relationship between Bitcoin market sentiment and trader behavior on Hyperliquid. Traders tend to assume larger positions during Fear periods while achieving their highest execution efficiency during Extreme Greed conditions.

These findings highlight opportunities for sentiment-aware risk management, dynamic position sizing, and momentum-based strategy optimization in algorithmic trading systems.
