import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password"
)
mycursor = mydb.cursor()

mycursor.execute("Create Database if not exists test")
mydb.close()