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

normal = np.array(spreadsheet)
normal = pp.normalize([normal])
print(normal, "- нормализованные данные")

scaled = pp.scale(normal,axis=1)

print(scaled, "- масштабированные данные")
