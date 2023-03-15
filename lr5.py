import re
import time
#timer = tim
io = open("vasya.txt", "w")

try:
    spreadsheet = open("74.csv", "r", errors="ignore")
    for value in spreadsheet:
        if time.strptime(value,"%m-%d-%Y "):
            io.write(re.sub("[^0-9][\-\:\]]",'',value))
    spreadsheet.close()
except Exception as ex:
    print(ex)

