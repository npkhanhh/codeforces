from sys import stdin

for _ in range(int(stdin.readline())):
    n, c = stdin.readline().split()
    n = int(n)
    s = stdin.readline().strip()
    res = []
    diff = []
    for idx, val in enumerate(s):
        if val != c:
            diff.append(idx+1)
    if len(diff) == 0:
        print(0)
    else:
        b = n-1
        while b>=0 and s[b] != c:
            b-=1
        if (b + 1)*2 <= n:
            print(2)
            print(n-1, n)
        else:
            print(1)
            print(b+1)
