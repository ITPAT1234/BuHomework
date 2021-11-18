import websocket
import json
import pandas as pd
import mplfinance as mpf
import matplotlib.animation as animation
import dateutil.parser
import datetime
import threading
import time
import sys
from datetime import date, datetime, timedelta


minutes_process = {}
minute_candlesticks = []
current_tick = None
previous_tick = None
currencyInput = input("Enter Your CurrencyName (BTC,ETH,XRP...) : ").upper()
fig = mpf.figure(style="charles", figsize=(7, 8))
ax1 = fig.add_subplot(1, 1, 1)

socket = 'wss://ws-feed.pro.coinbase.com'


def on_open(ws):
    print("Connection is opened")
    subscribe_msg = {
        "type": "subscribe",
        "channels": [
                    {
                        "name": "ticker",
                        "product_ids": [
                            currencyInput+"-USD"
                        ]
                    }

        ]
    }

    ws.send(json.dumps(subscribe_msg))


def on_message(ws, message):
    global current_tick, previous_tick

    previous_tick = current_tick
    current_tick = json.loads(message)

    print("=== Received Tick ===")
    # show current price and time
    print(f"{current_tick['price']} @ {current_tick['time']}")

    # convert time
    tick_datetime_object = dateutil.parser.parse(current_tick['time'])
    timenow = tick_datetime_object + timedelta(hours=8)
    tick_dt = timenow.strftime("%m/%d/%Y %H:%M")

    # check new candlestick
    if not tick_dt in minutes_process:
        print("New candlestick!!!")
        minutes_process[tick_dt] = True
        if len(minute_candlesticks) > 0:
            minute_candlesticks[-1]["close"] = previous_tick["price"]

        minute_candlesticks.append({
            "minute": tick_dt,
            "open": current_tick["price"],
            "high": current_tick["price"],
            "low": current_tick["price"]
        })
        df = pd.DataFrame(minute_candlesticks[:-1])
        df.to_csv("bitcoin_data.csv")

    if len(minute_candlesticks) > 0:
        current_candlestick = minute_candlesticks[-1]
        if current_tick['price'] > current_candlestick['high']:
            current_candlestick['high'] = current_tick['price']
        if current_tick['price'] < current_candlestick['low']:
            current_candlestick['low'] = current_tick['price']

        print("== Candlesticks ==")
        for candlestick in minute_candlesticks:
            print(candlestick)


def animate(ival):
    idf = pd.read_csv("bitcoin_data.csv", index_col=0)
    idf['minute'] = pd.to_datetime(idf['minute'], format="%m/%d/%Y %H:%M")
    idf.set_index('minute', inplace=True)

    ax1.clear
    mpf.plot(idf, ax=ax1, type='candle', ylabel=f'{currencyInput} US$')


ani = animation.FuncAnimation(fig, animate, interval=250)
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
currentTime = datetime.now()
thr = threading.Thread(target=ws.run_forever)
prepareTime = abs(int(currentTime.strftime("%S")) - 60)
print(f"Wait for Prepare Data : {prepareTime} second")
thr.start()
time.sleep(prepareTime + 5)
mpf.show()
