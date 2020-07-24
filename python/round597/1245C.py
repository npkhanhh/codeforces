dp = [0, 1, 2, 3]
for i in range(4, 10 ** 5 + 2):
    dp.append((dp[i - 2] + dp[i - 1]) % (10 ** 9 + 7))

s = input() + 'a'
res = 1
count_u = 0
count_n = 0
for c in s:
    if c == 'm' or c == 'w':
        res = 0
        break
    elif c == 'u':
        count_u += 1
        if count_n > 0:
            res = (res * dp[count_n]) % (10 ** 9 + 7)
            count_n = 0
    elif c == 'n':
        count_n += 1
        if count_u > 0:
            res = (res * dp[count_u]) % (10 ** 9 + 7)
            count_u = 0
    else:
        if count_u > 0:
            res = (res * dp[count_u]) % (10 ** 9 + 7)
        if count_n > 0:
            res = (res * dp[count_n]) % (10 ** 9 + 7)
        count_u = 0
        count_n = 0
print(res)
