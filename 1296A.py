for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    has_even = has_odd = False
    for i in a:
        if i % 2 == 0:
            has_even = True
        else:
            has_odd = True
        if has_even and has_odd:
            break
    if has_even and has_odd:
        print('YES')
    elif has_odd and n % 2 == 1:
        print('YES')
    else:
        print('NO')