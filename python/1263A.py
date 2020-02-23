
n = int(input())
for _ in range(n):
    a, b, c = sorted(list(map(int, input().split())))

    if a + b >= c:
        print(int((a+b+c)/2))
    else:
        print(a+b)
