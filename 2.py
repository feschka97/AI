# coding=utf8
import re
import time
timer = time.time()
io = open("vasya.txt", "w")

try:
    spreadsheet = open("74.csv", "r", errors="ignore")
    for value in spreadsheet:
        if time.strptime(re.sub("[^\d]", '', value),"%m%d%Y%H%M%f"):
            io.write(re.sub("[^\d\n\-\:\t]", '', value))
    spreadsheet.close()
    print('Затрачено:',time.time()-timer)
except Exception as ex:
    print(ex)

