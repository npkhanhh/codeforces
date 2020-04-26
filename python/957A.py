n = int(input())
s = '?' + input() + '?'
res = 'Yes'
flex = False
for i in range(1, n+1):
    if not flex and s[i] == '?':
        if s[i-1] == '?' or s[i+1] == '?':
            flex = True
        elif s[i-1] == s[i+1]:
            flex = True
    if s[i] != '?' and s[i] == s[i-1]:
        res = 'No'
        break
if res == 'Yes' and not flex:
    res = 'No'
print(res)
