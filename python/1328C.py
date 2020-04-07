for _ in range(int(input())):
    n = int(input())
    s = input()
    res1 = res2 = '1'
    swapped = False
    for i in s[1:]:
        if i == '2':
            if swapped:
                res1 += '2'
                res2 += '0'
            else:
                res1 += '1'
                res2 += '1'
        elif i == '1':
            res1 += '1'
            res2 += '0'
            if not swapped:
                res1, res2 = res2, res1
                swapped = True
        else:
            res1 += '0'
            res2 += '0'
    print(res1)
    print(res2)