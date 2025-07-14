import mysql.connector
import pandas as pd

# --- Database Connection Configuration ---
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'database': 'spherych_devapp'
}

def analyze_difficulty_exercise_correlation():
    """
    Analyzes the correlation between race difficulty and the types of exercises performed.
    """
    try:
        conn = mysql.connector.connect(**config)
        print("Database connection successful.\n")

        query = """
        SELECT
            rc.difficulty,
            AVG(w.totalPunches) as avg_punches,
            AVG(w.totalJumps) as avg_jumps,
            AVG(w.totalSquats) as avg_squats,
            AVG(w.totalTripples) as avg_tripples,
            AVG(w.totalLunges) as avg_lunges,
            AVG(w.totalBurpees) as avg_burpees,
            COUNT(w.id) as workout_count
        FROM Workouts w
        JOIN RaceConfigs rc ON w.id = rc.workoutId
        GROUP BY rc.difficulty
        ORDER BY rc.difficulty;
        """

        print("Executing query to analyze exercise distribution by difficulty...")
        df = pd.read_sql(query, conn)

        print("\n--- Analysis Results ---")
        print("Average exercise counts per difficulty rating:")
        print(df.to_string(index=False))

        print("\n--- Summary Table ---")
        summary_data = []
        for index, row in df.iterrows():
            difficulty = row['difficulty']
            exercises = []
            notes = f"{row['workout_count']} workouts analyzed."

            if row['avg_punches'] > 0: exercises.append(f"Punches (avg: {row['avg_punches']:.2f})")
            if row['avg_jumps'] > 0: exercises.append(f"Jumps (avg: {row['avg_jumps']:.2f})")
            if row['avg_squats'] > 0: exercises.append(f"Squats (avg: {row['avg_squats']:.2f})")
            if row['avg_tripples'] > 0: exercises.append(f"Tripples (avg: {row['avg_tripples']:.2f})")
            if row['avg_lunges'] > 0: exercises.append(f"Lunges (avg: {row['avg_lunges']:.2f})")
            if row['avg_burpees'] > 0: exercises.append(f"Burpees (avg: {row['avg_burpees']:.2f})")

            summary_data.append([difficulty, ", ".join(exercises) if exercises else "No consistent exercises", notes])

        summary_df = pd.DataFrame(summary_data, columns=["Difficulty Rating", "Associated Exercises/Subsets", "Notes"])
        print(summary_df.to_string(index=False))


    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    analyze_difficulty_exercise_correlation() 