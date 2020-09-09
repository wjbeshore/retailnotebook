import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="XO52eg?!wb",
  database="retail",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()