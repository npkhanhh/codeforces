from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    s = set()
    for i in range(n-1):
        for j in range(i+1, n):
            s.add(a[j]-a[i])
    print(len(s))
