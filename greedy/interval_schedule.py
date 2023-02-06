from operator import itemgetter


def intersect(a, b):
    return a[0] <= b[1] and b[0] <= a[1]


def greedy_first_to_end(L):
    sorted(L, key=itemgetter(1))

    I = []

    while len(L) > 0:
        i = L.pop(0)
        I.append(i)

        to_rem = [] # make a list of things to remove
        for l in range(len(L)):
            if intersect(i, L[l]):
                to_rem.append(l)

        sorted(to_rem, reverse=True) # remove from right to left
        for l in to_rem:
            L.pop(l)

    return(I)

L = [(1,3), (2,8), (4, 6), (7,10), (8,12)] 
print(greedy_first_to_end(L))
