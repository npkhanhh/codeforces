for _ in range(int(input())):
    input()
    s = input().split()
    d = {}
    res = 'NO'
    for i, v in enumerate(s):
        if v in d:
            if i - d[v] > 1:
                res = 'YES'
                break
        else:
            d[v] = i
    print(res)
