from sys import stdin

for _ in range(int(stdin.readline())):
    a, b, c = sorted(list(map(int, stdin.readline().split())))
    res = 'NO'
    if a == b and c % 2 == 0:
        res = 'YES'
    elif b == c and a % 2 == 0:
        res = 'YES'
    elif c == a + b:
        res = 'YES'
    print(res)
