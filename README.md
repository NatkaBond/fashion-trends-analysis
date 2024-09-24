
# Fashion Trends Analysis in North Carolina and Charlotte

This project analyzes the popularity of several luxury fashion brands, including Burberry, Gucci, Yves Saint Laurent, Louis Vuitton, and Alexander McQueen, using Google Trends data. The analysis focuses on North Carolina (NC) and Charlotte specifically, allowing for insights into regional interest in these brands over the past five years.

## Project Overview

This project uses the `pytrends` library, which is an unofficial Python API for Google Trends. We gather data for five fashion brands and visualize the search interest over time. The data is processed and saved as a CSV file for further analysis, and a line plot is generated to visualize the relative popularity of these brands.

### Key Components:
1. **Google Trends Data Extraction**:
   - The data was fetched using the `pytrends` API.
   - The project focuses on North Carolina (`US-NC`) and Charlotte region.
   - The timeframe for the data is the past five years (`today 5-y`).

2. **Brands Analyzed**:
   - **Burberry**
   - **Gucci**
   - **Yves Saint Laurent**
   - **Louis Vuitton**
   - **Alexander McQueen**

3. **Processes**:
   - **Fetching Data**: The script uses `pytrends` to get search interest data for the brands over time.
   - **Saving Data**: The fetched data is saved into a CSV file (`fashion_trends_nc_charlotte.csv`).
   - **Data Visualization**: A line plot is generated using `matplotlib` to visualize the popularity of each brand over the past five years.

## Files in the Repository

- `fetch_trends.py`: The Python script that fetches Google Trends data for the selected brands in North Carolina and Charlotte.
- `fashion_trends_nc_charlotte.csv`: The CSV file that contains the Google Trends data for each brand over the past five years.
- `fashion_trends_nc_charlotte.png`: A line plot image that visualizes the trends for all five brands over time.
  
## Data Analysis

The data fetched from Google Trends is normalized between 0 and 100, where 100 represents the peak search interest for a specific brand during the timeframe. This analysis helps to compare the relative interest of consumers in North Carolina and Charlotte for these five luxury fashion brands.

### Insights:
- Track how interest in each brand has changed over the past five years.
- Compare the popularity of each brand in the region.
- Understand regional trends for luxury fashion brands.


## Conclusion

This project provides a clear and effective way to analyze and visualize Google Trends data for luxury fashion brands. It helps in understanding consumer interest in different regions, which can be useful for fashion brands, marketers, and analysts.

