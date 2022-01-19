from heapq import heappush, heappop

msg = 'MISSISSIPPIS'

def get_freqs(data):
    freq = {}
    for d in data:
        if d not in freq:
            freq[d] = 0
        freq[d] = freq[d] + 1/len(data)
    return freq

freqs = get_freqs(msg)
F = []

# add all symbols and their freq to a priority queue
for s in freqs:
    heappush(F, (freqs[s], s))

def huffman(F):
    if len(F) == 2:
        a = heappop(F)
        b = heappop(F)
        
        #make a tree with just a and b
        #use an adjacency matrix
        T = {}
        T['root'] = [a[1],b[1]]
        T[a[1]] = None
        T[b[1]] = None
        
        return T
    else:
        a = heappop(F)
        b = heappop(F)
        heappush(F,(a[0] + b[0], a[1] + b[1]))
        T = huffman(F)
    
        # expand ab with a b
        T[a[1]+b[1]] = [a[1],b[1]]
        T[a[1]] = None
        T[b[1]] = None
        
        return T

T = huffman(F)

# user DFS to get the bits for each symbol
def get_code(V):
    state = {}
    Q = []
    
    code = {}

    Q.append(['root',''])
    while len(Q) != 0:
        x,bits = Q.pop(-1)
        
        if V[x] != None:
            left = bits + '0'
            Q.append([V[x][0],left])
            right = bits + '1'
            Q.append([V[x][1],right])
        else:
            code[x] = bits
    
    return code

code = get_code(T)

print(code)

bits = ''
for m in msg:
    bits += code[m]
print(bits)

def decode(T, bits):
    msg = ''
    
    curr_node = 'root'
    
    for bit in bits:
        if T[T[curr_node][int(bit)]] is None:
            msg += T[curr_node][int(bit)]
            curr_node = 'root'
        else:
            curr_node = T[curr_node][int(bit)]
    return msg

print(decode(T, bits))
