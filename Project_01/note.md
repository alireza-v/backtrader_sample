

## To do list
1. add the function counter form the __one.ipynb__ and add it it __Tester.py main class__
2. find a way to predict the feature label, the features engineer about the dataset
3. calculating hte macd by pandas.bt (only Sell)
4. Test the archeticture



### where are we and what are we doing....
    our featuers is the the signal of macd. trained to understand what and where is 0 and 1 in the chart. then we pick a atleast 30 windows of last
     candle to predict the next candl.not all the candle must would end with the probabality of above 60 percent. just bunch of a little  candle would
     eventually end with the signal buy and sell

     1. two different model for the candlstick the indicator.
     2. 



----
## Done
1. do some backtrader on the indicator
2. calculating hte macd by pandas.bt (only Buy)
3. 
 

###  Want to do at the end of the year

- 


## the Candlestick we need to apply
1. bearish engulfing
2. bullish engulfing
3. Hammer
4. Grave stone
5. dragon fly
6. three white soldier
7. morning start


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


we have our data
1. indicator are set, first check pass our indicator macd to our neral to see what goes out,
    __then__
2. if it work with the lighest evaluation we goe to the next features.

Let's find our what are having here? ->
1. __macd indicator__ with period of block candle between every signal that is taking
2. __candlstick pattern__ by neural network (hammer,gravestone,morningstar,engulfing etc.)
3. __Multi timeframe__ for more evaluation ()








# road map of AI enginner
Becoming an Artificial Intelligence (AI) Engineer requires a combination of education and experience in computer science, mathematics, statistics, and machine learning. Here is a general roadmap to becoming an AI Engineer:

Earn a Bachelor's degree in a relevant field such as Computer Science, Mathematics, Electrical Engineering, or Physics. This will provide you with a solid foundation in the fundamentals of computer science and mathematics, and prepare you for more advanced studies in AI.

Develop a strong understanding of programming languages and technologies commonly used in AI, such as Python, Java, and C++. You can do this by taking online courses or pursuing a minor or certificate program in computer programming.

Gain experience in machine learning and data science by participating in coding competitions, hackathons, or working on personal projects. This will help you develop your skills and build a portfolio of work to showcase to potential employers.

Obtain a graduate degree in a related field such as a Master's in Computer Science, Artificial Intelligence, or Data Science. This will provide you with advanced knowledge in AI, machine learning, and data science, and prepare you for more advanced roles in the field.

Gaining practical experience by working on AI projects or internships. You can also start by participating in open-source projects or contributing to research papers.

Specialize in a specific area of AI such as natural language processing, computer vision, or reinforcement learning. This will help you to stand out in the field and increase your chances of landing a job in your area of interest.

Keep yourself updated with the latest advancements in AI by reading research papers and attending conferences and workshops.

Network and build relationships with other professionals in the field by attending meetups, joining online communities, and participating in hackathons.

Look for entry-level or internship opportunities to gain practical experience in the field and start building your professional network.

Look for job opportunities as an AI Engineer, and apply to roles that match your skills and experience.

Note that this is a general roadmap and depending on the specific role and industry, the requirements may differ. Additionally, the field of AI is rapidly evolving and the job market is highly competitive, so it's important to continue learning and developing your skills throughout your career.





