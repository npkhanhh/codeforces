from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    d2 = -1
    for i in range(1, n):
        if a[i] != a[0]:
            d2 = i + 1
            break
    if d2 == -1:
        print('NO')
    else:
        print('YES')
        for idx, val in enumerate(a[1:], start=1):
            if val == a[0]:
                print(idx+1, d2)
            else:
                print(idx+1, 1)
