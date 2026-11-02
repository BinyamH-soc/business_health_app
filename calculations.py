import pandas as pd

def calculate_metrics(df):

    # BASE CALCULATIONS

    df["NetProfit"] = df["Revenue"] - df["Expenses"]

    revenue_decline = 0.20
    average_monthly_expenses = df["Expenses"].rolling(window=12, min_periods=1).mean()
    previous_debt = df["Debt"].shift(1)
    previous_revenue = df["Revenue"].shift(1)
    previous_expenses = df["Expenses"].shift(1)
    previous_profit = df["NetProfit"].shift(1)  

    # Profitability

    df["NetProfit"] = (
        df["Revenue"] - df["Expenses"]
    )

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

    return df


def indicator_table(df):

    indicators = [
        "Net Profit Margin",
        "Net Profit Growth",
        "Revenue Growth",
        "Expense Growth",
        "Current Ratio",
        "Working Capital",
        "Debt Asset Ratio",
        "Debt Growth",
        "Profit Volatility",
        "Stress Test"
    ]

    latest = df.iloc[-1]

    table = pd.DataFrame({
        "Indicator": indicators,
        "Latest Month": [latest[name] for name in indicators]
    })

    table["Previous Month"] = [
        df[metric].iloc[-2] if len(df) >= 2 else float("nan")
        for metric in indicators
    ]

    table["3 Month Average"] = [
        df[metric].tail(3).mean() if len(df) >= 3
        else float("nan")
        for metric in indicators
    ]

    table["12 Month Average"] = [
        df[metric].tail(12).mean() if len(df) >= 12
        else float("nan")
        for metric in indicators
    ]

    return table.round(2)
