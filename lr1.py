def deone():
    text = input("Введите слово:")
    while text == "":
        text = input("Введите слово:")
    letter = input("Введите букву в слове для поиска:")
    if letter in text:
        print("Нашли букву '" + letter + "' в слове \"" + text + "\"")
        print(text.index(letter) + 1)
    else:
        print("Таковой буквы нема")

def detwo():
    lim = int(input("Введите n для предельного числа в последовательности Фибоначчи:"))
    curr=1
    next=1
    while next < lim:
        print(curr)
        curr +=next
        print(next)
        next +=curr


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
    io = int(input("Введите число:"))
    while (True):
        action = input("1) Сложение \n 2) Вычитание \n 3) Деление \n 4) Умножение \n 5) Выход \n")
        match action:
            case "1": io+=int(input("Введите слагаемое:")); print(io," - результат");action=0
            case "2": io-=int(input("Введите вычитаемое:")); print(io," - результат");action=0
            case "3": io/=int(input("Введите делитель:")); print(io," - результат");action=0
            case "4": io*=int(input("Введите множитель:")); print(io," - результат");action=0
            case "5":break
            case _: print("Паника!");break
    print(io)
try:
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
