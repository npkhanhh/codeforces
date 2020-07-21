keyboard = 'qwertyuiopasdfghjkl;zxcvbnm,./'

d = {'q': 0, 'w': 1, 'e': 2, 'r': 3, 't': 4, 'y': 5, 'u': 6, 'i': 7, 'o': 8, 'p': 9, 'a': 10, 's': 11, 'd': 12, 'f': 13,
     'g': 14, 'h': 15, 'j': 16, 'k': 17, 'l': 18, ';': 19, 'z': 20, 'x': 21, 'c': 22, 'v': 23, 'b': 24, 'n': 25,
     'm': 26, ',': 27, '.': 28, '/': 29}

shift = {'R': -1, 'L': 1}
a = input()
s = input()
res = ''
for c in s:
    res += keyboard[d[c] + shift[a]]
print(res)
