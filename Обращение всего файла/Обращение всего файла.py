f = open('input.txt', 'r')
ff=open('output.txt', 'w')
txt = f.read()
txt=txt.split('\n')
for i in list(reversed(txt)):
    pr=(i[::-1][:])+'\n'
    ff.write(pr)
f.close()
ff.close()
