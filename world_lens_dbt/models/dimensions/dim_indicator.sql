{{ config(materialized='table') }}

SELECT
    'NY.GDP.MKTP.CD' AS indicator_id,
    'GDP' AS indicator_name,
    'Economy' AS category

UNION ALL

SELECT
    'SP.POP.TOTL',
    'Population',
    'Demographics'

UNION ALL

SELECT
    'SP.DYN.LE00.IN',
    'Life Expectancy',
    'Health'

UNION ALL

SELECT
    'IT.NET.USER.ZS',
    'Internet Users',
    'Technology'

UNION ALL

SELECT
    'SL.UEM.TOTL.ZS',
    'Unemployment',
    'Labor Market'