n = int(input())
s = input()

a = [-1] * (n + 1)
a[0] = 0
count = [0, 0]
res = 0
for idx, c in enumerate(s):
    count[int(c)] += 1
    diff = count[0] - count[1]
    if a[diff] == -1:
        a[diff] = idx + 1
    elif idx + 1 - a[diff] > res:
        res = idx + 1 - a[diff]

print(res)
