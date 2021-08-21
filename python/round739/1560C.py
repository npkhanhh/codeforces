from sys import stdin
import bisect

a = []
for i in range(1, 100001):
    a.append(i * i)


def find_lt(a, x):
    idx = bisect.bisect_left(a, x)
    if a[idx] == x:
        return idx+1, a[idx]
    return idx+1, a[idx - 1]


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    idx, val = find_lt(a, n)
    size = idx
    if n == val:
        print(size, 1)
    elif n - val < size:
        print(n-val, size)
    elif n - val > size:
        print(size, size - ((n-val) % size))
    else:
        print(size, size)


