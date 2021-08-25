from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    cur = 0
    swapped = True
    while True:
        cur += 1
        swapped = False
        for i in range(1 - cur % 2, n - (1 + cur % 2), 2):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        is_sorted = True
        for i in range(1,n):
            if a[i] < a[i-1]:
                is_sorted = False
        if not swapped and is_sorted:
            break
    print(cur - 1)
