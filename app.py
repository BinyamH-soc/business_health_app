import pandas as pd

df = pd.read_csv("data_1.csv")

# BASE CALCULATIONS

df["Net Profit"] = df["Revenue"] - df["Expenses"]

previous_revenue = df["Revenue"].shift(1)
previous_expenses = df["Expenses"].shift(1)
df["Expense Growth Pecentage"] = (
    (df["Expenses"] - previous_expenses) / previous_expenses * 100
)

# FINANCIAL FROWTH

df ["Revenue Growth Percentage"] = (
    (df["Revenue"] - previous_revenue) / previous_revenue * 100
)

df["Revenue per Dollar Expense"] = (
    df["Revenue"] / df["Expenses"]
)

df["Net Profit Margin"] = (
    df["Net Profit"] / df["Revenue"]
) * 100

#FINANCIAL HEALTH

df["Current Ratio"] = (
    df["CurrentAssets"] / df["CurrentLiabilities"]
)

df["Debt to Asset Ratio"] = (
    df["Debt"] / df["Assets"]
) * 100

df["Revenue-Expense Growth Differential"] = (
    df["Revenue Growth Percentage"]
    - df["Expense Growth Pecentage"]
)

#CUSTOMER HEALTH

df["Revenue per Customer"] = (
    df["Revenue"] / df["TotalCustomers"]
)

df["Purchases per Customer"] = (
    df["Orders/Purchases"] / df["TotalCustomers"]
)

df["Profit per Customer"] = (
    df["Net Profit"] / df["TotalCustomers"]
)

#MARKETING EFFICIENCY

df["Revenue per Marketing Dollar"] = (
    df["Revenue"] / df["MarketingSpend"]
)

df["Marketing Spend as % of Revenue"] = (
    df["MarketingSpend"] / df["Revenue"]
) * 100

df["Marketing Spend per Order"] = (
    df["MarketingSpend"] / df["Orders/Purchases"]
)

#OPERATIONAL EFFICIENCY

df["Revenue per Employee"] = (
    df["Revenue"] / df["NumberOfEmployees"]
)

df["Orders per Employee"] = (
    df["Orders/Purchases"] / df["NumberOfEmployees"]
)

df["Revenue per Labour Hour"] = (
    df["Revenue"] / df["LabourHours"]
)

df = df.round(2)

print(df)