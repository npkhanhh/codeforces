from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    s = sum(a) % n
    print(s*(n-s))
