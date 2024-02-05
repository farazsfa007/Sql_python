import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
)

mycursor = mydb.cursor()

# Drop the table
mycursor.execute("CREATE TABLE IF NOT EXISTS test.Student_info (Stu_name VARCHAR(90), Stu_id INT, Stu_Marks FLOAT, Stu_Sect VARCHAR(90))")

mydb.close()
