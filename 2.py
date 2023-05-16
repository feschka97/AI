import re
io = open("vasya.txt", "w")
try:
    spreadsheet = open("74.csv", "r", errors="ignore")
    for value in spreadsheet:
        if re.fullmatch("\"\d\d-\d\d-\d\d\d\d\s\d\d:\d\d\t\d\d\t\d\d\d\"", value):
            io.write(value)
        else:
            print(value)
    spreadsheet.close()
    
except Exception as ex:
    print(ex)

