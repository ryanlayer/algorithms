import quicksort
import mergesort
import random
import time



m_times = []
q_times = []
x = []
for i in range(1000, 10000, 1000):
    A = random.sample(range(1, i*10), i)
    AA = [a for a in A]

    m_tic = time.time()
    R = mergesort.mergesort(A)
    m_toc = time.time()

    q_tic = time.time()
    quicksort.quicksort(A, 0, len(A)-1)
    q_toc = time.time()

    m_times.append(m_toc - m_tic)
    q_times.append(q_toc - q_tic)
    x.append(i)


import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x, m_times, label='mergesort')
ax.plot(x, q_times, label='quicksort')
ax.legend(frameon=False)
ax.set_xlabel('List size')
ax.set_ylabel('Run time')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
fig.savefig('m_v_q_sort.png')
