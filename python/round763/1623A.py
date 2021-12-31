from sys import stdin

for _ in range(int(stdin.readline())):
    n, m, rb, cb, rd, cd = list(map(int, stdin.readline().split()))
    res_r = rd - rb
    if res_r < 0:
        res_r = 2*n - rb - rd
    res_c = cd - cb
    if res_c < 0:
        res_c = 2*m - cb - cd
    print(min(res_r, res_c))
