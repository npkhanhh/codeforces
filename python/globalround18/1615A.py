from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sum(list(map(int, stdin.readline().split())))
    print(1 if a % n != 0 else 0)
