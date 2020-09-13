from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline()
    print(*list(map(int, stdin.readline().split()))[::-1])
