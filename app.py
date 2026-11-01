import streamlit as st
import pandas as pd

from calculations import calculate_metrics, indicator_table

st.title("Ledger Labs")

st.write(
    "A catchy slogan here"
)

file = st.file_uploader(
    "Upload your monthly business financial data",
    type="csv"
)

if file is not None:
    df = pd.read_csv(file)

    df = calculate_metrics(df)

    table = indicator_table(df)

    st.subheader("Financial Health Indicators")

    st.dataframe(
        table,
        hide_index=True,
        use_container_width=True
    )