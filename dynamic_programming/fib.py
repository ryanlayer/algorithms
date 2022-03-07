import sys
import time
import matplotlib
import pylab


def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    f = fib(n-1) + fib(n-2)
    return f

def fib_memo(n, MEMO):
    if n in MEMO: 
        return MEMO[n]
    if n == 0 : return 0
    if n == 1 : return 1
    f = fib_memo(n-1, MEMO) + fib_memo(n-2, MEMO)
    MEMO[n] = f
    return f

def fib_bottom_up(n):
    MEMO = {}
    for i in range(n+1):
        f = None
        if i == 0 : f = 0
        elif i == 1 : f = 1
        else:
            f = MEMO[i-1] + MEMO[i-2]
        MEMO[i] = f 
    return MEMO[n]
    

n = int(sys.argv[1])

#fib_times = []
#for i in range(1,n):
#    start = time.time()
#    f_i = fib(i)
#    end = time.time()
#    fib_times.append((end-start))

fib_memo_times = []
for i in range(1,n):
    MEMO = {}
    start = time.time()
    f_i = fib_memo(i, MEMO)
    end = time.time()
    fib_memo_times.append((end-start))

fib_bottom_up_times = []
for i in range(1,n):
    MEMO = {}
    start = time.time()
    f_i = fib_bottom_up(i)
    end = time.time()
    fib_bottom_up_times.append((end-start))

fig = matplotlib.pyplot.figure(figsize=(4,3),dpi=300)
ax = fig.add_subplot(1,1,1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlabel('Input size')
ax.set_ylabel('Time (microsecond)')

#ax.plot(range(1,n), fib_times, '.-', lw=1, label='fib')
ax.plot(range(1,n), fib_memo_times, '.-', lw=1, label='fib_memo')
ax.plot(range(1,n), fib_bottom_up_times, '.-', lw=1, label='fib_bottom_up')
ax.legend(frameon=False)

matplotlib.pyplot.savefig('runtime.png', bbox_inches='tight')

