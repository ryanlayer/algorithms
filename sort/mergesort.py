def merge(A, B):
    a = 0
    b = 0
    R = []

    while a < len(A) or b < len(B):
        if a == len(A) or (b < len(B) and A[a] >= B[b]):
            R.append(B[b])    
            b+=1
        else:
            R.append(A[a])    
            a+=1

    return R

def mergesort(L):
    if len(L) <= 1:
        return L
    A = mergesort(L[:int(len(L)/2)])
    B = mergesort(L[int(len(L)/2):])
    return merge(A, B)

print(mergesort([4, 1, 6, 3, 2, 5]))
