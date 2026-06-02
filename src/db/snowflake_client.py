import snowflake.connector

from src.config.settings import Settings


class SnowflakeClient:

    def get_connection(self):
        return snowflake.connector.connect(
            account=Settings.SNOWFLAKE_ACCOUNT,
            user=Settings.SNOWFLAKE_USER,
            password=Settings.SNOWFLAKE_PASSWORD,
            role=Settings.SNOWFLAKE_ROLE,
            warehouse=Settings.SNOWFLAKE_WAREHOUSE,
            database=Settings.SNOWFLAKE_DATABASE,
            schema=Settings.SNOWFLAKE_SCHEMA,
        )