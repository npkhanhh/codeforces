for _ in range(int(input())):
    a, b, c = (input(), input(), input())
    res = 'YES'
    for i in range(len(a)):
        if b[i] != c[i] and a[i] != c[i]:
            res = 'NO'
            break
    print(res)