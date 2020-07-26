n = int(input())
a = sorted(map(int, input().split()))
t = n//2
s1 = sum(a[:t])
s2 = sum(a[t:])
print(s1**2+s2**2)
