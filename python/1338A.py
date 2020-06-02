from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    cur_max = a[0]
    max_diff = 0
    t = 0
    b = []
    c = []
    s = 0
    for i in range(n):
        if a[i] > cur_max:
            cur_max = a[i]
        elif cur_max - a[i] > max_diff:
            max_diff = cur_max - a[i]
    while s < max_diff:
        s += 2**t
        t += 1
    print(t)
