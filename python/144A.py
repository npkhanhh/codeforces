n = int(input())
a = list(map(int, input().split()))
first_max = last_min = 0
for i in range(1, n):
    if a[i] > a[first_max]:
        first_max = i
    elif a[i] <= a[last_min]:
        last_min = i
res = first_max + n - (last_min + 1)
if first_max > last_min:
    res -= 1
print(res)

