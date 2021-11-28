f = open('input.txt', 'r')
a = f.read()
y = a.find('@')
if y == -1:
    print('NO')
else:
    print('YES')
f.close()
