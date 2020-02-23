res_m = res_c = 0
for _ in range(int(input())):
    m, c = map(int, input().split())
    if m > c:
        res_m += 1
    if c > m:
        res_c += 1
if res_m > res_c:
    print('Mishka')
elif res_c > res_m:
    print('Chris')
else:
    print('Friendship is magic!^^')
