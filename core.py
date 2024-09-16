# localdb/core.py
import sqlite3


class CoreDatabase:
    def __init__(self, db_name="local_database.db"):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            print(f"Connected to database: {self.db_name}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def run_query(self, schema=None):
        """Execute a SQL query passed as a schema string."""
        if self.conn is None:
            print("No active database connection. Cannot run query.")
            return
        try:
            if schema:
                cursor = self.conn.cursor()
                cursor.execute(schema)
                self.conn.commit()
                print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def close_connection(self):
        """Close the SQLite database connection."""
        if self.conn:
            self.conn.close()
            print("Connection closed.")

    def insert_record(self, table_name, **kwargs):
        """
        Insert a new record into the specified table.

        Parameters:
        - table_name: Name of the table where the record should be inserted.
        - kwargs: A dictionary of column names and values to insert.

        Example:
        insert_record('users', name='Alice', age=25, email='alice@example.com')
        """
        if self.conn is None:
            print("No active database connection. Cannot insert record.")
            return

        try:
            # Dynamically generate the column names and values from kwargs
            columns = ', '.join(kwargs.keys())
            placeholders = ', '.join(['?' for _ in kwargs])
            values = tuple(kwargs.values())

            # Construct and execute the SQL insert statement
            cursor = self.conn.cursor()
            sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(sql_query, values)
            self.conn.commit()
            print(f"Record inserted into '{table_name}' successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting record: {e}")

    def query_table(self, table_name, columns="*", where_clause=None):
        """
        Query a table in the SQLite database.

        Parameters:
            table_name (str): The name of the table to query.
            columns (str or list): The columns to select. Default is '*', which selects all columns.
            where_clause (str, optional): Optional WHERE clause to filter results. Default is None.

        Returns:
            list: A list of tuples containing the rows returned by the query.
        """
        if self.conn is None:
            print("No active database connection. Cannot query the table.")
            return []

        # Convert columns list to a string if it's provided as a list
        if isinstance(columns, list):
            columns = ', '.join(columns)

        query = f"SELECT {columns} FROM {table_name}"
        if where_clause:
            query += f" WHERE {where_clause}"

        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Error querying {table_name}: {e}")
            return []

