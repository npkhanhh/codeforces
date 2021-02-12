from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    has_0 = False
    has_other = False
    start = 0
    while start < n and a[start] - start - 1 == 0:
        start += 1
    end = n-1
    while end > -1 and a[end] - end - 1 == 0:
        end -= 1
    if start == n:
        print(0)
    else:
        for i, v in enumerate(a[start:end+1], start=start):
            if abs(v - i - 1) == 0:
                has_0 = True
            else:
                has_other = True
        if has_0 and has_other:
            print(2)
        elif has_0:
            print(0)
        else:
            print(1)
