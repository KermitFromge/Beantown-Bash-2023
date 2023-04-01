import requests
import finnhub
import csv
import pandas as pd

print("START")
finnhub_client = finnhub.Client(api_key="cgk5dkhr01qq3c3u0lf0cgk5dkhr01qq3c3u0lfg")

df =  pd.read_csv("sp500.csv")

tickers = []

for i in df['Symbol']:
    tickers.append(i)
def fetch_insider_sentiment(ticker):
        sentiment_data = finnhub_client.stock_insider_sentiment(ticker, '2023-03-01', '2023-03-31')
        print(sentiment_data)
        if 'mspr' in sentiment_data:
            return sentiment_data['mspr']
mspr_data = {}
for i in range(2):
    print("checkpoint")
    print(tickers[i])
    mspr = fetch_insider_sentiment(tickers[i])
    print(mspr)
    if mspr is not None:
        mspr_data[tickers] = mspr

print(mspr_data)

#print(finnhub_client.stock_insider_sentiment('AAPL', '2023-03-01', '2023-03-31'))
