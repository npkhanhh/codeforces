from sys import stdin


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    res = False
    total = 0
    for i in a:
        if i < 2048:
            total += i
        elif i == 2048:
            res = True
            break
    if total >= 2048:
        res = True

    print('YES' if res else 'NO')
