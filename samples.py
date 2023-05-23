import random
cases = {0,1}
for value in cases:
	spreadsheet = open("vasya.txt", "r", errors="ignore")
	spreadsheet = spreadsheet.readlines()
	values1 = [int(len(spreadsheet)*0.7), int(len(spreadsheet)*0.8)]
	values2 = [len(spreadsheet)-values1[0], len(spreadsheet)-values1[1]]
	Tren = []
	while len(Tren) < values1[value]:
		eh = random.randint(0,len(spreadsheet)-1)
		Tren.append(spreadsheet[eh])
		spreadsheet.pop(eh)
	Test = spreadsheet.copy()
