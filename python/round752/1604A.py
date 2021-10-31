from sys import stdin

for _ in range(int(stdin.readline())):
    stdin.readline()
    a = list(map(int, stdin.readline().split()))
    res = 0
    for idx, val in enumerate(a):
        if val > idx + 1 + res:
            res += val - idx - 1 - res
    print(res)
