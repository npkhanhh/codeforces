from sys import stdin

import math

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    count_even = 0
    odds = []
    for i in a:
        if i % 2 == 0:
            count_even += 1
        else:
            odds.append(i)
    res = (count_even * (count_even - 1)) // 2
    t = count_even * len(odds)
    res += t
    for i in range(len(odds) - 1):
        for j in range(i + 1, len(odds)):
            if math.gcd(odds[i], odds[j]) > 1:
                res += 1
    print(res)
