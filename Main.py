import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import numpy as np


def main():
    # Select dates for stock exploration
    start = datetime.datetime(2012, 1, 1)
    end = datetime.datetime(2022, 1, 1)

    spy = loadData(start, end, "SPY")

    # Examine the structure of this data
    print(spy.info())

    # Show the first few values
    print(spy.head())

    # Plot SPY's closing price
    x = getAdjustedClosingPrice(spy)

    plt.plot(x)
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


def getAdjustedClosingPrice(stock, parameter='Adj Close'):
    # Assert that the object passed is a data frame
    assert isinstance(stock, pd.DataFrame), "Stock passed me be a data frame"

    # Truncate the values we want
    truncated_stock_values = stock.truncate()[parameter]

    return truncated_stock_values


if __name__ == "__main__":
    main()
