
# app.py
import streamlit as st
import pandas as pd

from agents import CUSTOMER, TRANSACTIONS, supervisor_agent

st.set_page_config(
    page_title="AI Banking Assistant",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 AI Banking Assistant")
st.write("Multi-Agent Banking System")

st.warning(
    "Educational demo only. Do not enter real banking details."
)

st.sidebar.header("Demo Customer")
st.sidebar.write("Customer ID:", CUSTOMER["customer_id"])
st.sidebar.write("Name:", CUSTOMER["name"])
st.sidebar.metric(
    "Account Balance",
    f"₹{CUSTOMER['balance']:,.2f}"
)

st.subheader("Ask Your Banking Question")

question = st.text_input(
    "Enter your question",
    placeholder="Example: What is my balance?"
)

income = st.number_input(
    "Monthly income (for loan demo)",
    min_value=0,
    max_value=10000000,
    value=30000,
    step=1000
)

if st.button("Submit Question"):
    if not question.strip():
        st.error("Please enter a question.")
    else:
        result = supervisor_agent(question, income)

        st.subheader("Agent Response")
        st.write(result["response"])

        st.info(f"Handled by: {result['agent']}")

        with st.expander("Routing details"):
            st.write("User question:", question)
            st.write("Selected agent:", result["agent"])
            st.write("Method: Keyword-based routing")

st.divider()

st.subheader("Demo Transaction History")
st.dataframe(
    pd.DataFrame(TRANSACTIONS),
    use_container_width=True,
    hide_index=True
)

st.caption("All account and transaction information is fictional.")
