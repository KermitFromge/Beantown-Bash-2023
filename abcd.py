import requests
import finnhub
import pandas as pd

api_key = 'cgk5dkhr01qq3c3u0lf0cgk5dkhr01qq3c3u0lfg'

finnhub_client = finnhub.Client(api_key=api_key)

df = pd.read_csv("sp500.csv")

tickers = df['Symbol'].tolist()

def pull_sentiment(symbol):
    try:
            finnhub_client.stock_insider_sentiment(symbol, '2023-03-31', '2023-04-01')
    except Exception as e:  
        print(f"Error fetching data for {symbol}: {e}")
        return None, None


sentiments = []
for symbol in tickers[:5]:
    sentiments.append(pull_sentiment(symbol))

