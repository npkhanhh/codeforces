n = int(input())
s = input()
s_f = f_s = 0
for idx in range(1, n):
    if s[idx] == 'F' and s[idx-1] == 'S':
        s_f += 1
    if s[idx] == 'S' and s[idx-1] == 'F':
        f_s += 1
print('YES' if s_f > f_s else 'NO')