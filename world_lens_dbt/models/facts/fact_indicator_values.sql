{{ config(materialized='table') }}
    
WITH country_only AS (

    SELECT *
    FROM {{ ref('stg_world_bank_observations') }}

    WHERE country_code IS NOT NULL
      AND TRIM(country_code) <> ''

)

SELECT
    country_code,
    country_name,
    year,
    indicator_id,
    metric_value

FROM country_only