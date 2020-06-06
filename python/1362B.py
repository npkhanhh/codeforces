from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    if n % 2 == 1:
        print(-1)
        continue
    s = set()
    for i in range(n):
        t = set()
        for j in range(n):
            if i != j:
                t.add(a[i] ^ a[j])
        if i == 0:
            s = t
        else:
            s = s & t
    if len(s) == 0:
        print(-1)
    else:
        print(min(s))



