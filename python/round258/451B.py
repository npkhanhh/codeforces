n = int(input())

a = list(map(int, input().split()))

decreased = False
decreasing = False
start = -1
end = -1
res = 'yes'
for i in range(1, n):
    if a[i - 1] > a[i]:
        if decreased:
            res = 'no'
            break
        if not decreasing:
            start = i - 1
            decreasing = True
    else:
        if decreasing:
            decreasing = False
            decreased = True
            if start > 0 and a[start-1] > a[i-1]:
                res = 'no'
            if a[start] > a[i]:
                res = 'no'
            end = i - 1


if start > -1 and end == -1:
    end = n - 1
    if start > 0 and a[start-1] > a[end]:
        res = 'no'
print(res)
if res == 'yes':
    if start == -1 and end == -1:
        start = 0
        end = 0
    print(start + 1, end + 1)
