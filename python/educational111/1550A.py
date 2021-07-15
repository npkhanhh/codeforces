from sys import stdin

for _ in range(int(stdin.readline())):
    t = int(stdin.readline())
    cur = 1
    idx = 3
    res = 1
    while cur < t:
        cur += idx
        idx += 2
        res += 1
    print(res)
