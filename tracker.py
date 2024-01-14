#from sys import argv

#program_name, offensetest = argv

points = 0
listoff = ['bdt']
f = open('mem.txt', 'r+')
file_cont = f.readlines()
f.close()
print(file_cont)
if file_cont != []:
    for i in range(0, len(file_cont)):
        a = str(file_cont.pop(0))
        a.removesuffix('\\n')
        file_cont.append(a)
else:
    f = open('mem.txt', 'w+')
    temp = 'p.0000\n[]\nbto.0000'
    f.write(temp)
    f.close()
f = open('mem.txt', 'r+')
file_cont = f.readlines()
f.close()
print(file_cont)