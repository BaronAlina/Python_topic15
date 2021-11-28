f = open('input.txt', 'r')
a = f.read()
p = ''
for i in a:
    s = 0
    if i != '\n':
        p += i
    else:
        for i in p.split():
            s += int(i)
        print(s)
        p = ''
if p != '':
    for i in p.split():
        s += int(i)
    print(s)
f.close()
