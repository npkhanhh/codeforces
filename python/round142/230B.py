import math


def sieve(size):
    res = [1] * size
    sie = [-1] * size
    for i in range(2, int(size ** 0.5) + 1):
        if sie[i] != -1:
            continue
        for j in range(i * i, size, i):
            sie[j] = i
            res[j] += 1
    return sie


s = sieve(10 ** 6 + 1)

input()
a = list(map(int, input().split()))
for i in a:
    t = math.sqrt(i)
    if i > 1 and t.is_integer() and s[int(t)] == -1:
        print('YES')
    else:
        print('NO')
