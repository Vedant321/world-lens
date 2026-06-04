from src.config.indicator_loader import load_indicators
from src.ingestion.world_bank_ingestor import WorldBankIngestor
from src.db.snowflake_client import SnowflakeClient


START_YEAR = 1960
END_YEAR = 2000

indicators = load_indicators()

ingestor = WorldBankIngestor()
snowflake_client = SnowflakeClient()

for indicator in indicators:

    indicator_code = indicator["code"]

    if snowflake_client.already_loaded(
        indicator_code,
        START_YEAR,
        END_YEAR
    ):
        print(
            f"Skipping {indicator['name']} "
            f"(already loaded)"
        )
        continue

    payload = ingestor.fetch_indicator(
        indicator_code,
        START_YEAR,
        END_YEAR
    )

    snowflake_client.insert_raw_payload(
        indicator_code,
        payload
    )

    rows_loaded = len(payload[1])

    snowflake_client.record_success(
        indicator_code,
        START_YEAR,
        END_YEAR,
        rows_loaded
    )

    print(f"Loaded {indicator['name']}")