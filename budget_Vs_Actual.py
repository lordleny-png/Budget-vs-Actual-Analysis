
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Budget vs Actual Analysis",
    page_icon="📊",
    layout="wide"
)

# Custom design

# Clean and readable dashboard design
st.markdown("""
<style>
.stApp {
    background-color: #F4F7FB;
    color: #243047;
}

[data-testid="stSidebar"] {
    background-color: #E8EEF7;
}

[data-testid="stSidebar"] * {
    color: #243047 !important;
}

h1, h2, h3, p, label {
    color: #243047;
}

div[data-testid="stMetric"] {
    background-color: #FFFFFF;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #D8E0EC;
    box-shadow: 0 2px 8px rgba(20, 33, 61, 0.08);
}

div[data-testid="stMetricLabel"] {
    color: #52627A !important;
}

div[data-testid="stMetricValue"] {
    color: #14213D !important;
}

.stAlert {
    color: #243047 !important;
}
</style>
""", unsafe_allow_html=True)


# Header
st.title("📊 Budget vs Actual Analysis")
st.caption("Financial performance | Budget monitoring | Business insights")

# Load data
df = pd.read_csv("Financial analysis_Data Set.csv")
df["Month"] = pd.to_datetime(df["Month"])

categories = [
    c for c in df.columns
    if c not in ["Month", "Expenses"]
]

# Sidebar filters
st.sidebar.title("⚙️ Dashboard Filters")

months = sorted(df["Month"].unique())
selected_months = st.sidebar.multiselect(
    "Select months",
    months,
    default=months,
    format_func=lambda x: x.strftime("%b %Y")
)

selected_categories = st.sidebar.multiselect(
    "Select cost categories",
    categories,
    default=categories
)

if not selected_months or not selected_categories:
    st.warning(
        "Please select at least one month and one cost category "
        "using the filters in the left sidebar."
    )
    st.stop()

# Filter data
filtered = df[df["Month"].isin(selected_months)]
budget = filtered[filtered["Expenses"] == "Budget"].set_index("Month")
actual = filtered[filtered["Expenses"] == "Actual"].set_index("Month")

budget_total = budget[selected_categories].sum().sum()
actual_total = actual[selected_categories].sum().sum()
variance = actual_total - budget_total
execution = actual_total / budget_total * 100 if budget_total else 0

# KPI cards
st.subheader("📌 Financial Overview")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Budget", f"{budget_total:,.0f}")
c2.metric("Actual Expenses", f"{actual_total:,.0f}")
c3.metric("Variance", f"{variance:,.0f}")
c4.metric("Budget Execution", f"{execution:.2f}%")

# Monthly comparison
st.subheader("📅 Monthly Budget vs Actual")

monthly = pd.DataFrame({
    "Month": budget.index,
    "Budget": budget[selected_categories].sum(axis=1).values,
    "Actual": actual[selected_categories].sum(axis=1).values
})

monthly_chart = px.bar(
    monthly, x="Month", y=["Budget", "Actual"],
    barmode="group",
    color_discrete_sequence=["#4361EE", "#F4A261"],
    template="plotly_white"
)
monthly_chart.update_layout(
    legend_title_text="Financial Measure",
    xaxis_title="Month",
    yaxis_title="Amount",
    margin=dict(t=25, b=20)
)
st.plotly_chart(monthly_chart, use_container_width=True)

# Monthly Variance Trend
st.subheader("📈 Monthly Spending Variance")

monthly["Variance"] = monthly["Actual"] - monthly["Budget"]

monthly["Status"] = monthly["Variance"].apply(
    lambda x: "Overspending" if x > 0
    else "Under Budget" if x < 0
    else "On Budget"
)

variance_chart = px.bar(
    monthly,
    x="Month",
    y="Variance",
    color="Status",
    color_discrete_map={
        "Overspending": "#E63946",
        "Under Budget": "#2A9D8F",
        "On Budget": "#4361EE"
    },
    template="plotly_white",
    title="Actual Expenses minus Budget"
)

variance_chart.update_layout(
    xaxis_title="Month",
    yaxis_title="Variance",
    showlegend=True
)

st.plotly_chart(variance_chart, use_container_width=True)



# Category analysis
st.subheader("💰 Variance by Cost Category")

category_budget = budget[selected_categories].sum()
category_actual = actual[selected_categories].sum()
category_variance = category_actual - category_budget

category_df = pd.DataFrame({
    "Category": selected_categories,
    "Variance": [category_variance[c] for c in selected_categories]
})

category_df["Status"] = category_df["Variance"].apply(
    lambda x: "Overspending" if x > 0
    else "Under Budget" if x < 0
    else "On Budget"
)

category_chart = px.bar(
    category_df, x="Category", y="Variance",
    color="Status",
    color_discrete_map={
        "Overspending": "#E63946",
        "Under Budget": "#2A9D8F",
        "On Budget": "#4361EE"
    },
    template="plotly_white"
)
category_chart.update_layout(
    xaxis_title="Cost Category",
    yaxis_title="Variance",
    showlegend=True
)
st.plotly_chart(category_chart, use_container_width=True)

# Summary table
st.subheader("📋 Detailed Category Summary")

summary = pd.DataFrame({
    "Budget": category_budget,
    "Actual": category_actual,
    "Variance": category_variance
})
summary["Variance (%)"] = (
    summary["Variance"] / summary["Budget"].replace(0, float("nan")) * 100
)
st.dataframe(summary.round(2), use_container_width=True)

# Business insights
st.subheader("🔎 Business Insights")

overruns = category_variance[category_variance > 0]

if not overruns.empty:
    highest = overruns.idxmax()
    st.warning(
        f"Review **{highest}**: it has the largest overspending "
        f"of {overruns[highest]:,.0f}."
    )
else:
    st.success("No selected category exceeded its budget.")

if variance < 0:
    st.info(f"Actual expenses are {abs(variance):,.0f} below the selected budget.")
elif variance > 0:
    st.warning(f"Actual expenses exceed the selected budget by {variance:,.0f}.")
else:
    st.success("Actual expenses match the selected budget.")
