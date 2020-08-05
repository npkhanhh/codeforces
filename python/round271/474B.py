n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
t = [0]
for idx, val in enumerate(a):
    for j in range(val):
        t.append(idx + 1)
for val in q:
    print(t[val])

