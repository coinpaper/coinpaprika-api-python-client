# Coinpaprika API wrapper for python

Coinpaprika API delivers free & frequently updated market data from the world of crypto: coin prices, volumes, market caps, ATHs, return rates and more.

Coinpaper.io uses the Coinpaprika API for all price-related data.
The here provided wrapper for the coinpaprika API is delivered under the MIT License.

## Installation:

The package is uploaded to PyPi.

```
pip install coinpaprika-client
```

## Global

### Get market overview data

```python
import Coinpaprika

api_client = Coinpaprika.Client()
market_overview = api_client.global_market_overview()
```

## Coins

### List coins

```python
import Coinpaprika

api_client = Coinpaprika.Client()
all_coins = api_client.coins()
```

### Get coin by ID

```python
import Coinpaprika

api_client = Coinpaprika.Client()
bitcoin = api_client.coins.with_id("btc-bitcoin")
```

### Get twitter timeline for coin

Not more than last 50 tweets

```python
import Coinpaprika

api_client = Coinpaprika.Client()
twitter_timeline = api_client.coins.twitter("btc-bitcoin")
```

### Get coin events by coin ID

```python
import Coinpaprika

api_client = Coinpaprika.Client()
events = api_client.coins.events("btc-bitcoin")
```

### Get exchanges by coin ID

```python
import Coinpaprika

api_client = Coinpaprika.Client()
exchanges = api_client.coins.exchanges("btc-bitcoin")
```

### Get markets by coin ID

```python
import Coinpaprika

api_client = Coinpaprika.Client()
markets = api_client.coins.markets("btc-bitcoin")
```

### Get OHLC for last full day

Open/High/Low/Close values with volume and market_cap

```python
import Coinpaprika

api_client = Coinpaprika.Client()
last_OHLC = api_client.coins.last_OHLC("btc-bitcoin")
```

### Get historical OHLC

Open/High/Low/Close values with volume and market_cap. Request example: https://api.coinpaprika.com/v1/coins/btc-bitcoin/ohlcv/historical?start=2019-01-01&end=2019-01-20 if the last day is current day it can an change with every request until actual close of the day at 23:59:59

```python
import Coinpaprika
from datetime import datetime, timedelta

api_client = Coinpaprika.Client()
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
import Coinpaprika

api_client = Coinpaprika.Client()
todays_OHLC = api_client.coins.today_OHLC(coin_id="btc-bitcoin")
```

## People

### Get people by ID

```python
import Coinpaprika

api_client = Coinpaprika.Client()
vitalik = api_client.people.with_id("vitalik-buterin")
```

## Tags

### List tags

```python
import Coinpaprika

api_client = Coinpaprika.Client()
tags = api_client.tags()
```

### Get tag by ID

```python
import Coinpaprika

api_client = Coinpaprika.Client()
tag = api_client.tags.with_id("blockchain-service")
```

## Tickers

### Get tickers for all coins

```python
import Coinpaprika

api_client = Coinpaprika.Client()
tickers = api_client.tickers()
```

### Get ticker information for specific coin

```python
import Coinpaprika

api_client = Coinpaprika.Client()
btc_ticker = api_client.tickers.for_coin("btc-bitcoin")
```


### Get historical tickers for specific coin

```python
import Coinpaprika
from datetime import datetime, timedelta

api_client = Coinpaprika.Client()
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
import Coinpaprika

api_client = Coinpaprika.Client()
exchanges = api_client.exchanges()
```

### Get exchange by ID

```python
import Coinpaprika

api_client = Coinpaprika.Client()
binance = api_client.exchanges.with_id("binance")
```

### List markets by exchange ID

```python
import Coinpaprika

api_client = Coinpaprika.Client()
binance_markets = api_client.exchanges.markets("binance")
```