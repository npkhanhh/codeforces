for _ in range(int(input())):
    s = input()
    l = len(s)
    res = []
    for i in range(l-1, -1, -1):
        if s[i] != '0':
            res.append(s[i] + '0' * (l - 1 - i))
    print(len(res))
    print(*res)
