n, sx, sy = list(map(int, input().split()))

res = [0, 0, 0, 0]
for _ in range(n):
    x, y = list(map(int, input().split()))
    if y > sy:
        res[0] += 1
    if x > sx:
        res[1] +=1
    if y < sy:
        res[2] += 1
    if x < sx:
        res[3] +=1

t = max(res)
print(t)
if t == res[0]:
    print(sx, sy+1)
elif t == res[1]:
    print(sx + 1, sy)
elif t == res[2]:
    print(sx, sy-1)
elif t == res[3]:
    print(sx-1, sy)
