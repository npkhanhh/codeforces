from sys import stdin

n = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().split()))
b = sorted(a)
prefix_a = [0]*(n+1)
prefix_b = [0]*(n+1)
prefix_a[1] = a[0]
prefix_b[1] = b[0]
for i in range(2, n+1):
    prefix_a[i] = a[i-1] + prefix_a[i-1]
    prefix_b[i] = b[i-1] + prefix_b[i-1]
m = int(stdin.readline().rstrip())
for _ in range(m):
    m, l, r = list(map(int, stdin.readline().split()))
    if m == 1:
        print(prefix_a[r] - prefix_a[l-1])
    else:
        print(prefix_b[r] - prefix_b[l-1])




