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

    spy = loadData(start, end, "SPY")

    # Examine the structure of this data as well as the first few values
    # print("Some info on the parameters: \n", spy.info())
    # print("\nThe first few values of spy: \n", spy.head())


    # Plot SPY's closing price
    # spy_adj_close_price = getParameter(spy) ############

    # plt.plot(spy_adj_close_price)
    # plt.show()

    # Plot the total volume over time
    # spy_volume = getParameter(spy, 'Volume')# ######################

    # plt.plot(spy_volume)
    # plt.title("Volume")
    # plt.show()

    # Task 1: Examine relationship between vix volatility index and spy
    runTask2(start, end)
    """
    Here we see an interesting result. First of all, our data is severely skewed with most of it being clustered in the 
    bottom left-hand corner. This is indicative of something, but I can't quite remember. Regardless of that, we do 
    a very feint positive linear relationship. We see that as the price of VIX increases (that is, as the stock market 
    gets more volatile, the number of shares traded increases.
    """

    # Task 2:




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


def runTask2(start, end):
    """This method will run task 1. The ^VIX (CBOE Volatility Index) is a popular measure of the stock market's
    expectation of volatility based on the S&P 500 index options. In layman's terms, it is a fear index. """
    infoSeparator()
    print("Starting task 2: ")

    # Read in vix and spy using pd data reader
    spy = loadData(start, end, "SPY")
    vix = loadData(start, end, "^VIX")

    # Display info on vix
    print("Info on vix: \n")
    print(vix.info())
    print("Info on spy: \n")
    print(spy.info())
    # print("First few values of vix: \n", vix.head())

    # Create data frame for Close parameter of vix
    vix_adjclose_df = getParameter(vix, 'Adj Close')

    # Plot adjusted close price data
    plt.title("Adjusted close price of VIX Over Past 5 Years")
    plt.xlabel("Date")
    plt.ylabel("Index Price (in Dollars)")
    plt.plot(vix_adjclose_df)
    plt.show()

    """The VIX is a measure of implied volatility, based on the prices of a basket of S&P 500 Index options with 30 days
    to expiration. By zooming into the graph, we see a huge spike around April of 2020. As many of you can guess or 
    even remember, that was around the time the United States went awol: people were buying all the toilet paper they 
    could find and the market was doing back-flips. blah blah blah. """

    infoSeparator()

    # Explore the relationship between VIX and SPY
    data = [ vix['Adj Close'], spy['Adj Close'], spy['Volume']]
    headers = ["VIX Adj Close", "SPY Adj Close", "SPY Volume"]

    new_data_frame = pd.concat(data, axis=1, keys=headers)

    print(new_data_frame.corr())
    sns.heatmap(new_data_frame.corr(), annot=True, fmt='.1f', cmap='Greens')
    plt.show()


   # Create a Daily Return column in the spy df
    # spy['Daily Return'] = spy['Adj Close'] - spy['Open']


    # Create scatter plot for spy volume vs vix
    # plt.title("SPY volume vs volatility")
    # plt.xlabel("Adjusted Close Price for Vix")
    # plt.ylabel("Volume of SPY Traded")
    # plt.scatter(vix_adj_close_price, spy_volume)
    # plt.show()


if __name__ == "__main__":
    main()
