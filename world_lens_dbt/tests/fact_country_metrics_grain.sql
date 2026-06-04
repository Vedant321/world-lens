SELECT
    country_code,
    year,
    COUNT(*) AS row_count
FROM {{ ref('fact_country_metrics') }}
GROUP BY
    country_code,
    year
HAVING COUNT(*) > 1