from sys import stdin

for _ in range(int(stdin.readline())):
    s = stdin.readline().strip()
    d = {}
    for i in s:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1
    res = 0
    count = 0
    for c, val in d.items():
        if val > 1:
            res += 1
        else:
            count += 1
    res += count // 2
    print(res)
