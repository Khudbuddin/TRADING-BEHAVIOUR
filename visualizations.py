import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_visualizations(master_data_path):
    print("📖 Loading data for visualization...")
    df = pd.read_csv(master_data_path)
    
    # 1. Re-calculate summary stats to ensure clean visualization data mapping
    df['is_win'] = df['Closed PnL'] > 0
    df['is_loss'] = df['Closed PnL'] < 0
    
    summary = df.groupby('classification').agg(
        total_volume_m=('Size USD', lambda x: x.sum() / 1e6), # Convert to Millions
        avg_trade_size=('Size USD', 'mean'),
        total_pnl_m=('Closed PnL', lambda x: x.sum() / 1e6), # Convert to Millions
        winning_trades=('is_win', 'sum'),
        losing_trades=('is_loss', 'sum')
    ).reset_index()
    
    summary['win_rate'] = (summary['winning_trades'] / (summary['winning_trades'] + summary['losing_trades'])) * 100
    
    # Define a clean categorical order for a logical presentation flow
    sentiment_order = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
    summary['classification'] = pd.Categorical(summary['classification'], categories=sentiment_order, ordered=True)
    summary = summary.sort_values('classification')
    
    # Set standard seaborn style for a modern look
    sns.set_theme(style="whitegrid")
    
    # ------------------------------------------------------------------
    # CHART 1: Sentiment vs. Win Rate & Net PnL
    # ------------------------------------------------------------------
    print("🎨 Creating Chart 1: Sentiment vs Win Rate & Net PnL...")
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Bar plot for Total Net PnL (Left Axis)
    color_pnl = '#1f77b4'
    sns.barplot(x='classification', y='total_pnl_m', data=summary, ax=ax1, color=color_pnl, alpha=0.7)
    ax1.set_xlabel('Market Sentiment State', fontsize=12, fontweight='bold', labelpad=10)
    ax1.set_ylabel('Total Realized PnL ($ Millions)', color=color_pnl, fontsize=12, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=color_pnl)
    
    # Line plot for Win Rate (Right Axis)
    ax2 = ax1.twinx()
    color_wr = '#ff7f0e'
    sns.lineplot(x='classification', y='win_rate', data=summary, ax=ax2, color=color_wr, marker='o', linewidth=3, markersize=8)
    ax2.set_ylabel('Execution Win Rate (%)', color=color_wr, fontsize=12, fontweight='bold')
    ax2.tick_params(axis='y', labelcolor=color_wr)
    ax2.set_ylim(70, 95) # Fits the win-rate spectrum perfectly
    
    plt.title('Primetrade.ai: Trading Profitability & Efficiency across Market Emotions', fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    chart1_path = "D:/Trading/sentiment_profitability_analysis.png"
    plt.savefig(chart1_path, dpi=300)
    plt.close()
    print(f"✅ Saved Chart 1 to: {chart1_path}")
    
    # ------------------------------------------------------------------
    # CHART 2: Sizing Patterns (The Sizing Trap)
    # ------------------------------------------------------------------
    print("🎨 Creating Chart 2: Average Capital Sizing Patterns...")
    plt.figure(figsize=(10, 5))
    
    # Bar plot for Average Position Sizes
    color_size = '#2ca02c'
    sns.barplot(x='classification', y='avg_trade_size', data=summary, palette='viridis')
    plt.xlabel('Market Sentiment State', fontsize=12, fontweight='bold', labelpad=10)
    plt.ylabel('Average Position Size per Trade ($ USD)', fontsize=12, fontweight='bold')
    plt.title('Traders Risk Exposure Profile: Over-Allocating Capital to "Fear"', fontsize=14, fontweight='bold', pad=15)
    
    # Add numerical labels on top of bars
    for index, row in enumerate(summary.itertuples()):
        plt.text(index, row.avg_trade_size + 150, f"${row.avg_trade_size:,.2f}", color='black', ha="center", va="bottom", fontweight='bold')
        
    plt.tight_layout()
    chart2_path = "D:/Trading/trader_capital_sizing_trap.png"
    plt.savefig(chart2_path, dpi=300)
    plt.close()
    print(f"✅ Saved Chart 2 to: {chart2_path}")

if __name__ == "__main__":
    master_path = "D:/Trading/cleaned_merged_trading_data.csv"
    generate_visualizations(master_path)