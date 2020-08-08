from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline()
    print(*sorted(map(int, stdin.readline().split()), reverse=True))
