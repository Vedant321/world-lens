WITH base_gdp_metrics AS (

    SELECT
        country_code,
        country_name,
        year,
        GDP,
        POPULATION,

        GDP / NULLIF(POPULATION, 0) AS gdp_per_capita

    FROM {{ ref('fact_country_metrics') }}

    WHERE country_name NOT ILIKE '%income%'
      AND country_name NOT ILIKE '%Asia%'
      AND country_name NOT ILIKE '%Europe%'
      AND country_name NOT ILIKE '%Caribbean%'
      AND country_name NOT ILIKE '%dividend%'

),

growth_calculations AS (

    SELECT
        country_code,
        country_name,
        year,
        GDP,
        POPULATION,
        gdp_per_capita,

        LAG(gdp_per_capita) OVER (
            PARTITION BY country_code
            ORDER BY year
        ) AS prev_year_gdp_per_capita

    FROM base_gdp_metrics

)

SELECT
    country_code,
    country_name,
    year,

    GDP,
    POPULATION,

    gdp_per_capita,

    prev_year_gdp_per_capita,

    (
        (gdp_per_capita - prev_year_gdp_per_capita)
        /
        NULLIF(prev_year_gdp_per_capita, 0)
    ) * 100 AS gdp_per_capita_growth_rate

FROM growth_calculations