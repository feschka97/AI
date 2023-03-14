import re

io = open("vasya.txt", "w")

try:
    spreadsheet = open("74.csv", "r", errors="ignore")
    for value in spreadsheet:
        if value.isascii:
            io.write(re.sub("[^0-9][\-\:\]]",'',value))
    spreadsheet.close()
except Exception as ex:
    print(ex)

