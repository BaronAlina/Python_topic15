f = open('input.txt', 'r')
a, b = f.read().split()
print(int(a) + int(b))
f.close()
