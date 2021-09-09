from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    s = stdin.readline().strip()
    res = [-1, -1]
    for i in range(1, n):
        if s[i] != s[i-1]:
            res = [i, i+1]
            break
    print(*res)
