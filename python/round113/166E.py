n = int(input())
modulo = 10 ** 9 + 7
if n < 2:
    print(0)
else:
    a = 1
    t = -1
    for i in range(n - 2):
        a = (a * 3 + t) % modulo
        t *= -1
    print((a * 3) % modulo)
