
import pandas as pd

def evaluate_profitability(df):

    findings = []

    latest = df.iloc[-1]

    margin = latest["NetProfitMargin"]
    profit = latest["NetProfit"]

    
    indicators = { 
        "NetProfitMargin": (
            "Net Profit Margin measures the percentage of money you make that doesn't go toward expenses. In other words, what percentage of revenue is actually yours. For example, if your Net Profit Margin is 12%, $12 of every $100 you make actually goes into your pocket."
        )
    }

    suggestions = {
            "ProfitabilityGeneral": (
                "Improving your business's profitability means you either decrease your expenses or increase your revenue. You can do this by: \n"
                "1) Increasing product contribution. Contribution is the profit each product makes for each sale. So increase the price to make more money per sale, but do it slowly to avoid losing too many sales. For example, if it costs $8 to make a pizza, and you're selling it for only $9, then increasing the price by $1 might improve your conteribution. \n"
                "2) Identifying recurring overhead. Overhead just means costs that aren't directly associated with making the products. So figure out some recurring payments your business is making that you might be able to lower, or remove altogether. For example, consider a cheaper WiFi provider if that is a significant cost, or cancel an unused subscription."
            ),
            "ProfitabilityLoss": (
                "Focus on reducing your costs to reach the break even point. There are two great ways to do this: \n "
                "1) Catch expense spikes. Separate your monthly expenses into major categories, such as payroll, rent, etc. Then identify which ones had the biggest growth rates, investigate causes, and try to reduce unneccessaary spending. For example, if your payroll spiked, the you might want to consider lower staffing if possible. \n "
                "2) Identify recurring overhead. Overhead just means costs that aren't directly associated with making the products. So figure out some recurring payments your business is making that you might be able to lower, or remove altogether. For example, consider a cheaper WiFi provider if that is a significant cost, or cancel an unused subscription."
            )
        }

    if pd.notna(margin):

        if margin >= 10:
            findings.append({
                "Type": "Strength",
                "Indicator": "Net Profit Margin", 
                "Definition": indicators["NetProfitMargin"],
                "Explanation": (
                    f"The business generated ${profit:,.2f} in net profit, leading to a net profit margin of {margin:,.2f}%. Currently, your net profit margin is above the 10%, the typical safe mark for most retail businesses."
                ),
                "Suggestions": suggestions["ProfitabilityGeneral"]

            })

        elif margin < 10:
            if profit > 0:
                findings.append({
                    "Type": "Concern",
                    "Indicator": "Net Profit Margin", 
                    "Definition": indicators["NetProfitMargin"],
                    "Explanation": (
                        f"The business generated ${profit:,.2f} in net profit, leading to a net profit margin of {margin:,.2f}%. Currently, your net profit margin sits below 10%, the typical safe mark for most retail businesses. Your profit is above zero, so you should focus on tryin to hit the 10% benchmark."
                    ),
                    "Suggestions": suggestions["ProfitabilityGeneral"]
                })

            elif profit == 0:
                findings.append({
                    "Type": "Concern",
                    "Indicator": "Net Profit Margin", 
                    "Definition": indicators["NetProfitMargin"],
                    "Explanation": (
                        f"The business generated ${profit:,.2f} in net profit, leading to a net profit margin of {margin:,.2f}%. Currently, your net profit margin sits below 10%, the typical safe mark for most retail businesses. Your profit is exactly zero, so you should focus on increasing it so that you begin to actually make money from the business."
                    ),
                    "Suggestions": suggestions["ProfitabilityGeneral"]
                })

            elif profit < 0:
                findings.append({
                    "Type": "Concern",
                    "Indicator": "Net Profit Margin", 
                    "Definition": indicators["NetProfitMargin"],
                    "Explanation": (
                        f"The business generated ${profit:,.2f} in net profit, leading to a net profit margin of {margin:,.2f}%. Currently, your net profit margin sits below 10%, the typical safe mark for most retail businesses. Your profit is below zero, meaning you are losing money in this business, so you should focus on reaching the break even point, when profit is exactly zero."
                    ),
                    "Suggestions": suggestions["ProfitabilityLoss"]
                })

    return findings