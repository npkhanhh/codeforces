from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    d = {}
    last_element = -1
    for i in range(1, n):
        if a[i] != a[i-1]:
            if last_element != -1:
                if last_element in d:
                    d[last_element] += 1
                else:
                    d[last_element] = 1
            last_element = a[i]
    if last_element == -1:
        print(0)
    elif a[0] not in d or last_element not in d:
        print(1)
    else:
        print(min(d.values()) + 1)
