from argparse import ArgumentParser

from src.config.indicator_loader import load_indicators
from src.ingestion.world_bank_ingestor import WorldBankIngestor
from src.db.snowflake_client import SnowflakeClient


parser = ArgumentParser()

parser.add_argument(
    "--start-year",
    type=int,
    required=True
)

parser.add_argument(
    "--end-year",
    type=int,
    required=True
)

args = parser.parse_args()

START_YEAR = args.start_year
END_YEAR = args.end_year

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

    rows_loaded = len(payload[1])

    snowflake_client.save_ingestion_run(
        indicator_code,
        START_YEAR,
        END_YEAR,
        payload,
        rows_loaded
    )

    print(
        f"Loaded {indicator['name']} "
        f"({START_YEAR}-{END_YEAR})"
    )