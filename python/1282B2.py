nn = int(input())

for _ in range(nn):
    n, p, k = list(map(int, input().split()))
    items = sorted(list(map(int, input().split())))
    count = [0] * k
    loop_count = k
    loop = [True] * k
    p_a = [p] * k
    i = k - 1
    while loop_count > 0:
        if i == n:
            break
        t = i % k
        if items[i] <= p_a[t]:
            count[t] += k
            p_a[t] -= items[i]
        elif loop[t]:
            loop[t] = False
            loop_count -= 1
        i += 1
    for i in range(k - 1):
        if items[i] <= p_a[i]:
            count[i] += k
            p_a[t] -= items[i]
    print(max(count))
