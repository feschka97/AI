import numpy

import fourth_calc as fc
import pandas
import matplotlib.pyplot as plt
import random
from collections import Counter

def main():
    file = pandas.read_csv("5.csv")
    plt.hist(file.ale, bins=100)
    plt.show()

    a = Counter(file.node_density.values)
    count = []
    for value in a:
        count.append(value)
    plt.pie(count,autopct='%1.1f%%',labels=a.keys())
    plt.xlabel("node_density")
    plt.show()
    file.trans_range.sort_values()
    plt.polar(list(dict.fromkeys(file.trans_range.values)))
    plt.xlabel("trans_range")
    plt.show()

    plt.plot(file.ale.values)
    plt.xlabel("ale")
    plt.show()

    mean, sigma, varsize, median, interq, ratethreesigma, disper = 0,0,0,0,0,0,0
    data = file.anchor_ratio.values

    for value in data:
        mean += value
    mean /= len(data)
    print(mean,'- среднее значение')

    for cyclevar in range(len(data)):
        dis = data[cyclevar]-mean
        dis *= dis
        disper += dis
    disper /= len(data) - 1
    print(disper, '- дисперсия')

    sigma = fc.sqrt(disper)
    print(sigma, '- среднеквадратичное отклонение')

    varsize = max(data) - min(data)
    print(varsize, "- размах вариации")

    median = fc.median(data)
    print(median, '- медиана')

    interq = fc.iqr(data)
    print(interq, '- интерквантильный размах')

    print('матрица корреляции -', file.corr())

    haha = numpy.poly1d(numpy.polyfit(file.ale,file.sd_ale,1))
    plt.plot(file.ale,file.sd_ale)
    plt.subplot(fc.line(haha,max(file.sd_ale.values)))
    plt.show()




if __name__ == "__main__":
    main()

