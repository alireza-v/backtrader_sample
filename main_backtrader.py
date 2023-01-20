

#------->>> Libaries
import backtrader as bt
import numpy as np
import tqdm
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from  tqdm import tqdm
result=pd.DataFrame()

class IchimokuStrategy(bt.Strategy):
    # base prams that above prams that use with np.random.randint palce into these below params
    params = (('period_me1', 12), ('period_me2', 26), ('period_signal', 9))
    
    def __init__ (self):
        self.period_me1=params['period_me1']
        self.period_me2=params['period_me2']
        self.period_signal=params['period_signal']
        self.macd = bt.indicators.MACD(self.data.close, period_me1=params['period_me1'], period_me2=params['period_me2'], period_signal=params['period_signal'])
        self.raiser=False
        self.index_pos=1
        self.change=1

    def next(self):

        # print(self.macd.period_me1[0])
        # print(self.period_me1)
        # print()
        # 

        if  not self.position:
            if self.macd.macd[0] > self.macd.signal[0]:
                self.buy()
        # else :
        else:
            if  self.macd.macd[0] < self.macd.signal[0]:
                self.sell()
                name='{}_{}_{}'.format(self.period_me1,self.period_me2,self.period_signal)
                result.loc[len(self),[name]]=(round(self.broker.getvalue()))

        # print(f'Total_values :::::> {round(self.broker.getvalue())}---> params: {self.period_me1}, {self.period_me2}, {self.period_signal}')



cerebro = bt.Cerebro()

# Thest the Strategy in different paramerers in every epochs
epoch=10

# For a in tqdm.tqdm(range(epoch), leave=True):
plt.figure(figsize=(12,10))
def format_y_as_thousands(y, _):
    return '{:,.0f}k'.format(y / 1000)


for i in tqdm(range(epoch),position=0,leave=True):
        params = {'period_me1': np.random.randint(5,100), 'period_me2': np.random.randint(5,100), 'period_signal': np.random.randint(5, 15)}
        cerebro.addstrategy(IchimokuStrategy, period_me1=params['period_me1'], period_me2=params['period_me2'],period_signal=params['period_signal'])
        data = bt.feeds.YahooFinanceCSVData(dataname='BTC-USD.csv')
        cerebro.adddata(data)
        cerebro.run()
        # cerebro.plot(style='candlestick', barup='green', bardown='red')


# Ploting ------>>>>

for col_name, col_data in result.items():
    plt.ion()
    df_notna=result[col_name].dropna(axis=0)
    plt.plot(np.arange(len(df_notna)),df_notna,c=np.random.rand(3), label=col_name)
    plt.legend(loc='upper left',fontsize=5)
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_y_as_thousands))
    plt.pause(0.0000000001) # pause for a short time
    plt.grid()
    plt.draw()

# stay on the chart
plt.show(block=True)
