import time
timer = time.time()
try:
    spreadsheet = open("74.csv")
    print('Затрачено:',time.time()-timer)
except Exception as ex:
    print(ex)
