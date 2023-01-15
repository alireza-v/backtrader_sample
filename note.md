

## To do list
1. add the function counter form the __one.ipynb__ and add it it __Tester.py main class__
2. find a way to predict the feature label, the features engineer about the dataset
3. calculating hte macd by pandas.bt (only Sell)
4. Test the archeticture



### where are we and what are we doing....
our featuers is the the signal of macd. trained to understand what and where is 0 and 1 in the chart. then we pick a atleast 30 windows of last
     candle to predict the next candl.not all the candle must would end with the probabality of above 60 percent. just bunch of a little  candle would
     eventually end with the signal buy and sell

----
## Done
1. do some backtrader on the indicator
2. calculating hte macd by pandas.bt (only Buy)
3. 




tihnk as a machine learning engineer and testing and deploying of models and that person want to become a computer scientist, wnat to figure out how computer and all the aspect that has made the computer. that person as a machine learning engineer does not have a heavy background in mathematic but also can deal with models without undersanding fully how they are working..



|Task	|Sub-Task|	Time|


Experiment with different model architectures	Try implementing LSTM or GRU	1 hour
Experiment with different model architectures	Compare performance with current model	1 hour
Try adding more layers to the current model	Test different numbers of layers	1 hour
Implement regularization techniques such as dropout to prevent overfitting	Add dropout after each linear layer	1 hour
Experiment with different window sizes and see how it affects the model's performance	Test window sizes of 20, 30, and 40	30 minutes
Use cross validation to evaluate the model's performance	Implement k-fold cross validation	30 minutes
Add more features to the input data and see how it affects the model's performance	Add technical indicators such as moving averages	1 hour
Test the final model on unseen data and make any final adjustments	Prepare test set and evaluate performance	1 hour


## PyAututoGui with CV2 for recording the screen
import cv2
import numpy as np
import pyautogui

fourcc = cv2.VideoWriter_fourcc(*'XVID')
screen = (1920, 1080)
out = cv2.VideoWriter('screen_recording.avi', fourcc, 20.0, screen)

screen_size = (1920, 1080)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()


hiiiii
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor, SpanSelector

# Create the figure and axes for the subplot
fig, ax = plt.subplots()

# Plot the Close price on the bottom axis
ax.plot(short.index, short.Close, label='Close')

# Create the top axes for the macd and signal values
ax2 = ax.twinx()

# Plot the macd and signal values on the top axis
ax2.plot(short.index, short.macd, c='g', label='macd')
ax2.plot(short.index, short.signal, c='r', label='signal')

# Add crosshairs to the plot
cursor = Cursor(ax, useblit=True, color='red', linewidth=1)

# Add data dragging to the plot
def onselect(xmin, xmax):
    print(f'Selected x range: {xmin} to {xmax}')

span = SpanSelector(ax, onselect, 'horizontal', useblit=True, rectprops=dict(alpha=0.5, facecolor='red'))

# Show the legend
ax.legend()
ax2.legend()

# Display the plot
plt.show()


# # BTC value OHCL
# short=pd.read_csv('BTC_short.csv')

# # macd and signal value
# df=pd.read_csv('macd.csv')

# short['macd']=df['macd']

# short['signal']=df['signal']

# plt.figure(figsize=(15, 8)) 
# ax1 = plt.subplot(2, 1, 1)
# plt.plot(short.index, short.Close)
# ax1.set_title('Close Price')

# ax2 = plt.subplot(2, 1, 2)
# plt.plot(short.index, short.macd, c='g')
# plt.plot(short.index, short.signal, c='g')
# ax2.set_title('MACD and Signal')

