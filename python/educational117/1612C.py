from sys import stdin


def cal_number(m, k):
    if m <= k:
        t = (m * (m + 1)) // 2
    elif m > k:
        t = (k * (k + 1)) // 2
        t += (k * (k - 1)) // 2
        n = 2 * k - 1 - m
        t -= n * (n + 1) // 2
    return t


for _ in range(int(stdin.readline())):
    k, x = list(map(int, stdin.readline().split()))
    l = 1
    r = 2 * k - 1
    res = r
    while l < r:
        m = l + (r - l) // 2
        t = cal_number(m, k)
        if t == x or (t > x > cal_number(m - 1, k)):
            res = m
            break
        elif t < x:
            l = m + 1
        else:
            r = m
    print(res)

