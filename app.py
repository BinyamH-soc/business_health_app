import streamlit as st
import pandas as pd

from calculations import calculate_metrics, indicator_table

st.title("Ledger Labs")

st.subheader(
    "Financial Clarity, Made Accessible"
)

mode = st.radio(
    "Choose how to start:",
    ["Try a sample", "Upload your own CSV"]
)

df = None

if mode == "Try a sample":

    samples = {
        "Healthy IT Business": "healthy_it_support.csv",
        "Neutral Print Shop": "neutral_print_shop.csv",
        "Unhealthy Hobby Store": "unhealthy_homewares.csv"
    }

    selected = st.selectbox(
        "Choose a sample business:",
        list(samples.keys())
    )

    df = pd.read_csv(samples[selected])

    st.download_button(
    "Download Sample CSV",
    data=df.to_csv(index=False),
    file_name=samples[selected],
    mime="text/csv"
)

else:
    file = st.file_uploader(
        "Upload your monthly business financial data",
        type="csv"
    )

    if file is not None:
        df = pd.read_csv(file)

if df is not None:

    st.subheader("Raw Financial Data")

    st.dataframe(df, hide_index=True)
    
    calculated_df = calculate_metrics(df.copy())

    table = indicator_table(calculated_df)

    display_table = table.copy()

    display_table = display_table.replace(
        [float("inf"), float("-inf")],
        "N/A"
    )

    display_table = display_table.fillna("N/A")

    st.subheader("Financial Health Indicators")

    st.dataframe(
        display_table,
        hide_index=True,
        use_container_width=True
    )