import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn')
import pandas_datareader.data as web
import datetime
import numpy as np


def main():
    # Select dates for stock exploration
    start = datetime.datetime(2017, 1, 1)
    end = datetime.datetime(2022, 1, 1)

    test()

    # Task 1: Examine relationship between vix volatility index and spy
    # runTask2()
    """
    Here we see an interesting result. First of all, our data is severely skewed with most of it being clustered in the 
    bottom left-hand corner. This is indicative of something, but I can't quite remember. Regardless of that, we do 
    a very feint positive linear relationship. We see that as the price of VIX increases (that is, as the stock market 
    gets more volatile, the number of shares traded increases.
    """

    # Ideas
    """
    - We can use the VIX to track volatility index and see how that relates to stock price performance
    - We can track Treasury values and average mortgage inerest rates at Bankrate.com or HSN.com. 
    - We can create heatmap showing correlation between interest rates and stock price performance. 
    - Plot the moving average (popular on trading view and such)
    
    """


def loadData(start, end, stock):
    return web.DataReader(stock, 'yahoo', start, end)


def infoSeparator():
    print("-" * 40)


def getParameter(stock, parameter='Adj Close'):
    # Assert that the object passed is a data frame
    assert isinstance(stock, pd.DataFrame), "Stock passed me be a data frame"

    # Truncate the values we want
    truncated_stock_values = stock.truncate()[parameter]

    return truncated_stock_values


def test():
    spy15 = pd.read_csv("MORTGAGE15US.csv")
    spy30_df = pd.read_csv("MORTGAGE30US.csv")

    # Find the date 2000-01-01 or earliest date in 2000
    dates_15 = spy15["DATE"][436:]
    dates_30 = spy30_df["DATE"][3:]
    # dates_30 = spy30["DATE"][595:607]
    print(dates_30[605])
    print(spy30_df['MORTGAGE30US'][605])
    spy30_df.at[606, "DATE"] = "2011-07-21"
    spy30_df.at[606, "MORTGAGE30US"] = 4.52

    # print(dates_30[606])
    # print(spy30['MORTGAGE30US'][606])

    plt.plot(dates_15, spy15['MORTGAGE15US'][436: ], 'r-', label="15")
    plt.plot(dates_30, spy30_df['MORTGAGE30US'][3: ], 'b-', label="30")
    plt.plot([dates_30[606]], [spy30_df['MORTGAGE30US'][606]], "ko")
    # plt.plot(dates_30, spy30['MORTGAGE30US'][595:607], 'b-', label="30")
    plt.legend()
    plt.show()

    # plt.legend()
    # plt.show()
    #
    # plt.plot(spy30['DATE'], spy30['MORTGAGE30US'], 'b-', label="30")
    # plt.legend()
    # plt.show()

    print(len(spy30_df['DATE']))
    print(len(spy30_df['MORTGAGE30US']))

    # plt.title("Historical Mortgagae Rate Averages ")
    # plt.plot(spy15['DATE'], spy15['MORTGAGE15US'], 'r.', label='15-year fixed')
    # plt.plot(spy30['DATE'], spy30['MORTGAGE30US'], 'b.', label='30-year fixed')
    # # plt.xlabel("January 2000 to January 2022")
    # plt.ylabel("Interest Rates")
    # plt.legend()
    # plt.show()

    print(spy15.info())


def runTask2():
    """This method will run task 1. The ^VIX (CBOE Volatility Index) is a popular measure of the stock market's
    expectation of volatility based on the S&P 500 index options. In layman's terms, it is a fear index. """
    infoSeparator()
    start = datetime.datetime(2000, 1, 1)
    end = datetime.datetime(2022, 1, 1)
    print("Starting task 2: ")

    # Read in vix and spy using pd data reader
    spy = loadData(start, end, "SPY")
    vix = loadData(start, end, "^VIX")

    # Display information on spy and vix
    # print("Info on vix: \n")
    # print(vix.info())
    # print("Info on spy: \n")
    # print(spy.info())
    infoSeparator()

    # Plot graph of adjusted close price
    fig = plt.figure()
    max1 = max(vix['Adj Close'])
    vix_adj = vix['Adj Close']
    plt.plot(vix_adj.idxmax(), max1, 'ro', label="Max Value")
    plt.title("Adjusted Close Price of VIX")
    plt.xlabel("Date")
    plt.ylabel("Index Price (in Dollars)")
    plt.plot(vix['Adj Close'], 'green', label="Vix")
    plt.legend()
    plt.show()

    """
    The VIX is a measure of implied volatility, based on the prices of a basket of S&P 500 Index options with 30 days
    to expiration. By zooming into the graph, we see a huge spike around April of 2020. As many of you can guess or 
    even remember, that was around the time the United States went awol: people were buying all the toilet paper they 
    could find and the market was doing back-flips. Though, interestingly, we see that what happened at the beginning of 
    2020 shies in comparison to what happened in 2008 during the Great Recession.
    """

    infoSeparator()

    # Plot the adjusted close price of both SPY and VIX
    fig = plt.figure()
    plt.plot(vix['Adj Close'], 'r', label="VIX")
    plt.plot(spy['Adj Close'], 'g', label="SPY")
    plt.title("Adjusted Close Price of VIX and SPY ")
    plt.xlabel("Date")
    plt.ylabel("Price (in Dollars)")
    plt.legend()
    plt.show()

    infoSeparator()

    # Plot the normalized adjusted close price of spy and vix
    fig = plt.figure()
    vix_normalized = vix.apply(lambda x: x / x[0])
    spy_normalized = spy.apply(lambda x: x / x[0])
    plt.plot(vix_normalized['Adj Close'], 'r', label="VIX")
    plt.plot(spy_normalized['Adj Close'], 'g', label="SPY")
    plt.title("Normalized Adjusted Close Price of VIX and SPY")
    plt.xlabel("Date")
    plt.ylabel("Normalized Price")
    plt.legend()
    plt.show()

    # Calculate the correlation between daily return of vix and daily return of spy
    # Create new Daily Return columns in vix and spy df's
    vix['Daily Return'] = vix['Adj Close'].pct_change()
    spy['Daily Return'] = spy['Adj Close'].pct_change()

    # Sparse data into list of lists
    data = [spy['Daily Return'], vix['Daily Return']]
    headers = ["SPY Daily Return", "VIX Daily Return"]

    # Create new data frame with existing data
    df2 = pd.concat(data, axis=1, keys=headers)
    df2 = df2.reset_index()

    # Create heatmap
    sns.heatmap(df2.corr(), annot=True, fmt='.1f', cmap='Greens')
    plt.show()

    infoSeparator()

    data = [vix['Adj Close'], spy['Volume']]
    headers = ["VIX Adj Close", "SPY Volume"]

    new_data_frame = pd.concat(data, axis=1, keys=headers)
    new_data_frame = new_data_frame.reset_index()
    print(new_data_frame)

    print(new_data_frame.corr())
    sns.heatmap(new_data_frame.corr(), annot=True, fmt='.1f', cmap='Greens')
    plt.title('VIX Adjusted Close vs SPY Volume')
    plt.show()

    """Here we find some interesting results in our search for relationships between VIX and SPY. 
       - The VIX adjusted close value is moderately correlated to the SPY Volume. This makes sense because as the market 
           gets more volatile, more people jump and start buying OPTIONS.  
       - The 
       - 
       -   
    """

    # Compare SPY Adj Close to average mortgage interest rates
    mortgageInterestRates()

    # Calculate daily percentage moves of VIX index

# Create a Daily Return column in the spy df
# spy['Daily Return'] = spy['Adj Close'] - spy['Open']

# Create scatter plot for spy volume vs vix
# plt.title("SPY volume vs volatility")
# plt.xlabel("Adjusted Close Price for Vix")
# plt.ylabel("Volume of SPY Traded")
# plt.scatter(vix_adj_close_price, spy_volume)
# plt.show()


def mortgageInterestRates():
    # Read in data
    spy15 = pd.read_csv("MORTGAGE15US.csv")
    spy30_df = pd.read_csv("MORTGAGE30US.csv")

    # Set the start dates to 2000-01-07 (YEAR-MM-DD)
    dates_15 = spy15["DATE"][436:]
    dates_30 = spy30_df["DATE"][3:]

    # Plot the spy_30 before the fix
    plt.plot(dates_30, spy30_df['MORTGAGE30US'][3: ], 'r-', label="30 - Before Fix")

    # Plot the mortgages
    plt.plot(dates_15, spy15['MORTGAGE15US'][436: ], 'g-', label="15")
    plt.plot(dates_30, spy30_df['MORTGAGE30US'][3: ], 'b-', label="30")
    plt.plot([dates_30[606]], [spy30_df['MORTGAGE30US'][606]], "ko")
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()
