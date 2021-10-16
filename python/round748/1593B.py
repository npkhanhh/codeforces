from sys import stdin

for _ in range(int(stdin.readline())):
    n = stdin.readline().strip()
    res = 0
    has_5 = False
    has_0 = False
    for i in range(len(n) - 1, -1, -1):
        if has_5 and (n[i] == '7' or n[i] == '2'):
            if has_0:
                res += 1
            break
        if has_0 and (n[i] == '0' or n[i] == '5'):
            if has_5:
                res += 1
            break
        if n[i] == '5':
            if not has_5:
                has_5 = True
            else:
                res += 1
        elif n[i] == '0':
            if not has_0:
                has_0 = True
            else:
                res += 1
        else:
            res += 1
    print(res)
