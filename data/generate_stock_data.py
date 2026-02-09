import pandas as pd
import numpy as np

dates = pd.date_range(start="2000-01-01", end="2017-12-31", freq='B')

np.random.seed(42)

open_price = np.random.uniform(100, 300, len(dates))
high_price = open_price + np.random.uniform(1, 10, len(dates))
low_price = open_price - np.random.uniform(1, 10, len(dates))
close_price = open_price + np.random.uniform(-5, 5, len(dates))

df = pd.DataFrame({
    "Date": dates,
    "Open": open_price,
    "High": high_price,
    "Low": low_price,
    "Close": close_price
})

df.to_csv("data/stock_data.csv", index=False)
print("Dataset generated successfully!")
