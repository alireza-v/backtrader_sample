# backtrader_sample
sample code from backtrader library

The `macd` and `candlestick` module are extrancting the pre existed Data to calcualte the some chart pattern and macd signal seperately.

## __Chart Pattern listed in `candlestick` module are:__
1. bearish engulfing
2. bullish engulfing
3. Hammer
4. Grave stone
5. dragon fly
6. three white soldier
7. morning start

```python
# Macd signal with label
from Project_01.macd import macd
X,y=macd.signal_macd()
from  Project_01.candlstick import ca
data=ca.candstick(data='BTC-USD')

# Macd signal with label
from Project_01.macd import macd
X,y=macd.signal_macd()
```


# MACD Stategy in machine leanring
- We extract our signal of [__buy and sell__] by macd. those preiod of candles that happend before crossing buy(label as 1) and those number of candle that happend just before Crossing Sell(label as 0) are important for us. we gather them out and turn them into Tensor.

- at the end we have a unshaped Tensor with the X_columns of __OHCL,Volume,change etc__ and the one dimention y_label of 0 and 1.
then we pass these unshaped matrix to our neural network to let the machnie learn to in what sequence of candles we would have buy or sell

__In the Evaluation process__ we pass the `30-50 Previos Candle` to our mdoel to check the `buy,sell Probability` of the next candle and so on....

