from sys import stdin

a = []
t = 1
while t <= 10**18:
    a.append(str(t))
    t *= 2


for _ in range(int(stdin.readline())):
    n = stdin.readline().strip()
    res = 100
    for s in a:
        i = j = to_del = 0
        while i < len(n) and j < len(s):
            if n[i] == s[j]:
                j += 1
            else:
                to_del += 1
            i += 1
        cur_res = len(n) - i + to_del + len(s) - j
        res = min(res, cur_res)
        if res == 0:
            break
    print(res)

