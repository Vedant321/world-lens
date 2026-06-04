SELECT
    indicator_id,
    f.value:countryiso3code::STRING AS country_code,
    f.value:country.value::STRING AS country_name,
    f.value:date::INTEGER AS year,
    f.value:value::FLOAT AS metric_value

FROM {{ source('raw', 'RAW_API_RESPONSES') }},
LATERAL FLATTEN(input => payload[1]) f