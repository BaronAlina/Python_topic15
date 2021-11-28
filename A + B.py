f=open('input.txt', 'r')
ff=open('output.txt', 'w')
a=f.readlines()
s=0
for i in a:
    s+=int(i)
ff.write(str(s))
f.close()
ff.close()
