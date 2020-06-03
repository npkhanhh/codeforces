from sys import stdin
I = stdin.readline

for _ in range(int(I())):
    n = int(I())
    a = sorted(map(int, I().split()))
    has_diff_1 = False
    even = odd = 0
    for i, v in enumerate(a):
        if v % 2 == 0:
            even += 1
        else:
            odd += 1
        if i > 0 and abs(a[i] - a[i-1]) == 1:
            has_diff_1 = True
    if odd % 2 == even % 2:
        if even % 2 == 1 and not has_diff_1:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')
