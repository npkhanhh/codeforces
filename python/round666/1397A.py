from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    d = {}
    for _ in range(n):
        s = stdin.readline().rstrip()
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
    res = 'YES'
    for v in d.values():
        if v % n != 0:
            res = 'NO'
            break
    print(res)
