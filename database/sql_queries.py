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

CREATE_BAN_USER_TABLE_QUERY = '''
        CREATE TABLE IF NOT EXISTS ban_users
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        COUNT INTEGER,
        UNIQUE (TELEGRAM_ID)
        )
'''

CREATE_USER_FORM_TABLE_QUERY = '''
        CREATE TABLE IF NOT EXISTS user_form
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        NICKNAME CHAR(50),
        BIO TEXT,
        AGE INTEGER,
        OCCUPATION CHAR(50),
        PHOTO TEXT,
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

INSERT_USER_FORM_QUERY = '''
INSERT INTO user_form VALUES(?,?,?,?,?,?,?)
'''

INSERT_BAN_USER_QUERY = '''
INSERT INTO ban_users VALUES(?,?,?,?)
'''

INSERT_USER_RESPONSE = '''
INSERT INTO user_responses VALUES(?,?,?)
'''

SELECT_USER_QUERY = '''
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
'''

SELECT_ALL_USERS_QUERY = '''
SELECT * FROM telegram_users
'''

SELECT_USER_FORM_QUERY = '''
SELECT * FROM user_form WHERE TELEGRAM_ID = ?
'''

UPDATE_BAN_USER_COUNT_QUERY = '''
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ? 
'''
