for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    s_b = ''
    for i in range(b):
        s_b += chr(97+i)
    t, s = divmod(a, b)
    s_a = s_b * t + s_b[:s]
    t, s = divmod(n, a)
    res = s_a * t + s_a[:s]
    print(res)
