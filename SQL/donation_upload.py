import csv
from pathlib import Path
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="XO52eg?!wb",
  database="retail",
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()



file_name = input("File name?")

file = open(file_name)
reader = csv.reader(file)
result = [[item for item in row if item != ''] for row in reader]

stores = {}
result = result[11:]
result = result[:-3]


date_index = result[1][5].split("/")
date = date_index[2] + "-" + date_index[0] + "-01"
print(date)


current_store = ""
for row in result:
    if row[0] == "Donor Total":
        current_store = ""
    elif (row[1].isdigit() == False) and (row[1] != "RETAIL"):
        current_store = int(row[0])
        stores[current_store] = []
    
    else:
        if row[8] == '12/31/9999':
            pounds = row[9].replace(",", "")
            pounds = pounds[:-1]
            stores[current_store].append([row[5], row[2], row[4], float(pounds)])
        else:
            pounds = row[8].replace(",", "")
            pounds = pounds[:-1]
            stores[current_store].append([row[5], row[2], row[4], float(pounds)])

        
store_totals = {}
for line in stores:
    key = int(line)
    store_totals[key] = {}
    store_totals[key]["Store Total"] = 0
    for item in stores[key]:
        category = item[1]

        if category not in store_totals[key]:
            store_totals[key][category] = item[3]
            store_totals[key]["Store Total"] += item[3]
        else:
             store_totals[key][category] += item[3]
             store_totals[key]["Store Total"] += item[3]

# 66223344: {'Store Total': 40111.0, 'RETAIL, PRODUCE': 21080.0, 'RETAIL, MEAT AND DELI': 2855.0, 'RETAIL, MIX FOOD': 15786.0, 'RETAIL, DAIRY': 390.0}

val = []
sql = "INSERT INTO donation (ceres_id, month, produce,  meat, mix, dairy, nonfood) VALUES (%s, %s, %s, %s, %s, %s, %s)"
categories = ['RETAIL, PRODUCE', 'RETAIL, MEAT AND DELI', 'RETAIL, MIX FOOD', 'RETAIL, DAIRY', 'RETAIL, NON FOOD']
for each in store_totals:
    temp_vals = []
    for i in range(0,5):
        if categories[i] in store_totals[each]:
            temp_vals.append(store_totals[each][categories[i]])
        else:
            temp_vals.append(0)
    val.append((str(each), date, temp_vals[0], temp_vals[1], temp_vals[2], temp_vals[3], temp_vals[4]))

# print(val)



mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 



# +-------------+-------------+------+-----+---------+----------------+
# | Field       | Type        | Null | Key | Default | Extra          |
# +-------------+-------------+------+-----+---------+----------------+
# | donation_id | int         | NO   | PRI | NULL    | auto_increment |
# | ceres_id    | varchar(20) | NO   | MUL | NULL    |                |
# | month       | varchar(20) | YES  |     | NULL    |                |
# | mix         | int         | YES  |     | NULL    |                |
# | dairy       | int         | YES  |     | NULL    |                |
# | produce     | int         | YES  |     | NULL    |                |
# | meat        | int         | YES  |     | NULL    |                |
# | nonfood     | int         | YES  |     | NULL    |                |
# +-------------+-------------+------+-----+---------+----------------+




