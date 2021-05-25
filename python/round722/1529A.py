from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    m = a[0]
    count = 1
    for i in a[1:]:
        if i < m:
            m = i
            count = 1
        elif i == m:
            count += 1
    print(n-count)
