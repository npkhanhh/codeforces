from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = sorted(map(int, stdin.readline().split()), reverse=True)
    print(sum(a[:k+1]))

