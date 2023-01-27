def DFS(V):
    state = ['new']*len(V)
    Q = []
    Q.append(0)
    while len(Q) != 0:
        x = Q.pop(-1)
        if state[x] == 'new':
            state[x] = 'old'
            for y in V[x]:
                Q.append(y)

V = [[1,2,3],[4],[5],[6],[5],[7],[5],[]]   
DFS(V)

tree = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[],[],[],[],[],[],[],[]]
DFS(tree)
