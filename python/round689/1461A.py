from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    print(('abc' * (n // 3 + 1))[:n])
