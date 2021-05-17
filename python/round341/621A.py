n = int(input())
a = sorted(map(int, input().split()))
t = sum(a)
if t % 2 == 1:
    for i in a:
        if i % 2 == 1:
            t -= i
            break
print(t)
