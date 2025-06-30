import mysql.connector
import pandas as pd

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'spherych_devapp'
}

conn = mysql.connector.connect(**config)

# List of key tables to examine
key_tables = ['Workouts', 'Sessions', 'Users', 'SpeedCages', 'Rhythmgames']

for table in key_tables:
    print(f"\n{'='*60}")
    print(f"TABLE: {table}")
    print(f"{'='*60}")
    
    # Get columns
    columns_query = f"SHOW COLUMNS FROM {table}"
    columns_df = pd.read_sql(columns_query, conn)
    print("COLUMNS:")
    print(columns_df)
    
    # Get row count
    count_query = f"SELECT COUNT(*) as row_count FROM {table}"
    count_df = pd.read_sql(count_query, conn)
    print(f"\nROW COUNT: {count_df.iloc[0]['row_count']}")
    
    # Get sample data
    sample_query = f"SELECT * FROM {table} LIMIT 3"
    sample_df = pd.read_sql(sample_query, conn)
    print(f"\nSAMPLE DATA:")
    print(sample_df)

conn.close()