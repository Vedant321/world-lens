import streamlit as st
import plotly.express as px

from utils.db import run_query


st.title("⚖️ Country Comparison")

countries = run_query(
    """
    SELECT DISTINCT country_name
    FROM DIM_COUNTRY
    ORDER BY country_name
    """
)

col1, col2 = st.columns(2)

country_a = col1.selectbox(
    "Country A",
    countries["COUNTRY_NAME"]
)

country_b = col2.selectbox(
    "Country B",
    countries["COUNTRY_NAME"],
    index=1
)

df = run_query(
    f"""
    SELECT *
    FROM MART_COUNTRY_ANALYTICS
    WHERE country_name IN (
        '{country_a}',
        '{country_b}'
    )
    ORDER BY year
    """
)

fig = px.line(
    df,
    x="YEAR",
    y="GDP",
    color="COUNTRY_NAME",
    title="GDP Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.line(
    df,
    x="YEAR",
    y="POPULATION",
    color="COUNTRY_NAME",
    title="Population Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)