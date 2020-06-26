import math
from sys import stdin


def sieve(size):
    sie = [-1] * size
    for i in range(2, int(size**0.5)+1):
        if sie[i] != -1:
            continue
        for j in range(i*i, size, i):
            if sie[j] == -1:
                sie[j] = i
    return sie


sie = sieve(10 ** 7 + 1)
n = int(input())
a = list(map(int, stdin.readline().split()))
# a = [9840769]*500000
r1 = []
r2 = []
for i in a:
    remaining = i
    while sie[i] != -1 and remaining % sie[i] == 0:
        remaining //= sie[i]
    if sie[i] == -1 or remaining == 1:
        r1.append(-1)
        r2.append(-1)
    else:
        r1.append(sie[i])
        r2.append(remaining)

print(*r1)
print(*r2)
