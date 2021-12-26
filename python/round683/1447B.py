from sys import stdin

for _ in range(int(stdin.readline())):
    n, m = list(map(int, stdin.readline().split()))
    has_0 = False
    count_neg = 0
    tot = 0
    m = 101
    for _ in range(n):
        a = list(map(int, stdin.readline().split()))
        for j in a:
            if j == 0:
                has_0 = True
            if j < 0:
                count_neg += 1
            tot += abs(j)
            if abs(j) < m:
                m = abs(j)
    if has_0 or count_neg % 2 == 0:
        print(tot)
    else:
        print(tot - 2*m)
