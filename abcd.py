import pandas as pd
import time 
import finnhub

api_key = 'cgk5dkhr01qq3c3u0lf0cgk5dkhr01qq3c3u0lfg'

finnhub_client = finnhub.Client(api_key=api_key)

df = pd.read_csv("sp500.csv")

tickers = df['Symbol'].tolist()

def pull_sentiment(symbol):
    sentiment_data = finnhub_client.stock_insider_sentiment(symbol, '2023-03-31', '2023-04-01')
    if sentiment_data and 'data' in sentiment_data and len(sentiment_data['data']) > 0:
        return [sentiment_data['data'][0].get('symbol'), sentiment_data['data'][0].get('mspr') ] 
    else:
        return None

sentiment_values = []
for symbol in tickers:
    mspr = pull_sentiment(symbol)
    if mspr is not None:
        sentiment_values.append(mspr)
    else:
        print(f"Failed to get mspr for {symbol}")

    time.sleep(1)

print(sentiment_values)

