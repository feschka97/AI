def Fixup(stre,mistakes):
    stre = stre.replace(stre[mistakes.index(1)],'')
    mistakes[mistakes.index(1)] = 0
    print(stre[22]) # '"12-16-1199	8l:	33	8"'
                    # '"12-16-1990	08:00	58	205"'
    if (Checkque(stre)):
        return stre


def Checkque(stre):
    mistakes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in indeces:
        if stre[i].isdigit():
            mistakes[i] = 0
            continue
        else:
            mistakes[i] = 1
    for uh in minus:
        if stre[uh] == '-':
            mistakes[uh] = 0
            continue
        else:
            mistakes[uh] = 1
    for em in tab:
        if stre[em] == '\t':
            mistakes[em] = 0
            continue
        else:
            mistakes[em] = 1
    if mistakes == [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]:
        return True
    else:
        stre = Fixup(stre,mistakes)

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
