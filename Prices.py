### 1. Loading the Data
import pandas as pd

df = pd.read_csv("s&p500.csv", index_col='Date', parse_dates=True)

df.head()
df.tail()

#### 2. Analyzing the Data
df.describe()
df['Close'].min() #2237.39990234375
df['Close'].max() #4796.56005859375
df['Close'].head()

#### Visualizations:

#Visual (1)
df['Close'].plot(figsize=(14, 7), title='S&P Closing Price | 2017 - 2022')

#Visual (2)
ax1 = df['Close'].plot(figsize=(14, 7), title='S&P Closing Price | 2017 - 2022')
ax2 = ax1.twinx()
df['Volume'].plot(ax=ax2, color='red', ylim=[df['Volume'].min(), df['Volume'].max() * 5])
ax1.figure.legend(["Close", "Volume"])

#Visual (3)
df['Volume'].plot(kind='hist')

#Visual (4)
df['Volume'].plot(kind='box', vert=False)


### 3. Data Wrangling
df['Close SMA'] = df['Close'].rolling(60).mean()
df[['Close', 'Close SMA']].tail(10)

#Wrangling & Visual (5)
ax = df[['Close', 'Close SMA']].plot(figsize=(14, 7), title='Close Price & its SMA')

df['Lower Band'] = df['Close SMA'] - (2 * df['Close'].rolling(60).std())
df['Upper Band'] = df['Close SMA'] + (2 * df['Close'].rolling(60).std())

df[['Close', 'Close SMA', 'Lower Band', 'Upper Band']].tail()

#Visual (6)
df[['Close', 'Lower Band', 'Upper Band']].plot(figsize=(14, 7), title='Close Price & its SMA')

#Visual (7)
ax = df[['Close', 'Lower Band', 'Upper Band']].plot(figsize=(14, 7), title='Close Price & its SMA')
ax.annotate(
    "Let's find this point", xy=(pd.Timestamp("2020-03-23"), 2237), 
    xytext=(0.9, 0.1), textcoords='axes fraction',
    arrowprops=dict(facecolor='red', shrink=0.05),
    horizontalalignment='right', verticalalignment='bottom');


df.loc['2020-03-01': '2020-06-01'].query("Close < `Lower Band`").head()

#Visual (8)
df.loc['2020-01-01': '2020-06-01', ['Close', 'Lower Band', 'Upper Band']].plot(figsize=(14, 7), title='Close Price & its SMA | 2020-01-01 to 2020-06-01')
