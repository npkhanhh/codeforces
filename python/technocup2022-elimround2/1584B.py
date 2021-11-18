from sys import stdin


def cal(d1, d2):
    if d1*d2 == 2:
        return 1
    if d1 == 2 and d2 == 2:
        return 2
    d1, d2 = sorted([d1, d2])
    if d1 > 1:
        a, b = divmod(d1, 3)
        t = d2 * a
        t += cal(d2, b)
    return t


for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    res = cal(m,n)
    print(res)
