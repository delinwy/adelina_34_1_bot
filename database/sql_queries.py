CREATE_USER_TABLE_QUERY = '''
        CREATE TABLE IF NOT EXISTS telegram_users
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        FIRST_NAME CHAR(50),
        LAST_NAME CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )
'''

CREATE_USER_RESPONSES_TABLE_QUERY = '''
        CREATE TABLE IF NOT EXISTS user_responses
        (
        USER_ID INTEGER PRIMARY KEY,
        QUESTION TEXT,
        ANSWER TEXT
        )
'''

INSERT_USER_QUERY = '''
INSERT INTO telegram_users VALUES(?,?,?,?,?)
'''

INSERT_USER_RESPONSE = '''
INSERT INTO user_responses VALUES(?,?,?)
'''
