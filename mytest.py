import sqlite3

from localdb import CoreDatabase, SetupDatabase

myDatabase = "User_db"
tableName = "User_table"
myColumn = {
    'id': 'INTEGER PRIMARY KEY AUTOINCREMENT',
    'name': 'TEXT NOT NULL',
    'age': 'INTEGER',
    'email': 'TEXT'
}

newData = {
    'name': 'Beauty',
    'age': '22',
    'email': 'beauty1205@conection.com'}

try:
    db = SetupDatabase(myDatabase)
    db.create_connection()
    db.create_table(tableName, myColumn)
    core_db = CoreDatabase(myDatabase)
    core_db.connect()
    core_db.insert_record(tableName, **newData)
    core_db.run_query(F"SELECT * FROM {tableName}")
    res = core_db.query_table(tableName,"email")
    print(res)
    # core_db.run_query(f"DELETE FROM {tableName} WHERE name = 'Nishu Bharti'")
except sqlite3.Error as sql_err:
    print(f"DB related error..{sql_err}")
except KeyError as key_err:
    print(f"Some Key value error {key_err}")
except Exception as e:
    print(f"something went wrong..{e}")

finally:
    db.close_connection()
    core_db.close_connection()
