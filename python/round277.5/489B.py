n = int(input())
boy = sorted(map(int, input().split()))
m = int(input())
girl = sorted(map(int, input().split()))
b = 0
g = 0
res = 0
while b < n and g < m:
    if boy[b] < girl[g] - 1:
        b += 1
    elif girl[g] < boy[b] - 1:
        g += 1
    else:
        res += 1
        b += 1
        g += 1
print(res)
