max_start_i = max_start_j = 0
min_end_i = min_end_j = 10**10
for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    if x > max_start_i:
        max_start_i = x
    if y < min_end_i:
        min_end_i = y

for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    if x > max_start_j:
        max_start_j = x
    if y < min_end_j:
        min_end_j = y
res = max(max_start_i - min_end_j, max_start_j - min_end_i)
print(res if res > 0 else 0)
