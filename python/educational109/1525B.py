from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    is_sorted = True
    for i in range(1, n):
        if a[i] < a[i-1]:
            is_sorted = False
            break
    if is_sorted:
        print(0)
    else:
        if a[0] == 1 or a[-1] == n:
            print(1)
        elif a[0] == n and a[-1] == 1:
            print(3)
        else:
            print(2)
