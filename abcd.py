import requests
import pandas as pd
import finnhub



api_key = 'cgk5dkhr01qq3c3u0lf0cgk5dkhr01qq3c3u0lfg'

finnhub_client = finnhub.Client(api_key=api_key)

df = pd.read_csv("sp500.csv")

tickers = df['Symbol'].tolist()

def pull_sentiment(symbol):
    count =  0
    for i in range(50):
        count += 1
    sentiment_data = finnhub_client.stock_insider_sentiment(symbol, '2023-03-01', '2023-04-01') 
    return(sentiment_data['data'][count]['mspr'])

sentiment_values = []
for symbol in tickers:
    mspr = pull_sentiment(symbol)
    if mspr is not None:
        sentiment_values.append(mspr)
    else:
        print(f"Failed to get mspr for {symbol}")


print(sentiment_values)
