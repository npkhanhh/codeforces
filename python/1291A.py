for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))
    while len(a) > 0 and a[-1] % 2 == 0:
        del a[-1]
    need_deleted = sum(a) % 2 == 1
    if need_deleted:
        for idx, value in enumerate(a[:-1]):
            if value % 2 == 1:
                need_deleted = False
                del a[idx]
                break
    while len(a) > 0 and a[0] == 0:
        del a[0]
    if len(a) > 0 and not need_deleted:
        print(''.join(map(str, a)))
    else:
        print(-1)


