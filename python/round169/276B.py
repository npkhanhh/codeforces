s = input()
d = {}
num_ele = 0
num_odd = 0
for c in s:
    if c not in d:
        d[c] = 1
        num_ele += 1

    else:
        d[c] += 1
    if d[c] % 2 == 1:
        num_odd += 1
    else:
        num_odd -= 1

if num_odd <= 1:
    print('First')
else:
    if len(s) % 2 == 1:
        print('First')
    else:
        print('Second')
