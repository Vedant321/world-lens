SELECT
    country_code,
    country_name,
    year,
    GDP,
    POPULATION,
    GDP / NULLIF(POPULATION, 0) AS GDP_PER_CAPITA
    FROM {{ ref('fact_country_metrics') }}