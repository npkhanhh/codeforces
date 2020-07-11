a = sum(map(int, input().split()))
if a >= 5 and a % 5 == 0:
    print(a // 5)
else:
    print(-1)
