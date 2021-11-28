f=open('input.txt', 'r')
ff=open('output.txt', 'w')
#print(*(sum(map(int, i.split())) for i in f.readlines()), sep='\n')
sm=0
print(*(sm+=(map(int, i.split())) for i in f.readlines()), sep='\n')
ff.write(s)
f.close()
ff.close()
