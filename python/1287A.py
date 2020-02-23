n = int(input())

for i in range(n):
    _ = input()
    s = input()
    res = 0
    temp = 0
    has_a = False
    for c in s:
        if c == 'P' and has_a:
            temp+=1
            if temp > res:
                res = temp
        if c == 'A':
            has_a = True
            temp = 0
    print(res)