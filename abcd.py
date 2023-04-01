import requests
import pandas as pd
import time

api_key = 'cgk5dkhr01qq3c3u0lf0cgk5dkhr01qq3c3u0lfg'

df = pd.read_csv("sp500.csv")

tickers = df['Symbol'].tolist()

def pull_sentiment(symbol):
    url = f'https://finnhub.io/api/v1/stock/insider-sentiment?symbol={symbol}&from=2023-03-31&to=2023-04-01&token={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if 'data' in data:
            for record in data['data']:
                if record['symbol'] == symbol and record['year'] == 2023 and record['month'] == 3:
                    mspr_value = record.get('mspr', None)
                    if mspr_value is not None:
                        return mspr_value
    return None

sentiment_values = []
for symbol in tickers:
    mspr = pull_sentiment(symbol)
    if mspr is not None:
        sentiment_values.append(mspr)
    else:
        print(f"Failed to get mspr for {symbol}")

    # Add a delay between requests
    time.sleep(1)  # Sleep for 1 second

print(sentiment_values)
