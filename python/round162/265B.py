from sys import stdin

res = 0
cur = 0
for i in range(int(stdin.readline())):
    n = int(stdin.readline())
    res += abs(n-cur) + 1 + (i > 0)
    cur = n
print(res)



