# Coinpaprika API wrapper for python

Coinpaprika API delivers free & frequently updated market data from the world of crypto: coin prices, volumes, market caps, ATHs, return rates and more.

Coinpaper.io uses the Coinpaprika API for all price-related data.
The here provided wrapper for the coinpaprika API is delivered under the MIT License.

## Installation:

The package is uploaded to PyPi.

```
pip install coinpaprika-api
```

## Global

### Get market overview data

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
market_overview = api_client.global_market_overview()
```

## Coins

### List coins

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
all_coins = api_client.coins()
```

### Get coin by ID

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
bitcoin = api_client.coins.with_id("btc-bitcoin")
```

### Get twitter timeline for coin

Not more than last 50 tweets

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
twitter_timeline = api_client.coins.twitter("btc-bitcoin")
```

### Get coin events by coin ID

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
events = api_client.coins.events("btc-bitcoin")
```

### Get exchanges by coin ID

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
exchanges = api_client.coins.exchanges("btc-bitcoin")
```

### Get markets by coin ID

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
markets = api_client.coins.markets("btc-bitcoin")
```

### Get OHLC for last full day

Open/High/Low/Close values with volume and market_cap

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
last_OHLC = api_client.coins.last_OHLC("btc-bitcoin")
```

### Get historical OHLC

Open/High/Low/Close values with volume and market_cap. Request example: https://api.coinpaprika.com/v1/coins/btc-bitcoin/ohlcv/historical?start=2019-01-01&end=2019-01-20 if the last day is current day it can an change with every request until actual close of the day at 23:59:59

```python
import CoinpaprikaClient
from datetime import datetime, timedelta

api_client = CoinpaprikaClient()
historical_OHLC = api_client.coins.historical_OHLC(
    coin_id="btc-bitcoin",
    start=datetime.now() - timedelta(weeks=1),
    end=datetime.now(),
    limit=7,
)
```

### Get today OHLC (can change every each request until actual close of the day at 23:59:59)

Open/High/Low/Close values with volume and market_cap for today

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
todays_OHLC = api_client.coins.today_OHLC(coin_id="btc-bitcoin")
```

## People

### Get people by ID

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
vitalik = api_client.people.with_id("vitalik-buterin")
```

## Tags

### List tags

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
tags = api_client.tags()
```

### Get tag by ID

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
tag = api_client.tags.with_id("blockchain-service")
```

## Tickers

### Get tickers for all coins

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
tickers = api_client.tickers()
```

### Get ticker information for specific coin

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
btc_ticker = api_client.tickers.for_coin("btc-bitcoin")
```


### Get historical tickers for specific coin

```python
import CoinpaprikaClient
from datetime import datetime, timedelta

api_client = CoinpaprikaClient()
historical_ticker = api_client.tickers.historical_ticker_for_coin(
    coin_id="btc-bitcoin",
    start=datetime.now() - timedelta(weeks=1),
    end=datetime.now(),
    limit=1000,
    interval="1h"
)
```

## Exchanges

### List exchanges

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
exchanges = api_client.exchanges()
```

### Get exchange by ID

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
binance = api_client.exchanges.with_id("binance")
```

### List markets by exchange ID

```python
import CoinpaprikaClient

api_client = CoinpaprikaClient()
binance_markets = api_client.exchanges.markets("binance")
```