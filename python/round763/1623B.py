from sys import stdin

for _ in range(int(stdin.readline())):
    a = []
    n = int(stdin.readline())
    for _ in range(n):
        a.append(list(map(int, stdin.readline().split())))
    a = sorted(a, key=lambda item: item[1]-item[0])
    m = [False]*(n+1)
    for r in a:
        for i in range(r[0], r[1]+1):
            if not m[i]:
                m[i] = True
                print(*r, i)
                break
