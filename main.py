

def deone():
    text = input("Введите слово:")
    letter = input("Введите букву в слове для поиска:")
    if letter in text:
        print("Нашли букву '" + letter + "' в слове \"" + text + "\"")
        print(text.index(letter) + 1)
    else:
        print("Таковой буквы нема")
def detwo():
    lim = input("Введите n:")
    curr=1
    next=1
    while next < lim:
        curr +=next
        next +=curr
    print(curr)

choice = 1
choice = input("Задание")
match choice:
    case 1: deone()
    case 2: detwo()
    case 3: dethree()
    case _: print("Паника!")
