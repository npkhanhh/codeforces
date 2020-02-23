n, v1, v2, t1, t2 = list(map(int, input().split()))

a1 = t1 + v1 * n + t1
a2 = t2 + v2 * n + t2
if a1 < a2:
    print('First')
elif a2 < a1:
    print('Second')
else:
    print('Friendship')
