n = int(input())
a = [[1]*n for i in range(n)]
for i in range(1, n):
    for j in range(1, n):
        a[i][j] = a[i-1][j]+a[i][j-1]
print(a[-1][-1])

# n = int(input())
# r = 1
# for i in range(1, n):
#     r = r * (n + i - 1) // i
# print(r)