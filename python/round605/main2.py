import numpy as np

def distance(data):
    return np.sum(np.abs(data[i]-data[i+1]) for i in range(2)) + np.abs(data[2]-data[0])

def func(data, i):
    if i == 2:
        #stay
        a = distance(data)
        #left
        data[2] = data[2] - 1
        b = distance(data)
        data[2] = data[2] + 1
        #right
        data[2] = data[2] + 1
        c = distance(data)
        data[2] = data[2] - 1
        return min([a,b,c])

    #stay
    data[i] = data[i] + 0
    s = func(data, i+1)
    #left
    data[i] = data[i] - 1
    l = func(data, i+1)
    data[i] = data[i] + 1
    #right
    data[i] = data[i] + 1
    r = func(data, i+1)
    data[i] = data[i] - 1
    return np.min([s, l, r])

n = int(input())
for t in range(n):
    data=list(map(int, input().strip().split()))
    print(func(data, 0))
