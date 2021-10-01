from sys import stdin
import bisect

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = []
    for i in range(1, n):
        if a[i] < a[i-1]:
            idx = bisect.bisect(a[:i], a[i])
            res.append([idx+1, i+1, i-idx])
            a = list(sorted(a[:i+1])) + a[i+1:]
    print(len(res))
    for i in res:
        print(*i)


