import math


def solve(l, r):
    res = [-1]
    for i in range(l, r - 1):
        for j in range(i + 1, r):
            for k in range(j + 1, r + 1):
                if math.gcd(i, j) == 1 and math.gcd(j, k) == 1 and math.gcd(i, k) != 1:
                    return i, j, k
    return res


l, r = list(map(int, input().split()))

print(*solve(l, r))
