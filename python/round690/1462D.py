import math
from sys import stdin

def get_divisors(n, m):
    res = []
    for k in range(1, int(math.sqrt(n)) + 1):
        if n % k == 0:
            if k >= m:
                res.append(k)
            if n // k >= m:
                res.append(n // k)
    return res


for z in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    s = sum(a)
    m = max(a)
    divisors = sorted(get_divisors(s, m))
    res = -1
    for divisor in divisors:
        cur = 0
        group = 0
        for idx, val in enumerate(a):
            cur += val
            if cur == divisor:
                if idx < n - 1:
                    cur = 0
                group += 1
            elif cur > divisor:
                break
        if cur == divisor:
            res = n - group
            break

    print(res)


