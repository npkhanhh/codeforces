s = input()
t = s
has_ab = has_ba = False
if 'AB' in t:
    has_ab = True
    t = t.replace('AB', ' ', 1)
if 'BA' in t:
    has_ba = True

if not (has_ab and has_ba):
    has_ab = has_ba = False
    if 'BA' in s:
        has_ba = True
        s = s.replace('BA', ' ', 1)
    if 'AB' in s:
        has_ab = True
print('YES' if has_ab and has_ba else 'NO')
