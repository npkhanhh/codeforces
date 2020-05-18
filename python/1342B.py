for _ in range(int(input())):
    s = input()
    if '1' in s and '0' in s:
        if s[0] == '0':
            print('01'*len(s))
        else:
            print('10'*len(s))
    else:
        print(s)
