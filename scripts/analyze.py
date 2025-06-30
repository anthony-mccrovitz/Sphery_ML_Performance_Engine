import mysql.connector
import pandas as pd

# Database connection parameters
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'spherych_devapp'
}

# Connect to the database
conn = mysql.connector.connect(**config)

# Get all table names
tables_query = "SHOW TABLES"
tables_df = pd.read_sql(tables_query, conn)

print("="*60)
print("ALL TABLES IN SPHERYCH_DEVAPP DATABASE")
print("="*60)
print(tables_df)
print("\n" + "="*60)

# Close the connection
conn.close()