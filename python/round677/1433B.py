from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    while a[0] == 0:
        del a[0]
    while a[-1] == 0:
        del a[-1]
    print(a.count(0))
