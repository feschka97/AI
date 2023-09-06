import matplotlib
import matplotlib.pyplot as plt

import fourth_calc

import numpy as np

matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['axes.unicode_minus'] = False
# to not cut off bottom axes
matplotlib.rcParams.update({'figure.autolayout': True})

Ns = 1500
x = np.zeros((Ns, 1))
y = np.zeros((Ns, 1))

limit = 1

upper = limit * np.pi
lower = - limit
dx = (upper - lower) / Ns


def PlotFunction(x):
    return fourth_calc.th(12 * x)

for i in range(0, Ns):
    x[i, 0] = lower + i * dx


for i in range(0, Ns):
    y[i, 0] = PlotFunction(x[i, 0])

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_ylim([-2.333,2.333])
ax1.set_xlim([lower, limit])

ax1.plot(x, y)

leg = ax1.legend(loc=1)

plt.draw()
plt.savefig('fig1.eps')
plt.show()



