from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n <= 30:
        print("NO")
    else:
        a = [6, 10, 14]
        s = sum(a)
        for idx, val in enumerate(a):
            if n - s == val:
                a[2] = 15
                break
        print("YES")
        print(*a, n - sum(a))

