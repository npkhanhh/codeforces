from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    if a[0] > 0:
        print(1)
    else:
        min_diff = pow(10, 9)
        res = 1
        min_pos = -1
        for i in range(1, n):
            if a[i] <= 0:
                min_diff = min(min_diff, a[i] - a[i-1])
                res += 1
            else:
                min_pos = a[i]
                break
        res += 1 if min_diff >= min_pos > 0 else 0
        print(res)

