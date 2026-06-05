import os

import pandas as pd
import snowflake.connector
import streamlit as st

from dotenv import load_dotenv

load_dotenv()


@st.cache_resource
def get_connection():

    return snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE"),
    )


@st.cache_data(ttl=600)
def run_query(query):

    conn = get_connection()

    return pd.read_sql(query, conn)