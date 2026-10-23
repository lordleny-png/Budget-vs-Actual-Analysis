
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Budget vs Actual", page_icon="📊", layout="wide")

st.title("📊 Budget vs Actual Analysis")
st.caption("Monitor spending, compare budgets, and identify variances.")

uploaded_file = st.file_uploader("Upload your budget dataset (CSV)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    budget = df[df["Expenses"] == "Budget"].set_index("Month")
    actual = df[df["Expenses"] == "Actual"].set_index("Month")

    categories = [c for c in df.columns if c not in ["Month", "Expenses"]]
    budget_total = budget[categories].sum().sum()
    actual_total = actual[categories].sum().sum()
    variance = actual_total - budget_total

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Budget", f"{budget_total:,.0f}")
    c2.metric("Actual Expenses", f"{actual_total:,.0f}")
    c3.metric("Variance", f"{variance:,.0f}")
    c4.metric("Budget Execution", f"{actual_total / budget_total * 100:.2f}%")

    monthly_budget = budget[categories].sum(axis=1)
    monthly_actual = actual[categories].sum(axis=1)

    monthly = pd.DataFrame({
        "Month": monthly_budget.index,
        "Budget": monthly_budget.values,
        "Actual": monthly_actual.values
    })

    st.subheader("Monthly Budget vs Actual")
    monthly_chart = px.bar(
        monthly, x="Month", y=["Budget", "Actual"],
        barmode="group", color_discrete_sequence=["royalblue", "orange"]
    )
    st.plotly_chart(monthly_chart, use_container_width=True)

    category_budget = budget[categories].sum()
    category_actual = actual[categories].sum()
    category_variance = category_actual - category_budget

    st.subheader("Variance by Cost Category")
    category_df = pd.DataFrame({
        "Category": categories,
        "Variance": category_variance.values
    })
    category_df["Status"] = category_df["Variance"].apply(
        lambda x: "Overspending" if x > 0 else "Under Budget" if x < 0 else "On Budget"
    )

    category_chart = px.bar(
        category_df, x="Category", y="Variance", color="Status",
        color_discrete_map={
            "Overspending": "red",
            "Under Budget": "green",
            "On Budget": "royalblue"
        }
    )
    st.plotly_chart(category_chart, use_container_width=True)

    st.subheader("Category Summary")
    summary = pd.DataFrame({
        "Budget": category_budget,
        "Actual": category_actual,
        "Variance": category_variance,
        "Variance (%)": (category_variance / category_budget * 100)
    })
    st.dataframe(summary.round(2), use_container_width=True)

else:
    st.info("Upload your CSV file to view the dashboard.")

