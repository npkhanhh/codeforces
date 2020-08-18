n = int(input())
if n == 0:
    print(0)
else:
    t = 1
    for _ in range(n):
        t *= 8
        t = t % 10
    print(t)
