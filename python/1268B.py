n = int(input())

l = list(map(int, input().split()))

odd_prev = False
res = 0
for i in l:
    if i % 2 == 1:
        res += (i-1)/2
        if odd_prev:
            res += 1
            odd_prev = False
        else:
            odd_prev = True
    else:
        res += i/2
        odd_prev = False
print(int(res))
