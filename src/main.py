from src.db.snowflake_client import SnowflakeClient

from src.config.settings import Settings

# print(Settings.SNOWFLAKE_ACCOUNT)
# print(Settings.SNOWFLAKE_USER)

# client = SnowflakeClient()

# conn = client.get_connection()

# cursor = conn.cursor()

# cursor.execute("SELECT CURRENT_VERSION()")

# print(cursor.fetchone())

# cursor.close()
# conn.close()

# from src.config.indicator_loader import load_indicators

# indicators = load_indicators()

# print(indicators)

from src.config.indicator_loader import load_indicators
from src.ingestion.world_bank_ingestor import WorldBankIngestor

indicators = load_indicators()

ingestor = WorldBankIngestor()

first_indicator = indicators[0]

data = ingestor.fetch_indicator(first_indicator["code"])

print(first_indicator)
print(type(data))
print(len(data))
print(data[1][0])