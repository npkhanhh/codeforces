for _ in range(int(input())):
    res = 0
    t = 0
    start = False
    for c in input():
        if c == '1':
            start = True
        if start and c == '0':
            t += 1
        if start and c == '1':
            res += t
            t = 0
    print(res)
