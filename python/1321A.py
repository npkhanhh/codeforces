n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_t = b_t = 0
for i in range(n):
    if a[i] == 1 and b[i] == 0:
        a_t += 1
    elif a[i] == 0 and b[i] == 1:
        b_t += 1
if a_t == 0:
    print(-1)
else:
    print(b_t // a_t + 1)

# I=input
# I()
# r=p=0
# for x,y in zip(I(),I()):r+=x>y;p+=x<y
# print(r and p//r+1or-1)
