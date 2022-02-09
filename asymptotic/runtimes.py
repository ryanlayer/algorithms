import matplotlib
import pylab
import numpy as np


def set_ax(ax,x=False,y=False):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    if x:
        ax.set_xlabel('Input size')
    if y:
        ax.set_ylabel('Run time')
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])

fig = matplotlib.pyplot.figure(figsize=(7,1),dpi=300)



x = np.array(range(1,40))

ax = fig.add_subplot(1,6,1)
set_ax(ax)
ax.plot(x,np.log(x),lw=1, label='$\log n $',c='C0')
ax.plot(x,x,lw=1, label='$n$',c='C1')
ax.plot(x,x*np.log(x),lw=1, label='$n\log n$',c='C2')
ax.legend(frameon=False,fontsize=6)

ax = fig.add_subplot(1,6,2)
set_ax(ax)
ax.plot(x,x*np.log(x),lw=1, label='$n\log n$',c='C2')
ax.plot(x,x**2,lw=1, label='$n^2$',c='C3')
ax.legend(frameon=False,fontsize=6)

ax = fig.add_subplot(1,6,3)
set_ax(ax)
ax.plot(x,x**2,lw=1, label='$n^2$',c='C3')
ax.plot(x,x**3,lw=1, label='$n^3$', c='C4')
ax.legend(frameon=False,fontsize=6)

ax = fig.add_subplot(1,6,4)
set_ax(ax)
ax.plot(x,x**3,lw=1, label='$n^3$', c='C4')
ax.plot(x,x**4,lw=1, label='$n^4$', c='C5')
ax.legend(frameon=False,fontsize=6)

ax = fig.add_subplot(1,6,5)
set_ax(ax)
ax.plot(x,x**4,lw=1, label='$n^4$', c='C5')
ax.plot(x,2**x,lw=1, label='$2^n$', c='C6')
ax.legend(frameon=False,fontsize=6)

f = []
for i in x:
    f.append(np.math.factorial(i))

ax = fig.add_subplot(1,6,5)
set_ax(ax)
ax.plot(x,2**x,lw=1, label='$2^n$', c='C6')
ax.plot(x,f,lw=1, label='$n!$', c='C7')
ax.legend(frameon=False,fontsize=6)
matplotlib.pyplot.savefig('runtimes.png', bbox_inches='tight')
