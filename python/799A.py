import math

n, t, k, d = list(map(int, input().split()))
t1 = math.ceil(n / k) * t
a = d // t
b = n - (a * k)
b /= 2
t2 = d + math.ceil(b / k) * t
print('YES' if t2 < t1 else 'NO')

# Shortest solution found:
# n,t,k,d=map(int,input().split())
# print("YES" if ((d+t)//t)*k<n else "NO")