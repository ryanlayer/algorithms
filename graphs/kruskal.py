from operator import itemgetter

def UF_init(n):
    return [i for i in range(n)]

def UF_find(parent, a):
    if parent[a] != a:
        return UF_find(parent, parent[a])
    else:
        return a

def UF_union(parent, a, b):
    parent[UF_find(parent, a)] = UF_find(parent, b)

def Kruskal(V, E, w):
    edges = [ [w[e],e] for e in w]
    T = []

    parent = UF_init(len(V))

    for w,(u,v) in sorted(edges):
        if UF_find(parent, u) != UF_find(parent, v):
            T.append((u,v))
            UF_union(parent, u, v)
    return T

L = 0; M = 1; N = 2; O = 3; P = 4

V = {L, M, N, O, P}
E = [[M, N], [L,N,O], [L,M,P], [M, P], [N,O]]

w = { (L,M) : 5, (L,N) : 6, 
      (M,N) : 1, (M,O) : 3,
      (N,P) : 4,
      (O,P) : 2 }

T = Kruskal(V, E, w)

print(T)
