import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import numpy as np



def main():
    # Let's first read in the data from spy
    df = pd.read_csv("SPY.csv")

    print(df.head())

    # Let's look at some basic values of spy
    print(df.describe())

    # Method 2 of reading data
    start = datetime.datetime(2012, 1, 1)
    end = datetime.datetime(2017, 1, 1)

    tesla = web.DataReader("TSLA", "yahoo", start, end)

    print(tesla.head())





    # Ideas
    """
    - We can use the VIX to track volatility index and see how that relates to stock price performance
    - We can track Treasury values and average mortgage inerest rates at Bankrate.com or HSN.com. 
    - We can create heatmap showing correlation between interest rates and stock price performance. 
    - Plot the moving average (populat on trading view and such)
    
    """



if __name__ == "__main__":
    main()
