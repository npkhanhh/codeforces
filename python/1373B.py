for _ in range(int(input())):
    s = input()
    a = [0, 0]
    for i in s:
        a[int(i)] += 1
    print('DA' if min(a) % 2 == 1 else 'NET')
