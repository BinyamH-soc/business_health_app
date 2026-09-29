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

df["Net Profit Margin"] (
    df["Net Profit"] / df["Revenue"]
) * 100

#FINANCIAL HEALTH

df["Current Ratio"] = (
    df["CurrentAssets"] / df["CurrentLiabilities"]
)

df["Debt to Asset Ratio"] = (
    df["Debt"] / df["TotalAssets"]
) * 100

df["Revenue-Expense Growth Differential"] = (
    df["Revenue Growth (%)"]
    - df["Expense Growth (%)"]
)

#CUSTOMER HEALTH

df["Revenue per Customer"] = (
    df["Revenue"] / df["Customers"]
)

df["Purchases per Customer"] = (
    df["Orders"] / df["Customers"]
)

df["Profit per Customer"] = (
    df["Net Profit"] / df["Customers"]
)

#MARKETING EFFICIENCY

df["Revenue per Marketing Dollar"] = (
    df["Revenue"] / df["MarketingSpend"]
)

df["Marketing Spend as % of Revenue"] = (
    df["MarketingSpend"] / df["Revenue"]
) * 100

df["Marketing Spend per Order"] = (
    df["MarketingSpend"] / df["Orders"]
)

#OPERATIONAL EFFICIENCY

df["Revenue per Employee"] = (
    df["Revenue"] / df["Employees"]
)

df["Orders per Employee"] = (
    df["Orders"] / df["Employees"]
)

df["Revenue per Labour Hour"] = (
    df["Revenue"] / df["LabourHours"]
)



print(df)