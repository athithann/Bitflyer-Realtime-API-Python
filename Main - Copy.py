import time
import pytz
import asyncio
import websockets
import pandas as pd
from datetime import datetime
from json import loads as jsdec
from os import system

errorCount = 0
data = {}
websocket_url = "wss://ws.lightstream.bitflyer.com/json-rpc?subscribe{'channel': 'lightning_ticker_FX_BTC_JPY'}"
subTopic = "lightning_ticker_FX_BTC_JPY"


async def runWS():
    async with websockets.connect(websocket_url) as websocket:
        # print('Bitmex Price Fetch (UTC) splitter program started at ' + str(datetime.now()))
        # global data
        # utc = pytz.utc
        # UTC = pytz.timezone('UTC')
        # update_condition = 0
        # reminder_condition = 0
        # document_condition = 0
        # df = pd.read_csv('../Files/BTC_10S.csv', index_col=[0], parse_dates=True)
        # print(df.tail(2))
        while True:
            tickerEnc = await websocket.recv()
            tickerEnc = jsdec(tickerEnc)
            data = str(tickerEnc)
            print(data)
            # if data.find("'data'") != -1:
            #     a = (data.split("'asks': [["))[1]
            #     b = a.split(", ")
            #     askprice = float(b[0])
            #     c = b[1].split("]")
            #     askvol = float(c[0])
            #     askvol2 = float(b[3].split("]")[0])
            #     askvol3 = float(b[5].split("]")[0])
            #     askvol4 = float(b[7].split("]")[0])
            #     askvol5 = float(b[9].split("]")[0])
            #     d = (data.split("'bids': [["))[1]
            #     e = d.split(", ")
            #     bidprice = float(e[0])
            #     f = e[1].split("]")
            #     bidvol = float(f[0])
            #     bidvol2 = float(e[3].split("]")[0])
            #     bidvol3 = float(e[5].split("]")[0])
            #     bidvol4 = float(e[7].split("]")[0])
            #     bidvol5 = float(e[9].split("]")[0])
            #     totalaskvol = askvol * 5 + askvol2 * 4 + askvol3 * 3 + askvol4 * 2 + askvol5 * 1
            #     totalbidvol = bidvol * 5 + bidvol2 * 4 + bidvol3 * 3 + bidvol4 * 2 + bidvol5 * 1
            #     midprice = (askprice + bidprice) / 2
            #     fee = (midprice * 0.001 + 0.5) / 2
            #     superprice = midprice - fee + (totalbidvol / (totalbidvol + totalaskvol)) * fee * 2
            #     rightnow = datetime.now(UTC)
            #     rightnow = rightnow.astimezone(utc)
            #     if rightnow.second % 10 > 7 and update_condition == 0:
            #         update_condition = 1
            #         index = rightnow.replace(microsecond=0)
            #         df.at[index, 'open'] = superprice
            #         df.at[index, 'high'] = superprice
            #         df.at[index, 'low'] = superprice
            #         df.at[index, 'close'] = superprice
            #         df.at[index, 'volume'] = superprice
            #     elif not (rightnow.second % 10 > 7):
            #         update_condition = 0
            #     if rightnow.second <= 1 and document_condition == 0:
            #         document_condition = 1
            #         df.to_csv('../Files/BTC_10S.csv', index_label='Date')
            #     elif not rightnow.second <= 1:
            #         document_condition = 0
            #     if rightnow.day == 1 and rightnow.hour == 14 and rightnow.minute == 50 and 23 < rightnow.second < 25 and reminder_condition == 0:
            #         reminder_condition = 1
            #         df = pd.read_csv('../Files/BTC_10S.csv')
            #         date_column = pd.DatetimeIndex(df['Date'])
            #         df.set_index('Date', inplace=True)
            #         month_list = date_column.month.unique()
            #         if len(month_list) > 1:
            #             for i in month_list:
            #                 temp = df[date_column.month == i]
            #                 if i != rightnow.month:
            #                     filename = '../Files/BTC_USD_{year}_{month}.csv'.format(
            #                         year=str(date_column[-1:].year[0]),
            #                         month=i)
            #                     temp.to_csv(filename)
            #                 else:
            #                     df = temp
            #             print('Document split successfully at ', str(rightnow))
            #     elif not (rightnow.day == 1 and rightnow.hour == 14 and rightnow.minute == 50 and 23 < rightnow.second < 25):
            #         reminder_condition = 0


def run():
    try:
        asyncio.get_event_loop().run_until_complete(runWS())
    except Exception as e:
        x = e
        print(x)
        global errorCount
        errorCount += 1
        print("Error in websocket, retrying, attempt #" + str(errorCount) + "\n" + str(type(e)) + "\t" + str(e))
        time.sleep(1)
        run()


run()
