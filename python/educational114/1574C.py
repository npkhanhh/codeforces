from sys import stdin
import bisect

n = int(stdin.readline())
a = sorted(map(int, stdin.readline().split()))
s = sum(a)
for _ in range(int(stdin.readline())):
    x, y = list(map(int, stdin.readline().split()))
    i = bisect.bisect(a, x)
    if i == n:
        print(max(0, y - (s - a[i-1])) + max(0, x-a[i-1]))
    elif a[i] == x or i == 0:
        print(max(0, y - (s - a[i])))
    elif i > 0:
        res1 = max(0, y - (s - a[i]))
        res2 = max(0, y - (s - a[i - 1])) + x-a[i-1]
        print(min(res1, res2))
