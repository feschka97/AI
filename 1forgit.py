import time
import numpy
timer = time.time()
try:
    spreadsheet = numpy.loadtxt("74.csv",dtype=str)
    print('Затрачено:',time.time()-timer)
except Exception as ex:
    print(ex)
