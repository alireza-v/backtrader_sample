#ma20
import backtrader as bt
import pandas as pd
import yfinance as yf
import requests

class Test:

    ma=20

    data=['bnb-usd','xrp-usd','btc-usd','eth-usd','doge-usd','ada-usd','matic-usd']
    start='2020-6-25'
    end='2021-6-25'
    first=[]
    last=[]
    ticker=[]

    def __init__(self):
        for i in self.data[:]:
            cerebro=bt.Cerebro()
            cerebro.addstrategy(self.Inner)
            data=bt.feeds.PandasData(
            dataname=yf.download(i, self.start, self.end))
            cerebro.adddata(data)
            self.first.append(cerebro.broker.getvalue())
            cerebro.run()
            self.last.append(int(cerebro.broker.getvalue()))
            self.ticker.append(i)
        self.df()

    def df(self):
        data=dict()
        data['ticker']=self.ticker
        data['first']=self.first
        data['last']=self.last
        df=pd.DataFrame(data)

        df['ma20(%)']=df['last']-df['first']
        df.set_index('ticker')
        df.to_csv('ma20.csv')

    class Inner(bt.Strategy):
        def __init__(self):
            self.dataclose=self.datas[0].close
            self.ind=bt.indicators.SimpleMovingAverage(self.datas[0].close,period=20)
            self.order=None

        def log(self,txt,dt=None):
            dt=dt or self.datas[0].datetime.date(0)
            print('%s %s'%(dt.isoformat(),txt))

        def next(self):
            if self.order:
                return

            if not self.position:
                if self.dataclose[0]>self.ind[0]:
                    self.buy()
                else:
                    return
            else:
                if len(self)>=(self.bar_executed+4):
                    self.log('exited, %.2f'%self.dataclose[0])
                    self.order=self.close()

        def notify_order(self, order):
            if order.status == order.Completed:
                if order.isbuy():
                    self.log('buy at, %.2f'%order.executed.price)
                else:
                    self.log('sell at, %.2f'%order.executed.price)
                    self.log('your profit, %.2f'%((self.broker.getvalue())-(self.firstMoney)))
                self.bar_executed = len(self)
            elif order.status in [order.Canceled, order.Margin, order.Rejected]:
                self.log("Order was canceled")
            self.order = None

page=requests.get('https://finance.yahoo.com/')
if page.status_code==200:
    ins=Test()
else:
    print('internet connection')