import random

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def partition(A, l, r, rand=False):
    if rand:
        swap(A,l,random.randint(l,r-1))
    p = A[l]
    i = l + 1
    for j in range(l+1, r):
        if A[j] < p:
            swap(A, i, j)
            i += 1
    swap(A, l, i-1)
    return i-1

def quicksort(A, l, r, rand=False):
    if r <= l:
        return
    p_i = partition(A, l, r+1, rand=rand)
    quicksort(A, l, p_i -1, rand=rand)
    quicksort(A, p_i + 1, r, rand=rand)

if __name__ == '__main__':
    A = [4, 5, 8, 9, 2 , 1, 3, 7, 6]
    quicksort(A, 0, len(A)-1, rand=True)
    print(A)
