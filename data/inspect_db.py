from pathlib import Path
import sqlite3

#Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_IN = (PROJECT_ROOT / "data" / "cohort.db")

if not DATA_IN.exists():
    raise FileNotFoundError(f"Database not found: {DATA_IN}")

with sqlite3.connect(DATA_IN) as connection:
    cursor = connection.cursor()

    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
""")
    tables = [row[0] for row in cursor.fetchall()]
    print("TABLES:", tables)

    for table in tables:
        print(f"\n{'=' * 50}")
        print(f"TABLE: {table}")

        # table names are from the database itself, so its quotes them so sqlite will treat it as an identifier
        quoted_table = '"' + table.replace('"', '""') +'"'

        # inspects the columns and their types
        cursor.execute(f"PRAGMA table_info({quoted_table});")
        columns = cursor.fetchall()
        print("\nCOLUMNS:")
        for column in columns:
            cid, name, data_type, not_null, default, primary_key = column
            print(
                f"  {name}: type={data_type}, "
                f"not_null={bool(not_null)}, "
                f"primary_key={bool(primary_key)}"
            )

        # inspects the foreign-key relationships
        cursor.execute(f"PRAGMA foreign_key_list({quoted_table});")
        foreign_keys = cursor.fetchall()
        print("\nFOREIGN KEYS:")
        if foreign_keys:
            for fk in foreign_keys:
                print(f"  {fk}")
        else:
            print("None declared")

        # counts the rows
        cursor.execute(f"SELECT COUNT(*) FROM {quoted_table};")
        print("\nROW COUNT:", cursor.fetchone()[0])

        # preview of some records
        cursor.execute(f"SELECT * FROM {quoted_table} LIMIT 3;")
        print("\nSAMPLE RECORDS:")
        for record in cursor.fetchall():
            print(" ", record)
