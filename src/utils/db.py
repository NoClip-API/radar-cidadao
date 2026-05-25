import os
import dotenv
import pymysql

dotenv.load_dotenv()

db_host = os.getenv('MYSQL_HOST',  'localhost')
db_user = os.getenv('MYSQL_USER', 'root')
db_password = os.getenv('MYSQL_PASSWORD', '')
db_name = os.getenv('MYSQL_DATABASE', 'deputados_db')
db_port = int(os.getenv('MYSQL_PORT', 3306))

def connect_db(cursor=pymysql.cursors.DictCursor):
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        port=db_port,
        cursorclass=cursor
        )
    return connection

def fetch_data(query, params=None):
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
    finally:
        connection.close()
