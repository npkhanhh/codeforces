import math
from sys import stdin
import bisect

a = []
c = []
m = 10**9
for i in range(1, 1001):
    cur = i ** 6
    if cur <= m:
        a.append(cur)
    c.append(i**3)
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    sq = int(math.sqrt(n))
    cb = bisect.bisect(c, n)
    idx = bisect.bisect(a, n)
    print(sq+cb -idx)

