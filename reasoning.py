
import pandas as pd

def evaluate_profitability(df):

    findings = []

    latest = df.iloc[-1]

    if len(df) >= 2:
        previous = df.iloc[-2]  
    else: 
        None

    margin = latest["NetProfitMargin"]
    profit = latest["NetProfit"]

    # RULE 1: CURRENT PROFITABILITY

    if pd.notna(margin):

        if profit > 0:
            findings.append({
                "Type": "Strength",
                "Indicator(s)": "Profit",
                "Title": "Business is profitable",
                "Explanation": (
                    f"The business generated ${profit:,.2f} in net profit, meaning it's revenues were ${profit:,.2f} larger than it's expenses."
                )
            })

        elif profit < 0:
            findings.append({
                "Type": "Concern",
                "Indicator(s)": "Profit",
                "Title": "Business is profitable",
                "Explanation": (
                    f"The business generated ${profit:,.2f} in net profit, meaning it's revenues were ${profit:,.2f} larger than it's expenses."
                )
            })

        else:
            findings.append({
                "Type": "Information",
                "Title": "Business is breaking even",
                "Explanation": (
                    "Revenue equals expenses for the latest month, so neither."
                )
            })

    # RULE 2: PROFIT MARGIN MOVEMENT

    if previous is not None and pd.notna(margin):

        previous_margin = previous["NetProfitMargin"]

        if pd.notna(previous_margin):

            change = margin - previous_margin

            if change > 0:
                findings.append({
                    "Type": "Strength",
                    "Title": "Profit margin improved",
                    "Explanation": (
                        f"Net profit margin increased from "
                        f"{previous_margin:.2f}% to {margin:.2f}%, "
                        f"an improvement of {change:.2f} "
                        "percentage points."
                    )
                })

            elif change < 0:
                findings.append({
                    "Type": "Concern",
                    "Title": "Profit margin declined",
                    "Explanation": (
                        f"Net profit margin decreased from "
                        f"{previous_margin:.2f}% to {margin:.2f}%, "
                        f"a decline of {abs(change):.2f} "
                        "percentage points."
                    )
                })

    return findings
