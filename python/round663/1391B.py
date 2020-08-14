from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    res = 0
    for _ in range(n - 1):
        s = input()
        if s[-1] == 'R':
            res += 1
    s = input()
    for c in s[:-1]:
        if c == 'D':
            res += 1
    print(res)
