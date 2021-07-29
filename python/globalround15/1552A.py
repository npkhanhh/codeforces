from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    a = sorted(s)
    res = 0
    for i in range(n):
        if a[i] != s[i]:
            res+=1
    print(res)
