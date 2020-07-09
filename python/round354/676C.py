n, k = list(map(int, input().split()))
s = input()
res = 0
count_a = 0
count_b = 0
left = 0
right = 0
while True:
    if s[right] == 'a':
        count_a += 1
    else:
        count_b += 1
    if count_a <= k or count_b <= k:
        if right - left + 1 > res:
            res = right - left + 1
    else:
        if s[left] == 'a':
            count_a -= 1
        else:
            count_b -= 1
        left += 1
    right += 1
    if n - left < res or right == n:
        break
print(res)

