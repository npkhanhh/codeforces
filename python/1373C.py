for _ in range(int(input())):
    s = input()
    cur = 0
    res = len(s)
    t = 0
    for i, v in enumerate(s):
        if v == '+':
            cur += 1
        else:
            cur -= 1
        if cur + t < 0:
            res += i+1
            t += 1
    print(res)
