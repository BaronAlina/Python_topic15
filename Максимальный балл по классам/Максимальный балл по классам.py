s9 = 0

s10 = 0

s11 = 0

f = open('input.txt', 'r', encoding = 'utf-8')

s = f.readlines()

for i in s:

    a = ''

    y = 0

    while i[y] != '9' and i[y] != '1':

        y += 1

    if i[y] == '9':

        for j in i[y+1:]:

            if '0' <= j <= '9':

                a += j

        if int(a) > s9:

            s9 = int(a)

    else:

        for j in i[y+2:]:

            if '0' <= j <= '9':

                a += j

        if i[y+1] == '0' and int(a) > s10:

            s10 = int(a)

        elif i[y+1] == '1' and int(a) > s11:

            s11 = int(a)

print(s9, s10, s11)

f.close()
