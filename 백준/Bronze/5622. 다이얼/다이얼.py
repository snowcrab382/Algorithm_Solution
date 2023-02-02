alphabet = input()
count = 0
for i in alphabet:
    if  i in 'ABC':
        count += 3
    elif i in 'DEF':
        count += 4
    elif i in 'GHI':
        count += 5
    elif i in 'JKL':
        count += 6
    elif i in 'MNO':
        count += 7
    elif i in 'PQRS':
        count += 8
    elif i in 'TUV':
        count += 9
    elif i in 'WXYZ':
        count += 10
print(count)