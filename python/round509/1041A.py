n = int(input())
a = sorted(map(int, input().split()))

print(a[-1] - a[0] - n + 1)
