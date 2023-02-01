def BFS_dist(E):
    state = ['new']*len(E)
    Q = []
    dist = [None]*len(E)
    dist[0] = -1

    pred = [None]*len(E)
    pred[0] = 0

    Q.append(0)
    while len(Q) != 0:
        x = Q.pop(0)
        dist[x] = dist[ pred[x] ] + 1
        if state[x] == 'new':
            state[x] = 'old'
            for y in E[x]:
                if pred[y] == None:
                    pred[y] = x
                Q.append(y)
    return dist

E = [[1,2,3],[4],[5],[6],[5],[7],[5],[]]
print(BFS_dist(E))
