s = input()

res = -1
i = -1

for idx, val in enumerate(s):
    if val in ['A', 'E', 'I', 'O', 'U', 'Y']:
        if idx - i > res:
            res = idx - i
        i = idx
if len(s) - i > res:
    res = len(s) - i
print(res)
