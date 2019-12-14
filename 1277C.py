import re

nn = int(input())

for _ in range(nn):
    s = input()
    idx = [m.start(0) + 3 for m in re.finditer("twone", s)]
    s = s.replace("twone", "11111")
    idx += [m.start(0) + 2 for m in re.finditer("two", s)]
    idx += [m.start(0) + 2 for m in re.finditer("one", s)]
    print(len(idx))
    print(*idx)
