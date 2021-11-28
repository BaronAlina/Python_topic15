def gai_ylii_cezar(i,x):
    i += 1
    code = ''
    for j in x:
        if j.isalpha():
            code += chr(ord(j)+i)
        else:
            code += j
    return code
with open('input.txt') as fil:
    for i,x in enumerate(fil.readlines()):
        print(gai_ylii_cezar(i,x))
