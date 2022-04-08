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
    print("Some info on the parameters: \n", spy.info())
    print("\nThe first few values of spy: \n", spy.head())

    # Plot SPY's closing price
    spy_adj_close_price = getParameter(spy)

    # plt.plot(spy_adj_close_price)
    # plt.show()

    # Plot the total volume over time
    spy_volume = getParameter(spy, 'Volume')

    # plt.plot(spy_volume)
    # plt.title("Volume")
    # plt.show()

    # Task 1: Examine relationship between vix volatility index and spy
    runTask1(start, end)
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


def getParameter(stock, parameter='Adj Close'):
    # Assert that the object passed is a data frame
    assert isinstance(stock, pd.DataFrame), "Stock passed me be a data frame"

    # Truncate the values we want
    truncated_stock_values = stock.truncate()[parameter]

    return truncated_stock_values


def runTask1(start, end):
    """This method will run task 1. The ^VIX (CBOE Volatility Index) is a popular measure of the stock market's
    expectation of volatility based on the S&P 500 index options. In layman's terms, it is a fear index. """
    # Read in vix csv file
    # vix = pd.read_csv("VIX.csv")
    spy = loadData(start, end, "SPY")
    vix = loadData(start, end, "^VIX")

    # Create df for spy volume
    spy_volume = spy['Volume']

    # Create a Daily Return column in the spy df
    # spy['Daily Return'] = spy['Adj Close'] - spy['Open']

    # Display info on vix
    print("Info on vix: \n")
    print(vix.info())
    print("First few values of vix: \n", vix.head())

    # Create univariate distribution of observations
    plt.hist(spy['Volume'])
    plt.show()

    # Get adj close parameter for vix
    vix_adj_close_price = getParameter(vix)

    # Display the adjusted close price for vix
    # plt.title("Adjusted Close Price of VIX Over Past 5 Years")
    # plt.xlabel("Date")
    # plt.ylabel("Index Price (in dollars)")
    # plt.plot(vix_adj_close_price)
    # plt.show()

    # Create scatter plot for spy volume vs vix
    # plt.title("SPY volume vs volatility")
    # plt.xlabel("Adjusted Close Price for Vix")
    # plt.ylabel("Volume of SPY Traded")
    # plt.scatter(vix_adj_close_price, spy_volume)
    # plt.show()


def task2():
    # # Concatenate the two columns to find correlation
    # print("\n First few values: ")
    #
    # data = [spy['Adj Close'], vix['Volume']]
    #
    # df = pd.concat(data)
    # df = df.reset_index()
    #
    # df = df[['Date', 'Adj Close', 'Volume']]
    #
    # print(df.head())
    return 2


    # Now that we have a general idea of the relationship, we will create a heat map for this

if __name__ == "__main__":
    main()
