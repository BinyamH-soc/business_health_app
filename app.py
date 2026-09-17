import pandas as pd

data = {
    "Campaign": ["Email", "Search", "Flyers"],
    "Spend": [500, 1200, 600],
    "Revenue": [3200, 4700, 950],
    "Customers": [40, 72, 18]
}

df = pd.DataFrame(data)
df["ROAS"] = df["Revenue"] / df["Spend"]
df["CAC"] = df["Spend"] / df["Customers"]

print(df)