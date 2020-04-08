import math

for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    delta = 1 + 8 * k
    t = (math.sqrt(delta) - 1) / 2
    if t == math.floor(t):
        t = int(t)
    else:
        t = math.ceil(t)
    t2 = k - int(t*(t-1)/2)
    t = (n - 1) - t
    t2 = n - t2
    a = ['a'] * n
    a[t] = 'b'
    a[t2] = 'b'
    print(''.join(a))

# import math
# for _ in[0]*int(input()):
#     n,k=map(int,input().split());i=math.ceil(((8*k+1)**.5-1)/2)
#     r=['a']*n;r[-i-1]=r[i*(i-1)//2-k]='b';print(''.join(r))
