import heapq

def Dijkstra(E,s,w):
    Q = []

    dist = [float('inf')] * len(E)
    dist[s] = 0

    pred = [None] * len(E)
    
    heapq.heappush(Q,(0,s))
    while len(Q) > 0:
        d,x = heapq.heappop(Q)
        for y in E[x]:
            if dist[y] > dist[x] + w[(x,y)]: # (x,y) is tense
                dist[y] = dist[x] + w[(x,y)] # relax
                pred[y] = x
                heapq.heappush(Q,(dist[y],y))
        print(dist,pred,Q)

    return dist, pred
    
E = [[1,2],[2,3],[1,4],[1,4],[2,3]]

w = { (0,1) : 1, (1,0) : 1,
      (0,2) : 3, (2,0) : 3,
      (1,2) : 1, (2,1) : 1,
      (1,3) : 3, (3,1) : 3,
      (2,4) : 7, (4,2) : 7,
      (3,4) : 2, (4,3) : 2}

dist, pred = Dijkstra(E,0,w)
