# localdb/setup_db.py
import sqlite3


class SetupDatabase:
    def __init__(self, db_name="local_database.db"):
        self.db_name = db_name
        self.conn = None

    def create_connection(self):
        """Create a connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"Connected to database: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_table(self, table_name, columns):
        """Create a table in the SQLite database with dynamic table name and columns."""
        if self.conn is None:
            print("No active database connection. Cannot create table.")
            return

        columns_definition = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})"

        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            self.conn.commit()
            print(f"Table '{table_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def close_connection(self):
        """Close the SQLite database connection."""
        if self.conn:
            self.conn.close()
            print("Connection closed.")
