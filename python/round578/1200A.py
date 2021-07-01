n = int(input())
s = input().strip()
a = [0]*10
for i in s:
    if i == 'L':
        for j in range(10):
            if a[j] == 0:
                a[j] = 1
                break
    elif i == 'R':
        for j in range(9, -1, -1):
            if a[j] == 0:
                a[j] = 1
                break
    else:
        idx = int(i)
        a[idx] = 0
print(''.join(map(str, a)))

