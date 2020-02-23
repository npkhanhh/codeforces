nn = int(input())

for _ in range(nn):
    n = int(input())
    l = list(map(int, input().split()))
    d = {}
    count = 0
    for e in l:
        while e % 2 == 0:
            if e not in d:
                d[e] = 1
                count += 1
                e = int(e/2)
            else:
                break
    print(count)

