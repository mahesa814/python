import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="root",
  database="python_learn"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customer2 (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255) )")

# mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("SHOW TABLES")

# for x in mycursor :

insert = "insert into user (name,address) value (%s,%s)"

val = [
  ("john","Ciasayong 21"),
  ("wisnu","Ciasayong 22"),
  ("su","Ciasayong 23"),
  ("ilham","Ciasayong 24"),
  ("mah","Ciasayong 25")
  ]
# mycursor.executemany(insert,val)

# show_all = "select * from user"


# myresult = mycursor.fetchall()


# sql = "DELETE FROM user WHERE name = 'wisnu'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")
sql = "delete from user where name = 'su'"



mycursor.execute(sql)
mydb.commit()
myresult = mycursor.fetchall()

print(mycursor.rowcount,"record(s) deleted")
# my_select_one = mycursor.fetchone()
# print(my_select_one)

# for x in myresult:
#   print(x)

# for x in myresult:
#   print (x)
# print(mycursor.rowcount,"record")

#   print (x)