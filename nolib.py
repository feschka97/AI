def Fixup(str):
    str = input("Введите переправленный вариант")
    if str[1,2,4,5,7:10,12,13,15,16,18,19,21:24].isnumeric() and str[3,6]=='-'and str[11,17,20] =='\t' and str[14]=='\:':
        print("Плохой ввод")
        Fixup(str)

try:
    io = open("vasya.txt", "w")
    spreadsheet = open("74.csv", "r", errors="ignore")
    array = spreadsheet.readlines()
    indeces = [1,2,4,5,range(7,10),12,13,15,16,18,19,range(21,24)]

    for row in array:
        if [row[i] for i in indeces] and row[3,6]=='-'and row[11,17,20] =='\t' and row[14]=='\:':
            io.write(row)
        else:
            Fixup(row)
        spreadsheet.close()
except Exception as ex:
        print(ex)

