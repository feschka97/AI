io = open("vasya.txt","w")
dictator = []
while True:
    try:
        spreadsheet = open("74.csv","rb")
        for value in spreadsheet:
            if value.isascii:
                io.write(value)
            spreadsheet.close()
        

        break
    except Exception as ex:
        print(ex)
print(dictator)