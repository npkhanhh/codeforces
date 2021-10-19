n = int(input())
a = list(map(int, input().split()))
counter = 1
res = 1
min_a = a[0]
for i in range(1, n):
    if a[i] == min_a:
        counter += 1
    elif a[i] < min_a:
        min_a = a[i]
        counter = 1
        res = i+1
print(res if counter == 1 else "Still Rozdil")
