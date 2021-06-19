from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    tot = sum(a)
    if tot == n:
        print(0)
    elif tot > n:
        print(tot-n)
    else:
        print(1)
