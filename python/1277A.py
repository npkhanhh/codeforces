nn = int(input())

for i in range(nn):
    n = int(input())
    t = 0
    res = 0
    loop = True
    while loop:
        t *= 10
        t += 1
        for a in range(1, 10):
            if a * t > n:
                loop = False
                break
            else:
                res += 1
    print(res)
