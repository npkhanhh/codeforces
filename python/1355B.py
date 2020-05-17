from sys import stdin

for _ in range(int(input())):
    n = int(stdin.readline())
    a = sorted([int(x) for x in stdin.readline().strip().split(" ")])
    res = 0
    need = 0
    has = 0
    for idx, val in enumerate(a):
        if val > need:
            need = val
        has += 1
        if has == need:
            res += 1
            has = 0
            need = 0
    print(res)
