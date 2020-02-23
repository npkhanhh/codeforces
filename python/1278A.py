

def is_permumation(s1, s2):
    if len(s1) != len(s2):
        return False
    d = {}
    for c in s1:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    for c in s2:
        if c not in d:
            return False
        else:
            d[c] -= 1
            if d[c] == 0:
                del d[c]
    return len(d.keys()) == 0

n = int(input())

for _ in range(n):
    s = input()
    p = input()

    res = 'NO'
    for i in range(len(p) - len(s) + 1):
        if is_permumation(s, p[i:i+len(s)]):
            res = 'YES'
            break
    print(res)
