import re
import random
import pandas as pd
try:
    cases = {0,1}
    values1 = [346,395]
    values2 = [148,99]
    TSample = []
    TrSample = []
    for value in cases: #346/148 - 70%/30%; 395/99 - 80%/20%
        spreadsheet = open("vasya.txt", "r", errors="ignore")
        spreadsheet = spreadsheet.readlines()
        while len(TSample) < values1[value]:
            eh = random.randint(0,len(spreadsheet)-1)
            TSample.append(spreadsheet[eh])
            spreadsheet.pop(eh)
        TrSample = spreadsheet.copy()
        print("жопа")

except Exception as ex:
    print(ex)
