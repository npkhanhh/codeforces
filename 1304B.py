n, m = list(map(int, input().split()))
d = {}
left = right = ""
for _ in range(n):
    s = input()
    s1 = s[::-1]
    if s in d:
        left += s1
        right = s + right
        del d[s]
    else:
        d[s1] = True
longest_palin = ""
for key in d:
    if key == key[::-1]:
        if len(key) > len(longest_palin):
            longest_palin = key
res = left+longest_palin+right
print(len(res))
print(res)

