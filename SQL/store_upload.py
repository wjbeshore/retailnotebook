import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="XO52eg?!wb",
  database="retail",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()


file = open("CompRetail.csv")
reader = csv.reader(file)
result = [[item for item in row if item != ''] for row in reader]

val = []
print(len(result))
#['1608680', 'ALDI', '1305 NORTH RUSSELL ST', 'MARION ', 'IL', '62959', '618-993-6676']
for row in result:
	val.append((row[0], row[1], row[2], row[3], row[4]));

print(len(val))



# +----------+--------------+------+-----+---------+-------+
# | Field    | Type         | Null | Key | Default | Extra |
# +----------+--------------+------+-----+---------+-------+
# | ceres_id | varchar(20)  | NO   | PRI | NULL    |       |
# | banner   | varchar(100) | YES  |     | NULL    |       |
# | street   | varchar(50)  | YES  |     | NULL    |       |
# | city     | varchar(50)  | YES  |     | NULL    |       |
# | state    | varchar(50)  | YES  |     | NULL    |       |
# +----------+--------------+------+-----+---------+-------+




sql = "INSERT INTO stores (ceres_id, banner, street, city, state) VALUES (%s, %s, %s, %s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 