# World Lens: Global Economic Analytics Platform

A production-style Data Engineering and Analytics Engineering project that ingests economic indicators from the World Bank API, stores raw data in Snowflake, transforms it with dbt, and produces analytics-ready datasets for business intelligence and country-level economic analysis.

The project demonstrates modern data platform concepts including ingestion pipelines, medallion-style modeling, data quality validation, analytics engineering, KPI development, and business-rule enforcement.

---

## Project Overview

World Lens enables exploration of global economic trends by collecting and transforming publicly available World Bank indicators into analytics-ready datasets.

The platform currently tracks:

* GDP
* Population
* Life Expectancy
* Internet Usage
* Unemployment Rate

Using these indicators, the project derives business KPIs such as:

* GDP Per Capita
* Previous Year GDP Per Capita
* GDP Per Capita Growth Rate

---

## Architecture

```text
World Bank API
        │
        ▼
Python Ingestion Pipeline
        │
        ▼
Snowflake RAW Layer
(RAW_API_RESPONSES)
        │
        ▼
dbt Staging Layer
(stg_world_bank_observations)
        │
        ▼
dbt Fact Layer
(fact_country_metrics)
        │
        ▼
dbt Analytics Mart
(mart_country_analytics)
        │
        ▼
Business KPIs & Dashboards
```

---

## Data Flow

### 1. API Ingestion

A Python ingestion pipeline retrieves indicator data from the World Bank API.

Indicators are configured through YAML:

```yaml
indicators:
  - code: NY.GDP.MKTP.CD
    name: GDP

  - code: SP.POP.TOTL
    name: Population

  - code: SP.DYN.LE00.IN
    name: Life Expectancy

  - code: IT.NET.USER.ZS
    name: Internet Users

  - code: SL.UEM.TOTL.ZS
    name: Unemployment
```

New indicators can be added without modifying ingestion logic.

---

### 2. Raw Data Storage

Raw API payloads are stored in Snowflake:

#### RAW_API_RESPONSES

Stores complete World Bank API responses as JSON.

Columns:

```text
indicator_id
payload (VARIANT)
```

This preserves the original source data and supports reproducibility.

---

### 3. Ingestion Tracking

The pipeline maintains an ingestion audit table.

#### INGESTION_RUNS

Tracks:

* Indicator loaded
* Year range loaded
* Load status
* Record counts
* Timestamp

Example:

```text
GDP
1960-2000
SUCCESS
10906 records
```

---

## Idempotent Loading

The ingestion process prevents duplicate loads.

Before loading data, the pipeline checks:

```text
indicator_id
start_year
end_year
```

If the same range has already been successfully loaded, the request is skipped.

Example:

```text
GDP 1960-2000
```

loaded once will not load again.

This mirrors production-grade idempotent ingestion patterns.

---

## dbt Modeling

### Staging Layer

#### stg_world_bank_observations

Purpose:

* Flatten JSON payloads
* Standardize column names
* Cast data types

Grain:

```text
Country + Year + Indicator
```

Example:

```text
USA | 2000 | GDP
USA | 2000 | Population
USA | 2000 | Life Expectancy
```

Columns:

```text
indicator_id
country_code
country_name
year
metric_value
```

---

### Fact Layer

#### fact_country_metrics

Transforms long-format indicator data into a wide analytics-ready table.

Grain:

```text
Country + Year
```

Example:

```text
USA | 2000
```

Columns:

```text
country_code
country_name
year

GDP
POPULATION
LIFE_EXPECTANCY
INTERNET_USERS
UNEMPLOYMENT
```

Business rules are enforced here:

* Aggregate entities removed
* Blank country codes excluded
* Country-level analytics only

---

### Analytics Mart

#### mart_country_analytics

Purpose:

Provide business-ready KPIs for reporting and dashboards.

Columns:

```text
country_code
country_name
year

GDP
POPULATION

gdp_per_capita

prev_year_gdp_per_capita

gdp_per_capita_growth_rate
```

---

## KPI Definitions

### GDP Per Capita

```sql
GDP / NULLIF(POPULATION, 0)
```

Measures economic output per person.

---

### GDP Per Capita Growth Rate

Calculated using SQL window functions.

```sql
LAG(gdp_per_capita)
```

Formula:

```text
(Current GDP Per Capita - Previous GDP Per Capita)
/
Previous GDP Per Capita
* 100
```

Provides year-over-year economic growth.

---

## Data Quality Framework

The project includes automated dbt testing.

### Schema Tests

#### Staging

* country_code not null
* year not null
* indicator_id not null

#### Fact

* country_code not null
* year not null

#### Mart

* country_code not null
* country_name not null
* year not null

---

### Custom Data Quality Tests

#### Fact Grain Validation

Ensures:

```text
country_code + year
```

appears only once.

Detects accidental duplication.

---

#### Blank Country Code Validation

Ensures:

```text
country_code IS NOT NULL
```

and prevents aggregate entities from entering analytics datasets.

---

## Data Quality Investigation

During development, duplicate observations were discovered in World Bank source data.

Example:

```text
AFE
1995
Internet Users
```

appeared multiple times.

Investigation traced the issue to source-level aggregate entities rather than transformation logic.

The project now filters non-country entities from analytical layers while preserving raw source data.

---

## Project Structure

```text
world-lens/
│
├── ingestion/
│   ├── ingest_world_bank.py
│   ├── config.yaml
│   └── utils/
│
├── world_lens_dbt/
│   ├── models/
│   │
│   ├── staging/
│   │   ├── stg_world_bank_observations.sql
│   │   └── schema.yml
│   │
│   ├── facts/
│   │   ├── fact_country_metrics.sql
│   │   └── schema.yml
│   │
│   └── marts/
│       ├── mart_country_analytics.sql
│       └── schema.yml
│
│   └── tests/
│       ├── fact_country_metrics_grain.sql
│       └── no_blank_country_codes.sql
│
├── requirements.txt
└── README.md
```

---

## Tech Stack

| Layer           | Technology     |
| --------------- | -------------- |
| Language        | Python 3.12    |
| Data Warehouse  | Snowflake      |
| Transformation  | dbt Core       |
| Data Modeling   | SQL            |
| Data Quality    | dbt Tests      |
| Source System   | World Bank API |
| Version Control | Git & GitHub   |

---

## Key Concepts Demonstrated

### Data Engineering

* API ingestion
* Idempotent loading
* Audit logging
* Snowflake data warehousing
* JSON processing
* Pipeline design

### Analytics Engineering

* dbt modeling
* Staging → Fact → Mart architecture
* KPI development
* Data quality testing
* Grain validation
* Business rule enforcement

### SQL

* CTEs
* Window Functions
* LAG()
* Conditional Aggregation
* Data Quality Validation

---

## Future Enhancements

### Planned

* Incremental dbt models
* Country dimension table
* Additional World Bank indicators
* Dashboard layer (Streamlit)
* Automated orchestration
* CI/CD pipeline
* Data freshness monitoring

### Potential KPIs

* Population Growth Rate
* GDP Growth Rate
* Internet Adoption Growth
* Unemployment Trends
* Regional Economic Comparisons

---

## Why This Project Matters

World Lens demonstrates how raw external data can be transformed into a reliable analytics platform using modern Data Engineering and Analytics Engineering practices.

Rather than focusing only on ingestion, the project emphasizes data modeling, data quality, business metrics, and trustworthy analytics—the same principles used in production data platforms.
