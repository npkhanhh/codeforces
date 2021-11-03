from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    d = {}
    for idx, val in enumerate(s):
        d[val] = idx
    ss = stdin.readline().strip()
    res = 0
    for i in range(1, len(ss)):
        res += abs(d[ss[i]] - d[ss[i-1]])
    print(res)
