import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password"
)
mycursor = mydb.cursor()

mycursor.execute("insert into test2.student_info values ('Mohan',101,91.2,'Section A'),('Rohan',102,89.8,'Section B'),('Abdul',103,78.9,'Section C')")
mydb.commit()
mydb.close()