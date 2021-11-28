f = open('input.txt', 'r')
a = f.read()
s = 0
p = ''
for i in a:
    if '0' <= i <= '9':
        p += i
    elif p != '':
        s += int(p)
        p = ''
print(s)
f.close()
