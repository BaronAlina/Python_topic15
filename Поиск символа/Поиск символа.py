f = open('input.txt', 'r')
ff=open('output.txt', 'w')
c=f.read(1)
cin=0
while len(c)>0:
    if c=='@':
        ff.write('YES')
        cin+=1
    c=f.read(1)
f.close()
if cin>0:
    ff.write('YES')
else:
    ff.write('NO')
ff.close()
