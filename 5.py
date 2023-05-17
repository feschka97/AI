import re
io = open("74.csv", mode="r")
spreadsheet = io.readlines()
mean = 0
median = 0
mode = 0
newb = {}
length = len(spreadsheet)
for value in spreadsheet:
    newb.
for value in newb:
    mean += value
mean /= length
if length % 2 == 0:
    median = newb[length//2]
else:
    index = int(length/2)
    median = (newb[index]+newb[index+1])/2
for loop in length:
    newb[loop].count()





print(mean, "- среднее значение")
print(median, "- медиана")
print(mode, "-мода")
