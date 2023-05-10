def Fixup(stre,mistakes):
    stray = ''
    for indx in range(len(mistakes)):
        stray+=stre[indx]


    if (Checkque(stre)):
        return stray


def Checkque(stre):
    for i in indeces:
        if stre[i].isdigit():
            mistakes[i] = 0
            continue
        else:
            mistakes[i] = 1
            break
    for uh in minus:
        if stre[uh] == '-':
            mistakes[uh] = 0
            continue
        else:
            mistakes[uh] = 1
            break
    for em in tab:
        if stre[em] == '\t':
            mistakes[em] = 0
            continue
        else:
            mistakes[em] = 1
            break
    if mistakes == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
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
    mistakes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for value in array:
        if (Checkque(value)):
            io.write(value)
        else:
            value = Fixup(value, mistakes)
            io.write(value)
    spreadsheet.close()
except Exception as ex:
    print(ex)
