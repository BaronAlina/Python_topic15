with open('input.txt') as file:
    text = file.readlines()
r = 0
textlen = [0]*len(text)
for i in range(len(text)):
    text[i] = text[i].rstrip()
    if r < len(text[i]):
        r = len(text[i])
life = open(r'output.txt', "w+")
for i in range(len(text)):
    if len(text[i]) == r:
        text[i] = text[i].split()
        n = text[i]
        life.writelines("%s\n" % line for line in text[i])
print('Перебор завершён')
life.close()
