import streamlit as st
import plotly.express as px

from utils.db import run_query


st.title("🌎 Country Explorer")

countries = run_query(
    """
    SELECT DISTINCT country_name
    FROM DIM_COUNTRY
    ORDER BY country_name
    """
)

selected_country = st.selectbox(
    "Select Country",
    countries["COUNTRY_NAME"]
)

df = run_query(
    f"""
    SELECT *
    FROM MART_COUNTRY_ANALYTICS
    WHERE country_name = '{selected_country}'
    ORDER BY year
    """
)

fig = px.line(
    df,
    x="YEAR",
    y="GDP",
    title="GDP Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.line(
    df,
    x="YEAR",
    y="POPULATION",
    title="Population Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)