
import pandas as pd

from calculations import calculate_metrics
from reasoning import evaluate_profitability

# Load sample business data
df = pd.read_csv("data_1.csv")

# Calculate financial indicators
df = calculate_metrics(df)

# Evaluate profitability
findings = evaluate_profitability(df)

# Display results
for finding in findings:

    print("\nINDICATOR:", finding["Indicator"])

    print("TYPE:", finding["Type"])

    print("DEFINITION:", finding["Definition"])

    print("EXPLANATION:", finding["Explanation"])

    print("SUGGESTIONS:", finding["Suggestions"])

    print("-" * 60)

    
# TEST DIFFERENT PROFITABILITY SCENARIOS

scenarios = {
    "Strong Profit": (15, 1500),
    "Low Profit": (5, 500),
    "Break Even": (0, 0),
    "Operating Loss": (-10, -1000)
}

for name, (margin, profit) in scenarios.items():

    test_df = pd.DataFrame({
        "NetProfitMargin": [margin],
        "NetProfit": [profit]
    })

    findings = evaluate_profitability(test_df)

    print("\nSCENARIO:", name)

    for finding in findings:
        print("TYPE:", finding["Type"])
        print("EXPLANATION:", finding["Explanation"])
        print("SUGGESTIONS:", finding["Suggestions"])

