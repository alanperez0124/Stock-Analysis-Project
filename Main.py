import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Let's first read in the data from spy
    df = pd.read_csv("SPY.csv")

    print(df.head())

    # Let's look at some basic values of spy
    print(df.describe())




    # Ideas
    """
    - We can use the VIX to track volatility index and see how that relates to stock price performance
    - We can track Treasury values and average mortgage inerest rates at Bankrate.com or HSN.com. 
    - We can create heatmap showing correlation between interest rates and stock price performance. 
    - Plot the moving average (populat on trading view and such)
    
    """



if __name__ == "__main__":
    main()
