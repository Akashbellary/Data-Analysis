import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

def draw_plot():
    # Read the data from CSV file
    df = pd.read_csv('epa-sea-level.csv')

    # Perform linear regression for the first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create a scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Data')

    # Create a line plot using the linear regression equation
    years_extended = range(1880, 2051)
    plt.plot(years_extended, intercept + slope * years_extended, color='r', label='Linear Regression')

    # Perform linear regression for the second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, stderr_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Create a line plot for the recent years
    years_recent_extended = range(2000, 2051)
    plt.plot(years_recent_extended, intercept_recent + slope_recent * years_recent_extended, color='g', label='Linear Regression (2000-2050)')

    # Set plot labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create legend
    plt.legend()

    # Return the plot object
    return plt.gca()

# Uncomment the line below to display the plot
draw_plot()
