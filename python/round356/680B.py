
n, a = list(map(int, input().split()))
arr = list(map(int, input().split()))
a -= 1

res = 0
for i in range(n):
    if i == 0:
        res += arr[a]
    elif a+i < n and a - i > -1:
        if arr[a+i] == 1 and arr[a-i] == 1:
            res += 2
    elif a+i < n:
        res += arr[a+i]
    elif a-i > -1:
        res += arr[a-i]
print(res)
