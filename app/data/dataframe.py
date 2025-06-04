import pandas as pd

mpg_data = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/mpg.csv"
)
mpg_data.dropna(inplace=True)
mpg_data["horsepower"] = pd.to_numeric(mpg_data["horsepower"])
