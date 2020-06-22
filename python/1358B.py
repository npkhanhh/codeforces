from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    res = 1
    for i, v in enumerate(a):
        if i + 1 >= v:
            res = i + 2
    print(res)
