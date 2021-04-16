from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    d = {}
    for idx, val in enumerate(a):
        if val not in d:
            d[val] = 1
        else:
            d[val] += 1
    for idx, val in enumerate(a):
        if d[val] == 1:
            print(idx+1)
            break
