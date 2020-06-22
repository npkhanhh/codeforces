from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = list(map(int, stdin.readline().split()))
    s = input()
    a = []
    count = 0
    for idx, val in enumerate(s):
        if val == '1':
            a.append(idx)
    if len(a) == 0 or a[0] > k:
        a = [0] + a
        count += 1
    if a[-1] + k < n-1:
        a.append(n-1)
        count += 1
    for i in range(len(a)-1):
        count += max((a[i+1] - k - a[i] - 1) // (k + 1), 0)
    print(count)
