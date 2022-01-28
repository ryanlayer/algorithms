def BFS_dist(V):
    state = ['new']*len(V)
    Q = []
    dist = [None]*len(V)
    dist[0] = -1

    pred = [None]*len(V)
    pred[0] = 0

    Q.append(0)
    while len(Q) != 0:
        x = Q.pop(0)
        print('-', x)
        dist[x] = dist[ pred[x] ] + 1
        if state[x] == 'new':
            state[x] = 'old'
            for y in V[x]:
                if pred[y] == None:
                    pred[y] = x
                print('+', y)
                Q.append(y)
    print(dist)

V = [[1,2,3],[4],[5],[6],[5],[7],[5],[]]
DFS(V)
