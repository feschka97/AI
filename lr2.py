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
