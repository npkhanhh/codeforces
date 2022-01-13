from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c = list(map(int, stdin.readline().split()))
    arr = sorted([a, b, c])
    d = b - a
    t = b + d
    if t > 0 and t % c == 0:
        print('YES')
        continue
    d = c - b
    t = b - d
    if t > 0 and t % a == 0:
        print('YES')
        continue
    d = c - a
    if d % 2 == 0:
        d //= 2
        t = a + d
        if t > 0 and t % b == 0:
            print('YES')
            continue
    print('NO')

