from sys import stdin
import bisect

cur = 1
t = 2
a = []
while cur < 10 ** 7:
    a.append(cur)
    cur += t
    t += 1
for _ in range(int(stdin.readline())):
    x = int(stdin.readline())
    i = bisect.bisect_left(a, x)
    if x == a[i] - 1:
        i += 1
    print(i + 1)
