SELECT
    country_code,
    year,
    indicator_id,
    COUNT(*) AS row_count
FROM {{ ref('fact_indicator_values') }}
GROUP BY
    country_code,
    year,
    indicator_id
HAVING COUNT(*) > 1