croatian = ['c=', 'c-', 'd-','dz=', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatian:
    word = word.replace(i, '*')
print(len(word))