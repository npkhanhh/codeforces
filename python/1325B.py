for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        if i not in d:
            d[i] = 1
    print(len(d))