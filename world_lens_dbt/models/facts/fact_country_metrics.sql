SELECT
    country_code,
    country_name,
    year,

    MAX(
        CASE
            WHEN indicator_id = 'NY.GDP.MKTP.CD'
            THEN metric_value
        END
    ) AS GDP,

    MAX(
        CASE
            WHEN indicator_id = 'SP.POP.TOTL'
            THEN metric_value
        END
    ) AS POPULATION,

    MAX(
        CASE
            WHEN indicator_id = 'SP.DYN.LE00.IN'
            THEN metric_value
        END
    ) AS LIFE_EXPECTANCY,

    MAX(
        CASE
            WHEN indicator_id = 'IT.NET.USER.ZS'
            THEN metric_value
        END
    ) AS INTERNET_USERS,

    MAX(
        CASE
            WHEN indicator_id = 'SL.UEM.TOTL.ZS'
            THEN metric_value
        END
    ) AS UNEMPLOYMENT

FROM {{ ref('stg_world_bank_observations') }}

GROUP BY
    country_code,
    country_name,
    year