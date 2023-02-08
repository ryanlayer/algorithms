import heapq

def Prims(V, E, w):
    X = {0} # the nodes in the tree, pick any node as the starting node

    
    Q = []
    for y in E[0]:
        heapq.heappush(Q, (w[(0,y)], (0,y)))

    T = [] # the edges in the tree

    while X != V:
        #get the min edge u,v where u is in X and v is not in X
        d,(u,v) = heapq.heappop(Q) # min edge, u is in X, just test X

        while v in X:
            d,(u,v) = heapq.heappop(Q) # min edge, u is in X, just test X

        X.add(v)
        T.append([u,v])

        for y in E[v]:
            heapq.heappush(Q, (w[(v,y)], (v,y)))

    return T

A = 0
B = 1
C = 2
D = 3

V = {A, B, C, D}
E = [[B, C], [A,C,D], [A,B,D], [B, C]]

w = { (A,B) : 2, (A,C) : 3, 
      (B,A) : 2, (B,C) : 1, (B,D) : 4,
      (C,A) : 3, (C,B) : 1, (C,D) : 5,
      (D,B) : 4, (D,C) : 5 }

T = Prims(V, E, w)
