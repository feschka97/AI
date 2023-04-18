import random
try:
    
    spreadsheet = open("vasya.txt", "r", errors="ignore")
    spreadsheet = spreadsheet.readlines()
    Test =[]
    while len(Test) < 60: #494 * .12 = 60
        eh = random.randint(0,len(spreadsheet)-1)
        Test.append(spreadsheet[eh])
        spreadsheet.pop(eh)
    Comp = spreadsheet.copy()
    Vald = Comp[:int((len(Comp))/7)]
    Tren = Comp[int((len(Comp)/7)):]
    print("zhopa")


except Exception as ex:
    print(ex)
