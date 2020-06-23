for _ in range(int(input())):
    n = int(input())
    s = input()
    res = ''
    has_1 = has_0 = False
    z = 0
    fixed_z = 0
    o = 0
    count = 0
    for i in s:
        if i == '1':
            has_1 = True
            o += 1
        else:
            o = 0
            if not has_1:
                fixed_z += 1
            else:
                z = 1
    print('0'*(z+fixed_z) + '1'*o)


