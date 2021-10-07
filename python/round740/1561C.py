from sys import stdin

for _ in range(int(stdin.readline())):
    a = []
    for _ in range(int(stdin.readline())):
        b = list(map(int, stdin.readline().split()))
        cur = 0
        for idx, val in enumerate(b[1:]):
            cur = max(cur, val - idx + 1)
        a.append((cur, b[0]))
    a = sorted(a)
    res = 0
    total_mons = 0
    for min_pow, length in a:
        res = max(min_pow - total_mons, res)
        total_mons += length
    print(res)



# 8
# 6 22 11 16 12 12 16
# 1 6
# 4 19 1 15 22
# 10 24 11 6 7 11 15 20 22 2 6
# 10 5 3 6 1 12 24 20 4 1 23
# 6 10 3 24 1 24 8
# 1 19
# 7 8 23 4 5 7 20 18
