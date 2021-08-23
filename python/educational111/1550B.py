from sys import stdin

for _ in range(int(stdin.readline())):
    n, a, b = list(map(int, stdin.readline().split()))
    s = stdin.readline().strip()
    if b >= 0:
        print((a+b)*n)
    else:
        cur = 1
        for i in range(1, n):
            if s[i] != s[i-1]:
                cur += 1
        print(a*n + b*(cur//2 + 1))


