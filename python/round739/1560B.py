from sys import stdin

for i in range(int(stdin.readline())):
    a, b, c = list(map(int, stdin.readline().split()))
    a, b = sorted([a, b])
    diff = b - a
    if a - diff >= 1 or c - diff >= b or c + diff <= a or c > 2*diff:
        print(-1)
        continue
    if c - diff >= 1:
        print(c-diff)
    elif c + diff <= 2 * diff:
        print(c+diff)
    else:
        print(-1)

