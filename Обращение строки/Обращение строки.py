f = open('input.txt', 'r')
ff=open('output.txt', 'w')
txt = f.read()
ff.write(txt[::-1][1:])
f.close()
ff.close()
