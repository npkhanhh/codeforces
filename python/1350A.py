from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    sd = n
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            sd = i
            break
    n += sd
    k -= 1
    n += 2*k
    print(n)


