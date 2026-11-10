import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # create axis
    fig, ax = plt.subplots()

    # Create scatter plot
    ax.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    reg1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = pd.Series(range(df["Year"].min(), 2051))
    ax.plot(x1, reg1.intercept + reg1.slope * x1)

    # Create second line of best fit
    reg2 = linregress(
        df[df["Year"] >= 2000]["Year"],
        df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"],
    )
    x2 = pd.Series(range(2000, 2051))
    ax.plot(x2, reg2.intercept + reg2.slope * x2)

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
