from sys import stdin

for _ in range(int(stdin.readline())):
    u, v = list(map(int, stdin.readline().split()))
    print(-u*u, v*v)
