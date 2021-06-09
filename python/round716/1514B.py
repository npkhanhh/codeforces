from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    print(pow(n, k, 10**9+7))
