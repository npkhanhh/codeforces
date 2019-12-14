from operator import itemgetter

n = int(input())
l = list(map(int, input().split()))
l = [(i + 1, v) for i, v in enumerate(l)]
l = sorted(l, key=itemgetter(1), reverse=True)
shot = 0
result = []
for i in range(n):
    result.append(l[i][0])
    shot += l[i][1] * i + 1
print(shot)
print(*result)