n, m = list(map(int, input().split()))
s = input()
t = input()
if '*' not in s:
    if s != t:
        print('NO')
    else:
        print('YES')
else:
    first, second = s.split('*')
    if m + 1 >= n and t[:len(first)] == first and (t[-len(second):] == second or second == ''):
        print('YES')
    else:
        print('NO')



# input()
# s,t=input(),input()
# if '*'in s:x,y=s.split('*');r=t.startswith(x)and t[len(x):].endswith(y)
# else:r=t==s
# print(('NO','YES')[r])

