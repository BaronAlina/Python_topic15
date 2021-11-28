f=open('input.txt','r')

lines, letters, words = 0, 0, 0

word = ""

for ch in f.read():

   if ch == '\n':

       lines += 1

   if ch.isalpha():

       letters += 1

       word += ch

   elif word != "":

       word = ""

       words += 1

print('Input file contains:')

print(letters, 'letters')

print(words, 'words')

print(lines, 'lines')

f.close()
