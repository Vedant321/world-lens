import json
import snowflake.connector

from uuid import uuid4
from datetime import datetime

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

    def already_loaded(
        self,
        indicator_id,
        requested_start_year,
        requested_end_year
    ):

        conn = self.get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT 1
                FROM INGESTION_RUNS
                WHERE indicator_id = %s
                  AND status = 'SUCCESS'
                  AND start_year <= %s
                  AND end_year >= %s
                LIMIT 1
                """,
                (
                    indicator_id,
                    requested_start_year,
                    requested_end_year
                )
            )

            return cursor.fetchone() is not None

        finally:
            cursor.close()
            conn.close()

    def save_ingestion_run(
        self,
        indicator_id,
        start_year,
        end_year,
        payload,
        rows_loaded
    ):

        conn = self.get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO RAW_API_RESPONSES
                (
                    indicator_id,
                    payload
                )
                SELECT
                    %s,
                    PARSE_JSON(%s)
                """,
                (
                    indicator_id,
                    json.dumps(payload)
                )
            )

            cursor.execute(
                """
                INSERT INTO INGESTION_RUNS
                (
                    run_id,
                    indicator_id,
                    start_year,
                    end_year,
                    status,
                    rows_loaded,
                    loaded_at
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    str(uuid4()),
                    indicator_id,
                    start_year,
                    end_year,
                    "SUCCESS",
                    rows_loaded,
                    datetime.utcnow()
                )
            )

            conn.commit()

        except Exception:

            conn.rollback()
            raise

        finally:

            cursor.close()
            conn.close()