from pathlib import Path
import sqlite3

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_IN = (PROJECT_ROOT / "data" / "cohort.db")
SQL_PATH = (PROJECT_ROOT / "queries.sql")

# Make sure that the files can be found/exist
if not DATA_IN.exists():
    raise FileNotFoundError(f"Database not found: {DATA_IN}")
if not SQL_PATH.exists():
    raise FileNotFoundError(f"Database not found: {SQL_PATH}")

sql_query = SQL_PATH.read_text(encoding="utf-8")

# Use sqlite to run the query
with sqlite3.connect(DATA_IN) as connection:
    cursor = connection.cursor()
    cursor.execute(sql_query)
    column_names = [column[0] for column in cursor.description]
    results = cursor.fetchall()

# Print results
print("Columns:", column_names)
print("Number of rows:", len(results))
print()
for row in results[:15]:
    print(row)
if len(results) > 15:
    print("...showing first 15 rows only")
print()
print("Expected rows: 2830")
print("Actual rows:", len(results))
