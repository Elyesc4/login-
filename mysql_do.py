import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='Funnie2711',
    host='localhost',
    database="mydatabase"
)

my_cursor = cnx.cursor()

my_cursor.execute("CREATE TABLE users (1name VARCHAR(255), 2name VARCHAR(255), age VARCHAR(255), password VARCHAR(255))")

my_cursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")