import re
import numpy as np

from sklearn import preprocessing as pp

io = open("74.csv", mode="r")
spreadsheet = io.readlines()
length = len(spreadsheet)

for index in range(length):
    spreadsheet[index] = int(
        re.sub("\"\d\d-\d\d-\d\d\d\d\s\d\d:\d\d\t\d\d\t", '', spreadsheet[index]).removesuffix('\"\n'))

mean = 0
for value in spreadsheet:
    mean += value
mean /= length

disper = 0
for cyclevar in range(length):
    dispa = spreadsheet[cyclevar] - mean
    dispa *= dispa
    disper += dispa
disper /= length - 1

for cyclevar in range(length):
    spreadsheet[cyclevar] = (spreadsheet[cyclevar] - mean) / disper

normalZ = np.array(spreadsheet)

print(normalZ, "- данные из Z-нормализации\n")
scaled = pp.scale(normalZ)
print(scaled, "- масштабированные данные из Z-нормализации")

normalMinMax =[]
for value in spreadsheet:
    a = -1
    b = 1
    X = a + (value - min(spreadsheet))/(max(spreadsheet)-min(spreadsheet)) * (b-a)
    normalMinMax.append(value)
print(normalMinMax, "- данные из минимаксной нормализации")
print(pp.scale(normalMinMax), "- масштабированные данные из минимаксной нормализации")
