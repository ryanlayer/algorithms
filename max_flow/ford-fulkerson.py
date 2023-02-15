def BFS_dist(E, s):
    state = ['new']*len(E)
    Q = []
    dist = [None]*len(E)
    dist[s] = -1

    pred = [None]*len(E)
    pred[s] = s

    Q.append(s)
    while len(Q) != 0:
        x = Q.pop(0)
        dist[x] = dist[ pred[x] ] + 1
        if state[x] == 'new':
            state[x] = 'old'
            for y in E[x]:
                if pred[y] == None:
                    pred[y] = x
                Q.append(y)
    return pred

def find_st_path(E, s, t):
    pred = BFS_dist(E, s)

    if pred[t] is None: return None

    path = []
    curr = t

    while pred[curr] != curr:
        prev = curr
        curr = pred[curr]
        path.append((curr,prev))

    path.reverse()
    return path

def get_min_capacity(cf, path):
    return min([cf[e] for e in path])

def get_residual_graph(E, c, F):
    cf = {}
    Ef = [ [] for e in E]
    for u in range(len(E)):
        for v in E[u]:
            if  c[(u,v)] - F[(u,v)] != 0:
                cf[(u,v)] = c[(u,v)] - F[(u,v)]
                Ef[u].append(v)
            if  F[(u,v)] != 0:
                cf[(v,u)] = F[(u,v)]
                Ef[v].append(u)
    return cf, Ef

def augment_flow(F, c, path, new_flow):
    for u,v in path:
        if (u,v) in c: # True means its a forward edge
            F[(u,v)] += new_flow
        else: # Reverse edge
            F[(v,u)] -= new_flow


def FordFulkerson(V, E, s, t, c, F=None):
    if F is None:
        F = {}
        for u in V:
            for v in E[u]:
                F[(u,v)] = 0

    total_flow = 0
    while True:
        cf, Ef = get_residual_graph(E, c, F)
        path = find_st_path(Ef, s, t) 
        if path is None:
            break
        new_flow = get_min_capacity(cf, path)
        total_flow += new_flow
        augment_flow(F, c, path, new_flow)

    return total_flow


V = {0, 1, 2, 3}
s = 0
t = 3
E = [[1,2],[2,3], [3], []]

c = { (0,1): 3, (0,2): 2,
      (1,2): 5, (1,3): 2,
      (2,3): 3}

print (FordFulkerson(V, E, s, t, c))

#blocking path
F = { (0,1): 3, (0,2): 0,
      (1,2): 3, (1,3): 0,
      (2,3): 3}

print (FordFulkerson(V, E, s, t, c, F=F))
