n, k = list(map(int, input().split()))
s = input()
k /= 2
end = 0
for i, v in enumerate(s):
    if v == ')':
        k -= 1
        if k == 0:
            end = i
s1 = list(s[:end+1])
cur = 0
for i in range(len(s1)-1, -1, -1):
    if s1[i] == ')':
        cur += 1
    else:
        if cur == 0:
            del s1[i]
        else:
            cur -= 1
print(''.join(s1))
