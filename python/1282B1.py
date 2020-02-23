nn = int(input())

for _ in range(nn):
    n, p, k = list(map(int, input().split()))
    items = sorted(list(map(int, input().split())))
    res = 0
    odd = True
    count_odd = 0
    count_even = 0
    loop_odd = True
    loop_even = True
    p_odd = p_even = p
    i = 1
    while loop_odd or loop_even:
        if i == n+1:
            break
        if i % 2 == 0:
            if items[i-1] <= p_even:
                count_even += 2
                p_even -= items[i-1]
            else:
                loop_even = False
        else:
            if items[i-1] <= p_odd:
                count_odd += 2 if i > 1 else 1
                p_odd -= items[i-1]
            else:
                loop_odd = False
        i+=1
    print(max(count_even, count_odd))

