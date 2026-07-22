import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@reet@22",
    database="collage"
)
cursor = conn.cursor()
print("connected")
