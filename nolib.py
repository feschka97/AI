def Fixup(str):
    print(str)
    str = input("Введите переправленный вариант\n")
    return str
def Checkque(str):
    for i in indeces:
        if str[i].isdigit():
            continue
        else:
            str = Fixup(str)

    for uh in minus:
        if str[uh] == '-':
            continue
        else:
            str = Fixup(str)            
    for em in tab:
        if str[em] == '\t':
            continue
        else:
            str = Fixup(str)            
    return str
try:
    io = open("vasya.txt", "w")
    spreadsheet = open("74.csv", "r", errors="ignore")
    array = spreadsheet.readlines()
    indeces = [1,2,4,5,7,8,9,10,12,13,15,16,18,19,21,22,23]
    minus = [3,6]
    tab = [11,17,20]
    for value in array:        
        io.write(Checkque(value))
    spreadsheet.close()
except Exception as ex:
        print(ex)


