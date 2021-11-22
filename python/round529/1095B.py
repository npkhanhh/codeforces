n = int(input())
a = sorted(map(int, input().split()))
if n == 2:
    print(0)
else:
    print(min(a[-1]-a[1], a[-2]-a[0]))
