import sys

def h_ascii_sum(key, N):
    s = 0
    for i in range(len(key)):
        s += ord(key[i])
    return s % N

def h_polynomial_rolling(key, N, p=53):
    # p a prime number roughly equal to the number of characters in the input alphabe 
    s = 0
    for i in range(len(key)):
        s += ord(key[i]) * p**i
    return s % N 

def h_python(key, N):
    return hash(key) % N

if __name__ == '__main__':
    
    for l in open(sys.argv[1]):
        if sys.argv[2] == 'ascii':
            print(h_ascii_sum(l, 1000))
        elif sys.argv[2] == 'rolling':
            print(h_polynomial_rolling(l, 1000))
        elif sys.argv[2] == 'python':
            print(h_python(l, 1000))
