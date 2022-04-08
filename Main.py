import pandas as pd
import matplotlib.pyplot as plt
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
    vix = loadData(start, end, "VIX")

    print(vix.info())

    vix_adj_close_price = getParameter(vix, 'Adj Close')


    print("First few values of vix: \n", vix)


    # vix_volume = getParameter(vix, 'Volume')

    plt.title("SPY volume vs volatility")
    plt.plot(spy_volume, vix_adj_close_price)
    plt.show()


    # Ideas
    """
    - We can use the VIX to track volatility index and see how that relates to stock price performance
    - We can track Treasury values and average mortgage inerest rates at Bankrate.com or HSN.com. 
    - We can create heatmap showing correlation between interest rates and stock price performance. 
    - Plot the moving average (populat on trading view and such)
    
    """


def loadData(start, end, stock):
    return web.DataReader(stock, 'yahoo', start, end)


def getParameter(stock, parameter='Adj Close'):
    # Assert that the object passed is a data frame
    assert isinstance(stock, pd.DataFrame), "Stock passed me be a data frame"

    # Truncate the values we want
    truncated_stock_values = stock.truncate()[parameter]

    return truncated_stock_values


if __name__ == "__main__":
    main()
