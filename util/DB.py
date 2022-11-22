import pymysql

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="localhost",
            db="chatapp",
            user="testuser",
            charset="utf8",
            cursorclass=pymysql.cursors.DiscCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()