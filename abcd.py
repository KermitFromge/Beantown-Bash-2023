import requests
import pandas as pd
import finnhub



api_key = 'cgk8au9r01qq3c3u2fk0cgk8au9r01qq3c3u2fkg'

finnhub_client = finnhub.Client(api_key=api_key)

df = pd.read_csv("sp500.csv")

tickers = df['Symbol'].tolist()

def pull_sentiment(symbol):
    sentiment_data = finnhub_client.stock_insider_sentiment(symbol, '2023-03-31', '2023-04-01') 
    print(sentiment_data[1])
    return(sentiment_data.get(['mspr']))

sentiment_values = []
for symbol in tickers:
    mspr = pull_sentiment(symbol)
    if mspr is not None:
        sentiment_values.append(mspr)
    else:
        print(f"Failed to get mspr for {symbol}")


print(sentiment_values)
