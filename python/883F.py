d = {}

for _ in range(int(input())):
    s =input()
    s = s.replace('u', 'oo')
    while 'kh' in s:
        s = s.replace('kh', 'h')
    d[s] = True
print(len(d.keys()))
