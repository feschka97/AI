import random
k = 7
spreadsheet = open("74.csv", "r", errors="ignore")
spreadsheet = spreadsheet.readlines()
Test =[]
oldLen = int(len(spreadsheet)*0.12)
while len(Test) < oldLen:
	eh = random.randint(0,len(spreadsheet)-1)
	Test.append(spreadsheet[eh])
	spreadsheet.pop(eh) # 12%
Comp = spreadsheet.copy()
for podmn in range(1,k+1):
	split = int((len(Comp))/k)
	Vald = Comp[split*(podmn-1):split*podmn]
	Tren = [x for x in Comp if (x not in Vald)]
	print(f'{podmn}-ая валидаточная часть: {Vald}')
	print(f'{podmn}-ая тренировочная часть: {Tren}')
