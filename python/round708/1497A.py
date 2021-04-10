from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = sorted(map(int, stdin.readline().split()))
    main = [a[0]]
    rest = []
    for i in range(1, n):
        if a[i] != a[i-1]:
            main.append(a[i])
        else:
            rest.append(a[i])
    main += rest
    print(*main)
