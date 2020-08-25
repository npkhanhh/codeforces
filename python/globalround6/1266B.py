t = int(input())
a = list(map(int, input().split()))

for v in a:
    x, y = divmod(v, 14)
    if x >= 1 and 1 <= y <= 6:
        print('YES')
    else:
        print('NO')
