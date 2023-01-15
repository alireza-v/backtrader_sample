import pandas_ta as ta
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import torch


# Calculate MACD
class MACD():
    def __init__(self):
        super(MACD, self).__init__()
        self.data=pd.read_csv('btc_2021.csv') # Data
        self.X_list=[]
        self.label=[]

    def signal_macd(self):
        # Calculate MACD values using the pandas_ta library
        

        df=pd.read_csv('btc_2021.csv')
        df=self.data.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)
        
        # Create empty columns for buy and sell signals
        self.data["Buy"] = None
        self.data["Sell"] = None
        
        
        # Fill in buy and sell columns
        for i in range(len(self.data)):
            if i > 0:
                if self.data.at[i, "MACD_12_26_9"] > self.data.at[i, "MACDs_12_26_9"] and self.data.at[i-1, "MACD_12_26_9"] < self.data.at[i-1, "MACDs_12_26_9"]:
                    self.data.at[i, "Buy"] =1
                elif self.data.at[i, "MACD_12_26_9"] < self.data.at[i, "MACDs_12_26_9"] and self.data.at[i-1, "MACD_12_26_9"] > self.data.at[i-1, "MACDs_12_26_9"]:
                    self.data.at[i, "Sell"] = 0

     
        box=[]
        # b_plus=torch.cat([torch.torch.tensor[]])
        for index,z in enumerate(self.data['Buy']):
            if z ==1:  
                box.append(0)
                if len(box) <2:
                    first_index=index
                
                elif len(box) >1:                
                    last_index=index
                    box.clear()
                    self.X_list.append((self.data.loc[first_index:last_index+1,
                                        ['Open','High','Low','Close','Adj Close','Volume']]).values )
                    self.label.append(1)
            

        
        plt.figure(figsize=(10, 4)) 
        ax1 = plt.subplot(3, 1, 1)
        plt.plot(self.data.Date, self.data.Close)
        ax1.set_title('Close Price')

        ax2 = plt.subplot(3, 1, 2)
        plt.plot(self.data.Date, self.data['MACD_12_26_9'], c='black')
        plt.plot(self.data.Date, self.data['MACDs_12_26_9'], c='red')
        plt.scatter(np.arange(len(self.data)),self.data.Buy,marker='^',c='green')
        plt.scatter(np.arange(len(self.data)),self.data.Sell,marker='v',c='red')
        ax2.set_title('MACD and Signal')
        plt.show()

        return self.X_list,np.array(self.label)
                
# Excute
obj=MACD()
X_list,label=obj.signal_macd()
