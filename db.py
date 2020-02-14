import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, table_to_create: str):
        self.DB: str = "db.sqlite"
        # creates db file if none exists
        self.connection: sqlite3.Connection = self.__create_connection(self.DB)
        # DB TABLE
        self.create_table = table_to_create

        
    def __create_connection(self, path: str) -> sqlite3.Connection:
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error {e} occurred")
        return connection

    def execute_query(self, connection: sqlite3.Connection, query: str) -> None:
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query executed successfully")
        except Error as e:
            print("The error '" + str(e) + "' occurred")

    def execute_read_query(self, connection: sqlite3.Connection, query: str):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print("The error '" + str(e) + "' occurred")




## EXAMPLES 
"""
create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        age INTEGER,
                                        gender TEXT,
                                        nationality TEXT
                                    );"""

# creates table in DB
execute_query(connection, create_users_table)

create_users = """ INSERT INTO users (name, age, gender, nationality)
                   VALUES ('James', 25, 'male', 'USA'),
                   ('Leila', 32, 'female', 'France'),
                   ('Brigitte', 35, 'female', 'England'),
                   ('Mike', 40, 'male', 'Denmark'),
                   ('Elizabeth', 21, 'female', 'Canada');"""

# inserts into DB
execute_query(connection, create_users) 

# get all users
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)

# update a record in table
update_post_description = """UPDATE posts
                             set description = "The weather has become pleasant now"
                             WHERE id = 2"""
execute_query(connection, update_post_description)

# delete from table
delete_comment = """DELETE FROM comments
                             WHERE id = 5"""
execute_query(connection, delete_comment)
"""