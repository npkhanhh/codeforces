from sys import stdin

n, q = list(map(int, stdin.readline().split()))
a = list(map(lambda x: ord(x) - 96, list(stdin.readline())))
prefix_sum = [0] * n
prefix_sum[0] = a[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + a[i]
for _ in range(q):
    l, r = list(map(int, stdin.readline().split()))
    if l == 1:
        print(prefix_sum[r - 1])
    else:
        print(prefix_sum[r - 1] - prefix_sum[l - 2])
