import pandas as pd

df = pd.read_csv("data_1.csv")

# BASE CALCULATIONS

df["NetProfit"] = df["Revenue"] - df["Expenses"]

revenue_decline = 0.20
average_monthly_expenses = df["Expenses"].rolling(window=12, min_periods=1).mean()
previous_debt = df["Debt"].shift(1)
previous_revenue = df["Revenue"].shift(1)
previous_expenses = df["Expenses"].shift(1)
previous_profit = df["NetProfit"].shift(1)

# Profitability

df["NetProfitMargin"] = (
    df["NetProfit"] / df["Revenue"]
) * 100

df["NetProfitGrowth"] = (
    (df["NetProfit"] - previous_profit) / previous_profit * 100
)

# Growth

df ["RevenueGrowth"] = (
    (df["Revenue"] - previous_revenue) / previous_revenue * 100
)

df ["ExpenseGrowth"] = (
    (df["Expenses"] - previous_expenses) / previous_expenses * 100
)

previous_revenuegrowth = df["RevenueGrowth"].shift(1)
previous_expensegrowth = df["ExpenseGrowth"].shift(1)

df ["RevenueExpenseDifferential"] = (
    df["RevenueGrowth"] - df["ExpenseGrowth"]
)

df["RevenueGrowthAcceleration"] = (
    df ["RevenueGrowth"] - previous_revenuegrowth
)

df["ExpenseGrowthAcceleration"] = (
    df ["ExpenseGrowth"] - previous_expensegrowth
)

# Liquidity

df["CurrentRatio"] = (
    df["CurrentAssets"] / df["CurrentLiabilities"]
)

df["WorkingCapital"] = (
    df["CurrentAssets"] - df["CurrentLiabilities"]
)

# Debt

df["DebtAssetRatio"] = (
    (df["Liabilities"] / df["Assets"]) * 100
) 

df["DebtGrowth"] = (
    (df["Debt"] - previous_debt) / previous_debt * 100
) 

# Financial Resiliency

#df["CashReserveCoverage"] = (
 #   df["CashBalance"] / df["Expenses"]
#)

df["ProfitVolatility"] = (
    df["NetProfit"]
    .rolling(window=12, min_periods=3)
    .std(ddof=0)
)

df["StressTest"] = (
    (df["Revenue"] * (1 - revenue_decline)) - df["Expenses"]
)

#print(df)

indicators = [
    "NetProfitMargin",
    "NetProfitGrowth",
    "RevenueGrowth",
    "ExpenseGrowth",
    "CurrentRatio",
    "WorkingCapital",
    "DebtAssetRatio",
    "DebtGrowth",
    "ProfitVolatility",
    "StressTest"
]

latest = df.iloc[-1]

table = pd.DataFrame({
    "Indicator": indicators,
    "Latest Value": [latest[name] for name in indicators]
})

print(table.round(2).to_string(index=False))
