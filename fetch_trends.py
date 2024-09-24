from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define search terms
brands = ["Burberry", "Gucci", "Yves Saint Laurent", "Louis Vuitton", "Alexander McQueen"]

# Add a delay to avoid rate limiting
import time
time.sleep(5)

# Fetch data for North Carolina
try:
    pytrends.build_payload(brands, cat=0, timeframe='today 5-y', geo='US-NC', gprop='')
    data = pytrends.interest_over_time()
    print(data.head())

    # Save the data to a CSV file
    data.to_csv('fashion_trends_nc_charlotte.csv')

    # Plot data
    data.plot(figsize=(10, 6))
    plt.title('Google Trends of Fashion Brands in NC and Charlotte')
    plt.xlabel('Date')
    plt.ylabel('Popularity Index')
    plt.show()


except Exception as e:
    print(f"An error occurred: {e}")
