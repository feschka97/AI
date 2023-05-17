import re
io = open("74.csv", mode="r")
spreadsheet = io.readlines()
mean = 0
median = 0
mode = 0
counts = []
length = len(spreadsheet)
for index in range(length):
    spreadsheet[index] = int(re.sub("\"\d\d-\d\d-\d\d\d\d\s\d\d:\d\d\t\d\d\t", '', spreadsheet[index]).removesuffix('\"\n'))
for value in spreadsheet:
    mean += value
    counts.append(spreadsheet.count(value))
mean /= length

if length % 2 == 0:
    median = spreadsheet[length//2]
else:
    index = int(length/2)
    median = (spreadsheet[index]+spreadsheet[index+1])/2

mode = spreadsheet[counts.index(max(counts))]



print(mean, "- среднее значение")
print(median, "- медиана")
print(mode, "- мода, с ",max(counts))
#дисперсия
