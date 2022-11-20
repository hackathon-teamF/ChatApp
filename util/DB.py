import pymysql

class DB:
    def getConnection():
        try:
            conn = pymysql.connect(
            host="localhost",
            db="cahtapp",
            user="testuser",
            password="testuser",
            charset="utf-8",
            cursorclass=pymysql.cursors.DiscCursor
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
