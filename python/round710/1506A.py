from sys import stdin

for _ in range(int(stdin.readline())):
    n, m, x = list(map(int, stdin.readline().split()))
    c, r = divmod(x-1, n)
    res = r*m + c + 1
    print(res)
