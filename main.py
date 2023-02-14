

def deone():
    text = input("Введите слово:")
    letter = input("Введите букву в слове для поиска:")
    if letter in text:
        print("Нашли букву '" + letter + "' в слове \"" + text + "\"")
        print(text.index(letter) + 1)
    else:
        print("Таковой буквы нема")
def detwo():
    lim = int(input("Введите n дляя предельного числа в последовательности Фибоначчи:"))
    curr=1
    next=1
    while next < lim:
        curr +=next
        next +=curr
    print(curr)
def dethree():
    fact = int(input("Введите n для факториала:"))
    start = 1
    output = 1
    while start <= fact:
        output *=start
        start+=1
    print(output)
def defour():
    binary = bin(int(input("Введите число:")))
    print(binary.count("1"))

def defah():
    print (0)








choice = 1
choice = input("Задание: \n")
match choice:
    case "1": deone()
    case "2": detwo()
    case "3": dethree()
    case "4": defour()
    case "5": defah()
    case _: print("Паника!")
