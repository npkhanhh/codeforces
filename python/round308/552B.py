n = input()
length = len(n)
n = int(n)
res = (n - 10**(length-1) + 1) * length
for i in range(1, length):
    res += (10**i - 10**(i-1)) * i
print(res)
