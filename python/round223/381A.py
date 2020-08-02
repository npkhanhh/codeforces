n = int(input())
a = list(map(int, input().split()))
i = 0
j = n - 1
s_turn = True
res = [0, 0]
while i <= j:
    t = 0
    if a[i] > a[j]:
        t = a[i]
        i += 1
    else:
        t = a[j]
        j -= 1
    if s_turn:
        res[0] += t
    else:
        res[1] += t
    s_turn = not s_turn
print(*res)
