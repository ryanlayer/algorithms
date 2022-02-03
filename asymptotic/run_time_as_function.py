import time

import matplotlib
import pylab

import numpy as np


def square(n):
    r = 0
    for i in range(n):
        for j in range(n):
            r+=1
    return r

def linear(n):
    r = 0
    for i in range(n):
        r+=1
    return r


fig = matplotlib.pyplot.figure(figsize=(4,4),dpi=300)
ax = fig.add_subplot(1,1,1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_xlabel('Input size')
ax.set_ylabel('Time (microsecond)')

for func in [linear, square]:
    X = []
    Y = []
    for n in range(1,10000,1000):
        start = time.time()
        r = func(n)
        end = time.time()
        X.append(n)
        print(n,end-start)
        Y.append(1000000*(end - start)) #micro second


    ax.plot(X,Y,'.',lw=0)

    f = np.polyfit(X,Y,2)
    print(f)
    p = np.poly1d(f)
    xp = np.linspace(1,10000,1000)

    ax.plot(xp,p(xp))

    eq = '{:.1e}'.format(float(f[0])) + 'n^2 +'\
         ' {:.1e}'.format(float(f[1])) + 'n +' \
         ' {:.1e}'.format(float(f[2]))
         

    ax.text(X[-1],Y[-1],eq, size=8)
    

matplotlib.pyplot.savefig('runtime.png', bbox_inches='tight')

