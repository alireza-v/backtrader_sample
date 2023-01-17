# Calculate MACD values using the pandas_ta library
import pandas_ta as ta
import pandas as pd
from candlestick import candlestick
import matplotlib.pyplot as plt


class Candle():
    def __init__ (self):
        self.data= 0

    def candstick(self,data):
        # macd
        self.data= pd.read_csv(f'{data}.csv',parse_dates=True,index_col='Date')
        macd=self.data.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)

        # Defining OHLC
        ohlc=["Open", "High", "Low", "Close"]
        # candlstick pattern with candlestick
        self.data=candlestick.doji_star(self.data,ohlc,target='doji_start')
        self.data=candlestick.bearish_engulfing(self.data,ohlc,target='bearish_engulfing')
        self.data=candlestick.bullish_engulfing(self.data,ohlc,target='bullish_engulfing')
        self.data=candlestick.hammer(self.data,ohlc,target='hammer')
        self.data=candlestick.gravestone_doji(self.data,ohlc,target='gravestone_doji')
        self.data=candlestick.dragonfly_doji(self.data,ohlc,target='dragonfly_doji')
        self.data=candlestick.morning_star_doji(self.data,ohlc,target='morningstar')
        
        return self.data

# Excute
ca=Candle()
