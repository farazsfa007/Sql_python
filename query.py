import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT Stu_name, Stu_Marks FROM test2.student_info")
for q in mycursor.fetchall():
    print(q)
mydb.close()
