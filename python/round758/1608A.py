from sys import stdin

for _ in range(int(stdin.readline())):
    print(*list(range(2, int(stdin.readline())+2)))
