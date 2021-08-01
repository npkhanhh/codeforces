from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    res = -1
    for i in range(k):
        fall = True
        for j in range(1, n):
            if a[j] > a[j - 1]:
                a[j - 1] += 1
                res = j
                fall = False
                break
        if fall:
            res = -1
            break

    print(res)
