{{ config(materialized='table') }}

SELECT DISTINCT
    country_code,
    country_name
FROM {{ ref('stg_world_bank_observations') }}
WHERE country_code <> ''