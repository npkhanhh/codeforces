n = int(input())
a = list(map(int, input().split()))
largest = 0
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
    if d[i] > largest:
        largest = d[i]
print(largest, len(d))
