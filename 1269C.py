n, k = list(map(int, input().split()))
x = input()

repeat, left = divmod(n, k)
sub = ''
for i in range(k):
    sub += x[i]
result = sub * repeat

if left > 0:
    result += sub[:left]
if int(result) < int(x):
    sub = str(int(sub) + 1)
result = sub * repeat

if left > 0:
    result += sub[:left]

print(n)
print(result)