import mysql.connector
import pandas as pd

# --- Database Connection Configuration ---
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'spherych_devapp'
}

try:
    # --- Connect to the Database ---
    conn = mysql.connector.connect(**config)

    # --- SQL Query to Get All Preset Names ---
    # We select the 'name' column from the WorkoutPresets table.
    query = "SELECT id, name FROM WorkoutPresets ORDER BY name ASC"

    # --- Execute the Query and Load into a DataFrame ---
    game_types_df = pd.read_sql(query, conn)

    # --- Print the Results ---
    print("="*50)
    print("Available Game Types from WorkoutPresets")
    print("="*50)
    print(game_types_df.to_string(index=False))
    print("="*50)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # --- Close the Connection ---
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Database connection closed.")
