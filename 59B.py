n = int(input())
a = sorted(list(map(int, input().split())))
first_index = -1
count_odd = 0
for idx, value in enumerate(a):
    if value % 2 == 1:
        count_odd += 1
        if first_index == -1:
            first_index = idx
if count_odd == 0:
    print(0)
else:
    if count_odd % 2 == 0:
        del a[first_index]
    print(sum(a))
