import streamlit as st
import plotly.express as px

from utils.db import run_query


st.title("📊 Executive Overview")

df = run_query(
    """
    SELECT *
    FROM MART_COUNTRY_ANALYTICS
    """
)

countries = df["COUNTRY_CODE"].nunique()
years = df["YEAR"].nunique()

latest_year = int(df["YEAR"].max())

latest_df = df[
    df["YEAR"] == latest_year
]

global_gdp = latest_df["GDP"].sum()
global_population = latest_df["POPULATION"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Countries",
    f"{countries:,}"
)

col2.metric(
    "Years",
    f"{years:,}"
)

col3.metric(
    "Global GDP",
    f"${global_gdp:,.0f}"
)

col4.metric(
    "Global Population",
    f"{global_population:,.0f}"
)

st.divider()

st.subheader("Top GDP Countries")

top_gdp = (
    latest_df
    .sort_values(
        "GDP",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top_gdp,
    x="COUNTRY_NAME",
    y="GDP"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("GDP Per Capita Leaders")

leaders = (
    latest_df
    .sort_values(
        "GDP_PER_CAPITA",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    leaders,
    x="COUNTRY_NAME",
    y="GDP_PER_CAPITA"
)

st.plotly_chart(
    fig,
    use_container_width=True
)