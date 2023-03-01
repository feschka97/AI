
def deone():
    print(sum(listin), "- сумма")
    prod=1
    for index in listin:
        prod *=index
    print(prod, "- произведение")


def detwo():
    print(max(listin), "- максимальный член списка")

def dethree():
    var=0
    for var in listin:
        if listin.count(var) > 1:
            print(var," - дубликат")
        else:
            print("Дубликатов нет")
            break


def defour():
    minimal = min(listin)
    maximal= max(listin)
    listin[listin.index(minimal)] = maximal
    listin[listin.index(maximal)] = minimal

def defah():
    frommax = 0
    frommax_team=[]
    frommax_team.append(max(listin))
    lower=0
    for current in listin:
        if max(frommax_team)+lower > current:
            print("Начало")
            frommax_team.append(current)
            frommax_team.sort()
            frommax=frommax_team[0]+frommax_team[1]
            del listin[listin.index(current)]
            print("Добавили в игрока с ПП ", current)
            lower=frommax_team[-1]
            print("Текущее ПП в команде: ", sum(frommax_team))



try:
    rook=0
    listin = [608,602,251,291,841,415,395,952,287,206,552,525,811,995,358,589,897,892,926,977,770,921,214,722,227,732,320,203,262,623,231,315]
    listin.sort()
    choice = 1
    choice = input("Задание: \n")
    match choice:
        case "1": deone()
        case "2": detwo()
        case "3": dethree()
        case "4": defour()
        case "5": defah()
        case _: print("Паника!")
except Exception as exx:
    print("Вылезло исключение - ", exx)
