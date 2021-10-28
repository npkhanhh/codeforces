from sys import stdin
from bisect import bisect_left, bisect_right



for _ in range(int(stdin.readline())):
    n, l, r = list(map(int, stdin.readline().split()))
    a = sorted(list(map(int, stdin.readline().split())))
    res = 0
    for idx, val in enumerate(a):
        low = l - val
        high = r - val
        left = bisect_left(a, low)
        if left == n:
            continue
        right = bisect_right(a, high)
        if right == 0:
            continue
        res += right - left - (left <= idx < right)
    print(res//2)
