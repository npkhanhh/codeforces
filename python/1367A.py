for _ in range(int(input())):
    s = input()
    res = s[0:2]
    for i in range(3, len(s), 2):
        res += s[i]
    print(res)
