for _ in range(int(input())):
    n = int(input())
    t = n // 2
    res = 0
    for i in range(t):
        res += ((i*2+1)*4+4)*(i+1)
    print(res)


