from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s1 = stdin.readline().strip()
    s2 = stdin.readline().strip()
    res = []
    for i in range(n):
        if s1[i] != s2[i]:
            res.append(i + 1)
            res.append(1)
            res.append(i + 1)
    print(len(res), *res)
