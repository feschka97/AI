import re
import random
import pandas as pd
try:
    spreadsheet = open("vasya.txt", "r", errors="ignore")
    spreadsheet = spreadsheet.readlines()
    f = open('test.csv', 'w')
    cases = {0,1}
    values1 = [346,395]
    values2 = [148,99]
    TSample = []
    TrSample = []
    for value in cases:
        while len(TSample) != values1[value]:
            eh = random.randint(0,494)
            TSample.append(spreadsheet[eh])
            spreadsheet.pop(eh)
        while len(TrSample) != values2[value]:
            eh = random.randint(0, 494)
            TrSample.append(spreadsheet[eh])
            spreadsheet.pop(eh)


except Exception as ex:
    print(ex)
