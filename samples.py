import re
import random
import pandas as pd
try:
    spreadsheet = open("vasya.txt", "r", errors="ignore")
    spreadsheet = spreadsheet.readlines()
    f = open('test.csv', 'w')
    TSample = []
    TrSample = []
    while len(TSample) != 346: # 494*.7
        eh = random.randint(0,494)
        TSample.append(spreadsheet[eh])
        spreadsheet.pop(eh)
    while len(TrSample) != 148: #494*.3
        eh = random.randint(0, 494)
        TrSample.append(spreadsheet[eh])
        spreadsheet.pop(eh)


except Exception as ex:
    print(ex)
