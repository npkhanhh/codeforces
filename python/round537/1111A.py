v = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
s1 = input()
s2 = input()
if len(s1) != len(s2):
    print('No')
else:
    res = True
    for i in range(len(s1)):
        if s1[i] in v and s2[i] not in v:
            res = False
            break
        elif s1[i] not in v and s2[i] in v:
            res = False
            break
    print('Yes' if res else 'No')
