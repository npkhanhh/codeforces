n = int(input())
a = list(map(int, input().split()))
i = -1
while n > 0:
    i += 1
    if i == 7:
        i = 0
    n -= a[i]

print(i + 1)
