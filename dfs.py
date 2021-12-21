def DFS(V):
    state = ['new']*len(V)
    Q = []

    Q.append(0)
    while len(Q) != 0:
        x = Q.pop(-1)
        print('-',x)
        if state[x] == 'new':
            state[x] = 'old'
            for y in V[x]:
                print('+',y)
                Q.append(y)

V = [[1,2,3],[4],[5],[6],[5],[7],[5],[]]   
DFS(V)
