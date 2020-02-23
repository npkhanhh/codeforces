l = input()[1:-1]
if len(l) > 0:
    print(len(set(l.split(", "))))
else:
    print(0)

