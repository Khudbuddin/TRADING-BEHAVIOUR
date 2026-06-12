import pandas as pd

def run_sentiment_analysis(master_data_path):
    print("📖 Loading merged trading data...")
    df = pd.read_csv(master_data_path)
    
    # Create flags for winning and losing trades based on Closed PnL
    df['is_win'] = df['Closed PnL'] > 0
    df['is_loss'] = df['Closed PnL'] < 0
    
    print("🧮 Calculating behavioral metrics across sentiment tiers...")
    # Group by classification and run aggregations
    sentiment_summary = df.groupby('classification').agg(
        total_trades=('Order ID', 'count'),
        total_volume_usd=('Size USD', 'sum'),
        avg_trade_size_usd=('Size USD', 'mean'),
        total_net_pnl=('Closed PnL', 'sum'),
        winning_trades=('is_win', 'sum'),
        losing_trades=('is_loss', 'sum'),
        total_fees_paid=('Fee', 'sum')
    ).reset_index()
    
    # Calculate Win Rate Percentage dynamically based on closed outcome trades
    sentiment_summary['win_rate_%'] = (
        sentiment_summary['winning_trades'] / 
        (sentiment_summary['winning_trades'] + sentiment_summary['losing_trades'])
    ) * 100
    
    # Clean up display columns
    final_report = sentiment_summary[[
        'classification', 'total_trades', 'total_volume_usd', 
        'avg_trade_size_usd', 'total_net_pnl', 'win_rate_%', 'total_fees_paid'
    ]]
    
    print("\n=================== PRIMETRADE.AI SENTIMENT PERFORMANCE ANALYSIS ===================")
    print(final_report.to_string(index=False, formatters={
        'total_volume_usd': '{:,.2f}'.format,
        'avg_trade_size_usd': '{:,.2f}'.format,
        'total_net_pnl': '{:,.2f}'.format,
        'win_rate_%': '{:.2f}%'.format,
        'total_fees_paid': '{:,.2f}'.format
    }))
    print("====================================================================================")
    
    return final_report

if __name__ == "__main__":
    # Points to your newly generated master dataset
    master_path = "D:/Trading/cleaned.csv"
    run_sentiment_analysis(master_path)