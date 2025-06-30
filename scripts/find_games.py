import mysql.connector
import pandas as pd

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'spherych_devapp'
}

conn = mysql.connector.connect(**config)

# Get all table names again to see if we missed anything
tables_query = "SHOW TABLES"
tables_df = pd.read_sql(tables_query, conn)
print("ALL TABLES IN DATABASE:")
print(tables_df)

# Look for tables that might contain game data
game_related_tables = []
for table in tables_df.iloc[:, 0]:  # Get table names from first column
    if any(keyword in table.lower() for keyword in ['game', 'race', 'exergy', 'rhythm', 'fighter', 'config', 'cage', 'speed']):
        game_related_tables.append(table)

print(f"\nGAME-RELATED TABLES FOUND:")
for table in game_related_tables:
    print(f"- {table}")

# Check a few more tables that might have game data
additional_tables = ['Fighters', 'RhythmgameConfigs', 'RaceConfigs', 'FighterConfigs']
for table in additional_tables:
    if table in tables_df.iloc[:, 0].values:
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
        
        # Get sample data if there are rows
        if count_df.iloc[0]['row_count'] > 0:
            sample_query = f"SELECT * FROM {table} LIMIT 3"
            sample_df = pd.read_sql(sample_query, conn)
            print(f"\nSAMPLE DATA:")
            print(sample_df)
        else:
            print("\nNO DATA IN THIS TABLE")

# Also check if there are any tables with 'workout' in the name that might have game type info
print(f"\n{'='*60}")
print("CHECKING WORKOUTS TABLE FOR GAME TYPE INFORMATION...")
print(f"{'='*60}")

# Let's see if WorkoutPresets might tell us about game types
workout_preset_query = "SELECT * FROM WorkoutPresets LIMIT 10"
try:
    preset_df = pd.read_sql(workout_preset_query, conn)
    print("WORKOUT PRESETS SAMPLE:")
    print(preset_df)
except:
    print("Could not query WorkoutPresets table")

conn.close() 