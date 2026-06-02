from db.snowflake_connection import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("SELECT CURRENT_VERSION()")

print(cursor.fetchone())

cursor.close()
conn.close()

print("Snowflake connection successful!")