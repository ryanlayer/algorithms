def DFS(E):
    state = ['new']*len(E)
    Q = []
    Q.append(0)
    while len(Q) != 0:
        x = Q.pop(-1)
        if state[x] == 'new':
            state[x] = 'old'
            for y in E[x]:
                Q.append(y)

E = [[1,2,3],[4],[5],[6],[5],[7],[5],[]]   
DFS(E)
