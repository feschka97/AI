import time
import pandas
timer = time.time()
try:
 spreadsheet = pandas.read_csv("74.csv",encoding='windows-1251')
    print('Затрачено:',time.time()-timer)
except Exception as ex:
    print(ex)
