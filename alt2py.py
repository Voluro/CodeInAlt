print('welcome to codeInAlt')
print('place the file you want to compile in the same directory as this file')
a = input('exact file name without .alt: ')
file = open(f'{a}.alt', 'r')
file = file.read()
ls = file.split(';\n')
print(ls)
am = []
def value(inp):
    if inp.split("/")[0] == 
for i in ls:
    if i != "":
        am.append(i)
print(am)
for i in am:
    if i.split()[1] == 'set':
        print(f'{i.split()[0]} = {i.split()[2]}')
