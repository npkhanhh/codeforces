for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    res = n
    for _ in range(k-1):
        b = 0
        s = 10
        for i in str(res):
            if i == '0':
                s = 0
                break
            if int(i) > b:
                b = int(i)
            if int(i) < s:
                s = int(i)

        if s == 0:
            break
        res += b*s
    print(res)

