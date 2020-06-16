from sys import stdin

for _ in range(int(input())):
    n = int(input())
    need_one_col = [False]*n
    res = True
    for _ in range(n):
        s = input()
        if res:
            need_one = False
            for i in range(n):
                if need_one_col[i]:
                    if s[i] == '1':
                        need_one = True
                        need_one_col[i] = False
                    else:
                        res = False
                        break
                elif need_one and s[i] == '0':
                    need_one_col[i-1] = True
                    need_one = False
                elif s[i] == '1' and i < n - 1:
                    need_one = True
    print(['No', 'Yes'][res])


