n = int(input())
s = 0
for i in range(1,n+1):
    print(s)
    s += (pow(-1, i))*i
