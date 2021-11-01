from sys import stdin
import math

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    cur = 1
    res = 0
    for i in range(1, k+1):
        if cur >= n or cur >= k:
            break
        cur *= 2
        res += 1
    if cur < n:
        a, b = divmod(n-cur, k)
        res += a + (b>0)
    print(res)




