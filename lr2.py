import random


def deone():
    print(sum(listin))
def detwo():
    print(max(listin))
def dethree():
    var=0
    for var in listin:
        if listin.count(var) !=0:
            print(var," - дубликат")
def defour():
    min = min(listin)
    max= max(listin)
    listin[listin.index(min)] = max
    listin[listin.index(max)] = min
def defah():
    frommax = 0
    frommax_team=[]
    frommax_team.append(max(listin))
    current = listin.index(random.randint(0, len(listin)))
    while max(frommax_team)+frommax_team[len(frommax_team)] < current:
        frommax_team.append(current)
        frommax_team.sort()
        frommax=frommax_team[0]+frommax_team[1]
        listin.remove(current)
        print("Добавили в игрока с ПП ", current)
        current = listin.index(random.randint(0,listin.count()))
        print("Текущее ПП в команде: ", sum(frommax_team))




try:
    rook=0
    listin = []
    while rook != random.randint(0,100):
        listin.append((random.randint(0,100)))
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
