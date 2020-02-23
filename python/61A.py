a = input()
b = input()
c = int(a, 2) ^ int(b, 2)
print('{0:0{1}b}'.format(c, len(a)))
