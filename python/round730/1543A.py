from sys import stdin

for _ in range(int(stdin.readline())):
    a, b = list(map(int, stdin.readline().split()))
    t = abs(a - b)
    if t == 0:
        print(0, 0)
    else:
        print(t, min(a % t, t - a % t))
