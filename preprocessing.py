import pandas as pd
import os

def load_and_preprocess_data(historical_path, sentiment_path):
    print("🔄 Loading datasets...")
    # Load the raw CSV files
    historical_df = pd.read_csv("D:/Trading/historical_data.csv")
    sentiment_df = pd.read_csv("D:/Trading/fear_greed_index.csv")
    
    print(f"📊 Initial rows - Historical: {historical_df.shape[0]}, Sentiment: {sentiment_df.shape[0]}")
    
    # Step 1: Standardize Dates in Sentiment Dataset (YYYY-MM-DD)
    sentiment_df['clean_date'] = pd.to_datetime(sentiment_df['date']).dt.date
    
    # Step 2: Convert and Standardize Granular IST Timestamps in Historical Dataset
    # Using errors='coerce' turns invalid formats into NaT instead of crashing your script
    historical_df['clean_date'] = pd.to_datetime(
        historical_df['Timestamp IST'], 
        format='%d-%m-%Y %H:%M', 
        errors='coerce'
    ).dt.date
    
    # Step 3: Remove rows where timestamps couldn't be parsed
    initial_hist_count = len(historical_df)
    historical_df = historical_df.dropna(subset=['clean_date'])
    dropped_rows = initial_hist_count - len(historical_df)
    if dropped_rows > 0:
        print(f"⚠️ Dropped {dropped_rows} rows from historical data due to unparseable timestamps.")
    
    # Step 4: Merge the datasets on the synchronized 'clean_date' column
    print("🤝 Merging datasets on daily unified dates...")
    # We only bring over the sentiment score ('value') and 'classification' to keep things clean
    merged_df = pd.merge(
        historical_df, 
        sentiment_df[['clean_date', 'value', 'classification']], 
        on='clean_date', 
        how='inner'
    )
    
    print(f"✅ Preprocessing Complete! Merged dataset shape: {merged_df.shape}")
    return merged_df

# Run the pipeline (assuming files are in your current directory)
if __name__ == "__main__":
    hist_file = 'historical_data.csv'
    sentiment_file = 'fear_greed_index.csv'
    
    if os.path.exists(hist_file) and os.path.exists(sentiment_file):
        df_cleaned = load_and_preprocess_data(hist_file, sentiment_file)
        
        # Save to a new csv file so we can instantly load it for Phase 2 & 3
        df_cleaned.to_csv('cleaned.csv', index=False)
        print("💾 Processed dataset saved as 'cleaned.csv'")
    else:
        print("❌ Error: Please ensure both CSV files are in the working directory.")