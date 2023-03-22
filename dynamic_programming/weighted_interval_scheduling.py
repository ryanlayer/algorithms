from collections import namedtuple
Interval = namedtuple("Interval", "start end weight")

def get_pj(i, I):
    p_j = -1 
    for j in range(len(I)-1, -1, -1):
        if I[j].end < i.start:
            p_j = j
            break
    return p_j

def max_weight_interval_schedule(I):
    if len(I) == 0:
        return [0,[]]

    i = I[-1]

    p_j = get_pj(i, I[:-1])

    dont_take = max_weight_interval_schedule(I[:-1])
    take = max_weight_interval_schedule(I[:p_j+1])
    take[0] = take[0] + i.weight

    if take[0] > dont_take[0]:
        return [take[0], take[1] + [i]]
    else:
        return dont_take

def dp_max_weight_interval_schedule(I):
    p_j = []
    for i in range(len(I)):
        p_j.append(get_pj(I[i], I))

    M = []
    M.append(0)
    for i in range(0, len(I)):
        take = I[i].weight + (M[p_j[i]+1] if p_j[i] > -1 else 0)
        dont_take = M[-1]
        M.append(max(take, dont_take))
    return(M)

def back_track_max_weight_interval_schedule(M,I):
    p_j = []
    for i in range(len(I)):
        p_j.append(get_pj(I[i], I))

    OPT = []
    i = len(I) - 1
    while i >= 0:
        if M[i+1] == I[i].weight + (M[p_j[i]+1] if p_j[i] > -1 else 0):
            OPT.append(i)
            i = p_j[i]
        else:
            i-=1
    return (OPT)

I = [Interval(1,4,5),
     Interval(2,5,10),
     Interval(3,7,2),
     Interval(6,9,6),
     Interval(8,10,3)]

I = sorted(I, key=lambda i: i.end)
print(max_weight_interval_schedule(I))
M = dp_max_weight_interval_schedule(I)
OPT = back_track_max_weight_interval_schedule(M,I)
print(M[-1], OPT)
