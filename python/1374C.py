for _ in range(int(input())):
    input()
    s = input()
    res = 0
    c = 0
    for v in s:
        if v == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            res += 1
            c += 1

    print(res)
