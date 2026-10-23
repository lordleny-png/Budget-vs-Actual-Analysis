
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Budget vs Actual Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Budget vs Actual Analysis")
st.caption("Financial performance | Budget monitoring | Business insights")

# Load the dataset automatically
df = pd.read_csv("budget_vs_actual.csv")

budget = df[df["Expenses"] == "Budget"].set_index("Month")
actual = df[df["Expenses"] == "Actual"].set_index("Month")

categories = [
    c for c in df.columns
    if c not in ["Month", "Expenses"]
]

budget_total = budget[categories].sum().sum()
actual_total = actual[categories].sum().sum()
variance = actual_total - budget_total
execution_rate = actual_total / budget_total * 100

# KPI cards
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Budget", f"{budget_total:,.0f}")
c2.metric("Actual Expenses", f"{actual_total:,.0f}")
c3.metric("Variance", f"{variance:,.0f}")
c4.metric("Budget Execution", f"{execution_rate:.2f}%")

# Monthly comparison
st.subheader("📅 Monthly Budget vs Actual")

monthly = pd.DataFrame({
    "Month": budget.index,
    "Budget": budget[categories].sum(axis=1).values,
    "Actual": actual[categories].sum(axis=1).values
})

monthly["Month"] = pd.to_datetime(monthly["Month"])

chart = px.bar(
    monthly, x="Month", y=["Budget", "Actual"],
    barmode="group",
    color_discrete_sequence=["royalblue", "orange"],
    title="Monthly Spending Comparison"
)
st.plotly_chart(chart, use_container_width=True)

# Category variance
st.subheader("💰 Variance by Cost Category")

category_budget = budget[categories].sum()
category_actual = actual[categories].sum()
category_variance = category_actual - category_budget

category_df = pd.DataFrame({
    "Category": categories,
    "Variance": category_variance.values
})

category_df["Status"] = category_df["Variance"].apply(
    lambda x: "Overspending" if x > 0
    else "Under Budget" if x < 0
    else "On Budget"
)

chart = px.bar(
    category_df, x="Category", y="Variance",
    color="Status",
    color_discrete_map={
        "Overspending": "red",
        "Under Budget": "green",
        "On Budget": "royalblue"
    },
    title="Spending Variance by Category"
)
st.plotly_chart(chart, use_container_width=True)

# Summary table
st.subheader("📋 Category Summary")

summary = pd.DataFrame({
    "Budget": category_budget,
    "Actual": category_actual,
    "Variance": category_variance,
    "Variance (%)": category_variance / category_budget * 100
})

st.dataframe(summary.round(2), use_container_width=True)

# Business insights
st.subheader("🔎 Key Business Insights")

st.write(
    f"Overall budget execution was {execution_rate:.2f}%."
)

st.write(
    f"Total spending was {abs(variance):,.0f} "
    + ("below budget." if variance < 0 else "above budget.")
)

highest_overrun = category_variance.idxmax()

if category_variance.max() > 0:
    st.warning(
        f"Review {highest_overrun}: it has the largest "
        "positive budget variance."
    )
else:
    st.success("No cost category exceeded its budget.")
