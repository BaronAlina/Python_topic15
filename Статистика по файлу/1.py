f=open('input.txt', 'r')
a=f.read().split()
letters=0
words=0
lines=0
for i in a:
    #if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
        #letters+=1
    words+=1
    for l in i:
        if (ord(l)>=65 and ord(l)<=90) or (ord(l)>=97 and ord(l)<=122):
            letters+=1
for l in open('input.txt'):
    lines+=1
print('Input file contains:')
print(str(letters)+' letters')
print(str(words)+' words')
print(str(lines)+' lines')
f.close()
