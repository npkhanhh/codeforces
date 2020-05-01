def nCr(n):
    return (n-1)*n//2

n, m = list(map(int, input().split()))
a, b = divmod(n,m)
res_min = b*nCr(a+1)
if a >= 2:
    res_min += (m-b)*nCr(a)
res_max = nCr(n - (m-1))
print(res_min, res_max)