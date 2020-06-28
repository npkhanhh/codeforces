from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(input())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    res = 'YES'
    has_pos = False
    has_neg = False
    for i, v in enumerate(a):
        if v < b[i] and not has_pos:
            res = 'NO'
            break
        if v > b[i] and not has_neg:
            res = 'NO'
            break
        if v == 1:
            has_pos = True
        if v == -1:
            has_neg = True
    print(res)
