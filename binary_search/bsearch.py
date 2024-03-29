import numpy as np

def bsearch_recursive(lst, x):
    n = len(lst)
    if n == 0: return False
    
    if n == 1:
        if x == lst[0]: return True
        else: return False
        
    if n % 2 == 0:
        midIndex = int(n/2)
        mid = lst[midIndex]
        if x < mid:
            return bsearch_recursive(lst[0:midIndex], x)
        else:
            return n/2 + bsearch_recursive(lst[midIndex:n], x)
    else:
        midIndex = int((n-1)/2)
        mid = lst[midIndex]
        if x == mid:
            return midIndex
        elif x < mid:
            return bsearch_recursive(lst[0:midIndex], x)
        else:
            return n/2 + bsearch_recursive(lst[midIndex:n], x)

#print(bsearch_recursive([1,2,3,4,5,6], 5))

def bsearch_while(lst, x):
    lo = -1
    hi = len(lst)
    mid = -1
    while ( hi - lo > 1):
        mid = int((hi+lo)/2)
        if lst[mid] < x:
            lo = mid
        else:
            hi = mid
    return hi

#print(bsearch_while([1,2,3,4,5,6], 5))

import random
import time

lst = random.sample(range(1,3000000000),1000000)
lst.sort()
X = random.sample(range(1,3000000000),100)

rec_times = []
while_times = []

for x in X:
    start = time.time()
    h = bsearch_recursive(lst, x)
    end = time.time()
    rec_time = end - start

    rec_times.append(rec_time)

    start = time.time()
    h = bsearch_while(lst,x)
    end = time.time()
    while_time = end - start

    while_times.append(while_time)

print(np.mean(rec_times))
print(np.mean(while_times))
print(np.mean(rec_times)/ np.mean(while_times))


