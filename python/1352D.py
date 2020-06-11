from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, input().split()))
    res, alice, bob = 1, a[0], 0
    i = 1
    j = n - 1
    al = False
    prev_a = a[0]
    prev_b = 0
    while i <= j:
        res += 1
        t = 0
        prev_move = prev_b if al else prev_a
        while t <= prev_move and i <= j:
            if al:
                t += a[i]
                i += 1
            else:
                t += a[j]
                j -= 1
        if al:
            alice += t
            prev_a = t
        else:
            bob += t
            prev_b = t
        al = not al
    print(res, alice, bob)



