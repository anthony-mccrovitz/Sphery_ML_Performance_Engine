import mysql.connector
import pandas as pd

# --- Database Connection Configuration ---
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'spherych_devapp'
}

# This list will store our findings to print a summary at the end
summary_data = []

print("="*70)
print("Starting Data Location Analysis...")
print("This script will find the source table(s) and record counts for each game.")
print("="*70)

try:
    # --- Connect to the Database ---
    conn = mysql.connector.connect(**config)
    print("Database connection successful.\n")

    # --- 1. SpeedCage ---
    game_name = "SpeedCage"
    table_source = "SpeedCages"
    print(f"\n--- Analyzing: {game_name} ---")
    print(f"Source Table(s): {table_source}")
    count_query = f"SELECT COUNT(*) as count FROM {table_source}"
    data_query = f"SELECT * FROM {table_source} LIMIT 3"
    count = pd.read_sql(count_query, conn).iloc[0]['count']
    sample_df = pd.read_sql(data_query, conn)
    print(f"Records Found: {count}")
    print("Sample Data:")
    print(sample_df)
    summary_data.append([game_name, table_source, count])

    # --- 2. Racer ---
    game_name = "Racer"
    table_source = "Workouts JOIN RaceConfigs"
    print(f"\n--- Analyzing: {game_name} ---")
    print(f"Source Table(s): {table_source}")
    join_query = "FROM Workouts w JOIN RaceConfigs rc ON w.id = rc.workoutId"
    count_query = f"SELECT COUNT(*) as count {join_query}"
    data_query = f"SELECT w.id, w.score, w.userId, rc.difficulty, rc.duration {join_query} LIMIT 3"
    count = pd.read_sql(count_query, conn).iloc[0]['count']
    sample_df = pd.read_sql(data_query, conn)
    print(f"Records Found: {count}")
    print("Sample Data:")
    print(sample_df)
    summary_data.append([game_name, table_source, count])

    # --- 3. Fighter ---
    game_name = "Fighter"
    table_source = "Fighters"
    print(f"\n--- Analyzing: {game_name} ---")
    print(f"Source Table(s): {table_source}")
    count_query = f"SELECT COUNT(*) as count FROM {table_source}"
    data_query = f"SELECT * FROM {table_source} LIMIT 3"
    count = pd.read_sql(count_query, conn).iloc[0]['count']
    sample_df = pd.read_sql(data_query, conn)
    print(f"Records Found: {count}")
    print("Sample Data:")
    print(sample_df)
    summary_data.append([game_name, table_source, count])

    # --- 4. Games from WorkoutPresets ---
    preset_games = ['DualFlow', 'HomeFlow', 'LeagueQualification', 'LegDay', 'RehaFlow', 'UpperBody']
    for game_name in preset_games:
        table_source = "Workouts JOIN WorkoutPresets"
        print(f"\n--- Analyzing: {game_name} ---")
        print(f"Source Table(s): {table_source}")
        join_query = f"""
            FROM Workouts w
            JOIN WorkoutPresets wp ON w.workoutPresetId = wp.id
            WHERE wp.name = '{game_name}'
        """
        count_query = f"SELECT COUNT(*) as count {join_query}"
        data_query = f"SELECT w.id, w.score, w.userId, w.completedWorkout, wp.name as presetName {join_query} LIMIT 3"
        count = pd.read_sql(count_query, conn).iloc[0]['count']
        sample_df = pd.read_sql(data_query, conn)
        print(f"Records Found: {count}")
        print("Sample Data:")
        print(sample_df)
        summary_data.append([game_name, table_source, count])

except mysql.connector.Error as err:
    print(f"An error occurred: {err}")
finally:
    # --- Close the Connection ---
    if 'conn' in locals() and conn.is_connected():
        conn.close()

# --- Final Summary ---
print("\n\n" + "="*70)
print("              Data Location Summary")
print("="*70)
summary_df = pd.DataFrame(summary_data, columns=["Game Name", "Primary Source Table(s)", "Number of Records"])
print(summary_df.to_string(index=False))
print("="*70)
