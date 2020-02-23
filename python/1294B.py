for _ in range(int(input())):
    a = []
    for _ in range(int(input())):
        a.append(tuple(map(int, input().split())))
    a = sorted(a)
    i = j = 0
    has_res = True
    res = ''
    for ele in a:
        if ele[0] < i or ele[1] < j:
            has_res = False
            break
        res += 'R' * (ele[0] - i)
        i = ele[0]
        res += 'U' * (ele[1] - j)
        j = ele[1]
    if has_res:
        print('YES')
        print(res)
    else:
        print('NO')


