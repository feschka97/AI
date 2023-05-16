import re

def Fixup(stre):
    


    if (Checkque(stre)):
        return stray


def Checkque(stre):
    if:
        return True
    else:
        return False


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
        else:
            value = Fixup(value, mistakes)
            io.write(value)
    spreadsheet.close()
except Exception as ex:
    print(ex)
