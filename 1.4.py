import fourth_calc

try:
    io = int(input("Введите число:"))
    while (True):
        print(io)
        action = input(" 1)Сложение \n 2)Вычитание \n 3)Деление \n 4)Умножение \n 5)Остаток деления на\n 6)Синус\n 7)Косинус\n 8)Тангенс\n 9)Котангенс\n 10)Выход \n")
        match action:
            case "1": io+=int(input("Введите слагаемое:")); print(io," - результат");action=0
            case "2": io-=int(input("Введите вычитаемое:")); print(io," - результат");action=0
            case "3": io/=int(input("Введите делитель:")); print(io," - результат");action=0
            case "4": io*=int(input("Введите множитель:")); print(io," - результат");action=0
            case "5": io=fourth_calc.remainder(io,int(input("Введите делитель:")));print(io,"-результат");action=0
            case "6": io=fourth_calc.sine(io);print(io,"-результат");action=0
            case "7": io=fourth_calc.cosine(io);print(io,"-результат");action=0
            case "8": io=fourth_calc.tangent(io);print(io,"-результат");action=0
            case "9": io=fourth_calc.cotangent(io);print(io,"-результат");action=0
            case "10":break
            case _: print("Паника!");break
    print(io)
except Exception as exx:
    print("Вылезло исключение - ", exx)

