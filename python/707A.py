n, _ = list(map(int, input().split()))
res = '#Black&White'
for _ in range(n):
    s = input()
    if 'C' in s or 'M' in s or 'Y' in s:
        res = '#Color'
print(res)
