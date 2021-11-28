f=open('input.txt', 'r')
ff=open('output.txt', 'w')
a=f.read()
a=a.split('\n')
st=''
for i in a:
    st+=i
b=st.split(' ')
s=0
for i in b:
    if i=='':
        a=1
        ff.write('')
    else:
        s+=int(i)
ff.write(str(s))
f.close()
ff.close()
