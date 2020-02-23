s = input()

n_a = 0
for i in s:
    if i == 'a':
        n_a += 1

if n_a > len(s) // 2:
    print(len(s))
else:
    print(n_a*2-1)
