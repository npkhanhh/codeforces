from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    s = stdin.readline().strip()
    if s == s[::-1] or k < 1:
        print(1)
    else:
        print(2)
