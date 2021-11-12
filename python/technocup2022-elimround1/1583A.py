from sys import stdin
import math
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    s = sum(a)
    is_composite = False
    for i in range(2, int(math.ceil(math.sqrt(s)))+1):
        if s % i == 0:
            is_composite = True
            break
    if is_composite:
        print(n)
        print(*list(range(1, n+1)))
    else:
        removed = -1
        for i in range(n):
            if a[i] % 2 == 1:
                removed = i
                break
        res = list(range(1, removed+1)) + list(range(removed+2, n+1))
        print(n-1)
        print(*res)


