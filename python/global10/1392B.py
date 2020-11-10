from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    for _ in range(2 - (k % 2)):
        d = max(a)
        a = list(map(lambda x: d - x, a))
    print(*a)
