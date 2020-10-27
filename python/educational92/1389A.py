from sys import stdin

for _ in range(int(stdin.readline())):
    l, r = list(map(int, stdin.readline().split()))
    t = r // l
    if t == 1:
        print(-1, -1)
    else:
        print(l, l * t)
