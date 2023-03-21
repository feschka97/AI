import math

def func(x,y):
    func1 = pow(math.e,(math.log(math.e,4*20)))+pow(x,3)-5*y
    func2 = math.sqrt((pow(8,x)-y*y)*math.cos(math.pi/3)) / math.sin(math.pi/6)
    return "Значения функций:",func1,func2, "Округлённые значения функции:",round(func1),round(func2)



f = func(int(input("Введите x ")),int(input("Введите y ")))
print (f)



