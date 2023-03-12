io = open("vasya.txt","w")
dictator = []
try:
    spreadsheet = open("74.csv","r",errors="ignore")
    for value in spreadsheet:
        if value.isascii:
            io.write(value)
    spreadsheet.close()
except Exception as ex:
    print(ex)
        
print(dictator)