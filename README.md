# 🌍 World Lens — Global Analytics Platform

An end-to-end data engineering project that ingests World Bank economic and demographic data into Snowflake, transforms it into an analytics-ready star schema using dbt, and serves interactive insights through a Streamlit dashboard.

## Overview

World Lens demonstrates a modern analytics engineering workflow:

* Automated data ingestion from the World Bank API
* Cloud data warehouse powered by Snowflake
* Data modeling with dbt
* Star schema design with fact and dimension tables
* Data quality testing and lineage tracking
* Interactive analytics dashboard built with Streamlit

The project follows industry-standard ELT architecture and mirrors the workflow used in modern data platforms.

---

## Architecture

```text
World Bank API
      │
      ▼
Python Ingestion Pipeline
      │
      ▼
Snowflake Raw Layer
      │
      ▼
dbt Staging Models
      │
      ▼
Fact & Dimension Models
      │
      ▼
Analytics Mart
      │
      ▼
Streamlit Dashboard
```

---

## Data Model

### Fact Tables

* FACT_INDICATOR_VALUES

  * Long-format World Bank observations
  * Grain: Country × Year × Indicator

* FACT_COUNTRY_METRICS

  * Analytics-ready country metrics
  * Grain: Country × Year

### Dimension Tables

* DIM_COUNTRY
* DIM_INDICATOR

### Analytics Mart

* MART_COUNTRY_ANALYTICS

Includes:

* GDP
* Population
* GDP Per Capita
* Previous Year GDP Per Capita
* GDP Per Capita Growth Rate

---

## Features

### Data Ingestion

* Python-based ingestion pipeline
* Automated API extraction
* Incremental load tracking
* Ingestion audit logging

### Analytics Engineering

* dbt-powered transformations
* Star schema modeling
* Reusable SQL models
* Data lineage visualization

### Data Quality

* Primary key grain validation
* Referential integrity testing
* Null checks
* Uniqueness constraints

### Analytics Dashboard

* Executive Overview
* Country Explorer
* Country Comparison
* Growth Analytics (planned)
* Indicator Deep Dive (planned)

---

## Tech Stack

| Layer           | Technology     |
| --------------- | -------------- |
| Language        | Python         |
| Data Source     | World Bank API |
| Warehouse       | Snowflake      |
| Transformations | dbt            |
| Analytics       | SQL            |
| Dashboard       | Streamlit      |
| Visualization   | Plotly         |
| Version Control | Git/GitHub     |

---

## Project Structure

```text
world-lens/
│
├── src/
│   ├── ingestion/
│   ├── db/
│   ├── config/
│   └── main.py
│
├── world_lens_dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── dimensions/
│   │   ├── facts/
│   │   └── marts/
│   └── tests/
│
├── streamlit_app/
│   ├── pages/
│   └── utils/
│
├── requirements.txt
└── README.md
```

---

## Setup

### Clone Repository

```bash
git clone <repository-url>
cd world-lens
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Create a `.env` file:

```env
SNOWFLAKE_ACCOUNT=
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_ROLE=
SNOWFLAKE_WAREHOUSE=
SNOWFLAKE_DATABASE=WORLD_LENS
SNOWFLAKE_SCHEMA=RAW
```

---

## Usage

### 1. Ingest Data

```bash
python -m src.main
```

### 2. Build Analytics Models

```bash
cd world_lens_dbt

dbt run
dbt test

cd ..
```

### 3. Launch Dashboard

```bash
streamlit run streamlit_app/app.py
```

---

## Data Quality Coverage

Current dbt tests include:

* Fact table grain validation
* Referential integrity checks
* Dimension uniqueness tests
* Null validation tests
* Business rule validation

All dbt tests currently pass successfully.

---

## Future Enhancements

* Incremental dbt models
* Historical trend forecasting
* Automated orchestration with Airflow
* CI/CD pipeline
* Containerized deployment
* Real-time data refresh

---

## Author

Vedant Shinde

Built as a portfolio project to demonstrate modern Data Engineering, Analytics Engineering, and Data Platform development practices.
