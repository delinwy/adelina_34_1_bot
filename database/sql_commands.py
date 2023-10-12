import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print('Database connected successfully')

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.commit()

    def sql_create_user_responses_table(self):
        if self.connection:
            print('Database connected successfully')

        self.cursor.execute(sql_queries.CREATE_USER_RESPONSES_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_user_query(self, telegram_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, telegram_id, username, first_name, last_name,)
        )
        self.connection.commit()

    def sql_insert_user_response(self, user_id, question, answer):
        self.cursor.execute(
            sql_queries.INSERT_USER_RESPONSE,
            (user_id, question, answer)
        )
        self.connection.commit()
