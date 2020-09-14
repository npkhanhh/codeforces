from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    res = 'YES'
    diff = -1
    end_diff = False
    for i in range(n):
        if a[i] > b[i]:
            res = 'NO'
            break
        if b[i] > a[i]:
            if diff == -1:
                diff = b[i] - a[i]
            elif end_diff or b[i] - a[i] != diff:
                res = 'NO'
                break
        if diff > 0 and b[i] == a[i]:
            end_diff = True
    print(res)
