from sys import stdin

for _ in range(int(stdin.readline())):
    l, r = list(map(int, stdin.readline().split()))
    t = r // 2 - (1 - r % 2)
    if l > r / 2:
        print(r % l)
    else:
        print(t)
