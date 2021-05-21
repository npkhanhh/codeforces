n, c = list(map(int, input().split()))
a = list(map(int, input().split()))

diff = 0
for i in range(1, n):
    if a[i - 1] - a[i] > diff:
        diff = a[i - 1] - a[i]

print(max(0, diff - c))
