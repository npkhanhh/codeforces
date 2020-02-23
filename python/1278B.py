import math

t = int(input())

for i in range(t):
    a, b = list(map(int, input().split()))
    if a == b:
        print(0)
    else:
        c = abs(a-b)
        n = math.ceil((math.sqrt(8*c + 1) - 1)/2)
        while ((n*(n+1)/2) + c) % 2 == 1:
            n += 1
        print(int(n))