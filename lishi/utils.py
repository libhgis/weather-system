import pymysql

# 连接数据库函数
def connect_to_database():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='tianqi',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
