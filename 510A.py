n, m = list(map(int, input().split()))

end = True
for i in range(n):
    if i % 2 == 0:
        print('#'*m)
    else:
        if end:
            print('.'*(m-1) + '#')

        else:
            print('#'+'.'*(m-1))
        end = not end