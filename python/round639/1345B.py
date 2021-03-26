from sys import stdin
import bisect


def find_le(a, x):
    i = bisect.bisect_right(a, x)
    if i:
        return i - 1, a[i - 1]
    raise ValueError


a = [0]
i = 1
while True:
    t = a[-1]
    t += 3 * i - 1
    a.append(t)
    if t >= 10 ** 9:
        break
    i += 1
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    res = 0
    while n > 0:
        i, t = find_le(a, n)
        if i == 0:
            break
        res += 1
        n -= t
    print(res)
