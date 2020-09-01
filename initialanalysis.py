import csv
import simplejson as json
from pathlib import Path

file_name = input("File name?")

file = open("input/" + file_name)
reader = csv.reader(file)
result = [[item for item in row if item != ''] for row in reader]

stores = {}
result = result[11:]
result = result[:-3]

Months = {
        "1": "Jan",
        "2": "Feb",
        "3": "Mar",
        "4": "Apr",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "Aug",
        "9": "Sep",
        "10": "Oct",
        "11": "Nov",
        "12": "Dec"
         }

date_index = result[1][5].split("/")

date = Months[date_index[0]] + date_index[2][2:]

date_index = [date_index[0], date_index[2]]
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
                
WM = {"date":date_index}
ALDI = {"date":date_index}
KROGER = {"date":date_index}
RULER = {"date":date_index}
TARGET = {"date":date_index}
COSTCO = {"date":date_index}
SAL = {"date":date_index}
SAMS = {"date":date_index}
FT = {"date":date_index}

WMkey = [16473, 1001021, 1001188, 1001265, 100145, 100152, 100172, 100173, 100196, 1002213, 100243, 1002600, 100262, 100295, 100313, 100354, 10037, 100377, 100436, 1004695, 1005313, 100648, 10065, 100653, 10069, 10095, 10099, 101071, 101418, 101514, 10201, 10253, 10256, 102616, 10328, 10361, 104216, 104222, 104252, 1043022, 10435, 1608554, 1608566, 1608641, 1608644, 1608645, 1608815, 1609039, 235791, 31684, 379999, 63699]

ALDIkey = [1608619, 1608680, 1608681, 1608682, 1608683, 1608684, 1608685, 1608686, 1608687, 1608688, 1608689, 1608690, 1608691, 1608692, 1608693, 1608694, 1608695, 1608696, 1608697, 1608698, 1608699, 1608700, 1608701, 1608702, 1608703, 1608704, 1608705, 1608706, 1608707, 1608708, 1608710, 1608711, 1608712, 1608713, 1608714, 1608715, 1608716, 1608717, 1608718, 1608719, 1608720, 1608721, 1608722, 1608723, 1608743, 1608794, 1608803, 1608948, 1608970, 1608971]

KROGERkey = [4000, 4002, 4003, 4010, 4011, 4012, 4013, 4014, 4015]

RULERkey = [1608453, 1608475, 1608500, 1608504, 1608526, 1608545, 1608565, 1608725, 1608726, 1608836]

TARGETkey = [100234, 100422, 1004255, 100699, 10420, 106241, 12723, 15025, 18383, 18571, 197005, 222222, 23004, 23501, 250366, 291066, 34000, 400000, 445566, 47012, 560123, 567444, 79555]

FTkey = [1608474, 1608601, 1608602, 1608786, 1608821, 1608883]

COSTCOkey = [1608663, 1608894, 420001]

SAMSkey = [102356, 130550, 147832, 159886, 226547, 5569866, 631314, 631569, 631636, 6338555, 66223344]

SALkey = [1000000, 10000421, 1000404, 1000405, 1000407, 1000408, 1000409, 1000411, 1000412, 1000413, 1000414, 1000416, 1000417, 1000419, 1000420, 1000422, 1000424, 1000425, 1000427, 1000864, 1608476, 1608613, 1608759, 1608876, 1609046, 34671, 400004]


for store in store_totals:
    if store in WMkey:
        WM[store] = store_totals[store]
    if store in ALDIkey:
        ALDI[store] = store_totals[store]
    if store in KROGERkey:
        KROGER[store] = store_totals[store]
    if store in RULERkey:
        RULER[store] = store_totals[store]
    if store in TARGETkey:
        TARGET[store] = store_totals[store]
    if store in FTkey:
        FT[store] = store_totals[store]
    if store in COSTCOkey:
        COSTCO[store] = store_totals[store]
    if store in SAMSkey:
        SAMS[store] = store_totals[store]
    if store in SALkey:
        SAL[store] = store_totals[store]


banner_list = [["WM",WM] ,["ALDI", ALDI],["KROGER", KROGER], ["RULER", RULER], ["FT", FT], ["COSTCO", COSTCO], ["SAMS", SAMS], ["SAL", SAL], ["TARGET", TARGET]]


for each in banner_list:
    jsonline = json.dumps(each[1])

    f = open(Path("banner/" + each[0] + "/" + each[0] + date + ".json"),"w")
    f.write(jsonline)
    f.close()