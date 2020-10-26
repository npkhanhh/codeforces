n = int(input())
a = sorted(map(int, input().split()))

if a[0] == a[-1]:
    print(0, n*(n-1)//2)
else:
    b, c = 1, 1
    for i in range(1, n):
        if a[i] == a[0]:
            b += 1
        if a[-(i+1)] == a[-1]:
            c += 1
    print(a[-1] - a[0], b*c)



