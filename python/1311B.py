for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    p = list(map(lambda x: int(x)-1, input().split()))
    while True:
        swapped = False
        for i in p:
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if not swapped:
            break
    result = 'YES'
    for i in range(n-1):
        if a[i] > a[i+1]:
            result = 'NO'
            break
    print(result)

####
# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     l = [*map(int, input().split())]
#     p = sorted([*map(int, input().split())])
#     for _ in range(n):
#         for i in p:
#             l[i - 1], l[i] = sorted(l[i - 1 : i + 1])
#     print(['NO', 'YES'][l == sorted(l)])