from sys import stdin

for _ in range(int(stdin.readline())):
    n, m, x, y = list(map(int, stdin.readline().split()))
    two_tile = y if y < 2 * x else 2 * x
    res = 0
    for _ in range(n):
        s = input() + '*'
        con = 0
        for i in s:
            if i == '.':
                con += 1
            else:
                a, b = divmod(con, 2)
                res += two_tile * a + x * b
                con = 0
    print(res)
