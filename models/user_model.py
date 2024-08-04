import mysql.connector
from config import Config

class UserModel:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        self.cursor = self.conn.cursor()

    def create_user(self, user_name, pwd, role="user", status="Y"):
        query = """
        INSERT INTO user_table (user_name, pwd, role, status) 
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (user_name, pwd, role, status))
        self.conn.commit()

    def get_user_by_username(self, user_name):
        query = "SELECT * FROM user_table WHERE user_name = %s"
        self.cursor.execute(query, (user_name,))
        return self.cursor.fetchone()
