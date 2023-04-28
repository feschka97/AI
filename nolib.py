class BruhMemento(Exception): pass

def Checkque(stre):
    try:
        for i in indeces:
            if stre[i].isdigit():
                continue
            else:
                raise BruhMemento
        for uh in minus:
            if stre[uh] == '-':
                continue
            else:
                raise BruhMemento
        for em in tab:
            if stre[em] == '\t':
                continue
            else:
                raise BruhMemento
        return True
    except BruhMemento:
        tablo.write(stre)
try:
    io = open("vasya.txt", "w")
    spreadsheet = open("74.csv", "r", errors="ignore")
    array = spreadsheet.readlines()
    indeces = [1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 23]
    minus = [3, 6]
    tab = [11, 17, 20]
    tablo = open("errorsbruh.txt", 'w')
    for value in array:
        if (Checkque(value)):
            io.write(value)
    spreadsheet.close()
except Exception as ex:
    print(ex)
