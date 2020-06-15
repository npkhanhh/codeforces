from sys import stdin

for _ in range(int(stdin.readline())):
    n, x, m = list(map(int, stdin.readline().split()))
    res_l = res_r = x
    for _ in range(m):
        l, r = list(map(int, stdin.readline().split()))
        if l <= res_l <= r or l <= res_r <= r:
            if l < res_l:
                res_l = l
            if r > res_r:
                res_r = r
    print(res_r - res_l + 1)
