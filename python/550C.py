n = input()
s = len(n)
a = [[False] * 8 for _ in range(s)]
prev = [[-1] * 8 for _ in range(s)]
a[0][int(n[0]) % 8] = True

for i in range(1, s):
    a[i][int(n[i]) % 8] = True
    for j in range(8):
        if a[i - 1][j]:
            a[i][(j * 10 + int(n[i])) % 8] = True
            prev[i][(j * 10 + int(n[i])) % 8] = j

            a[i][j] = True
            prev[i][j] = j

res = ""
for i in range(s):
    if a[i][0]:
        cur_i = i
        cur_j = 0

        while True:
            if prev[cur_i][cur_j] == -1 or prev[cur_i][cur_j] != cur_j:
                res += n[cur_i]

            if prev[cur_i][cur_j] == -1:
                break

            cur_j = prev[cur_i][cur_j]
            cur_i -= 1
        break

if len(res) > 0:
    print('YES')
    print(res[::-1])
else:
    print('NO')
