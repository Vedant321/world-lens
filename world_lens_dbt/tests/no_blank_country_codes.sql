SELECT *
FROM {{ ref('fact_country_metrics') }}
WHERE country_code IS NULL
   OR TRIM(country_code) = ''