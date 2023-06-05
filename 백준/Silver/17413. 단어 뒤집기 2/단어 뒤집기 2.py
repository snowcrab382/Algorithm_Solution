i,start = 0,0
s = list(input())

while i < len(s):
    if s[i] == '<':
        i += 1
        while s[i] != '>':
            i += 1
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        tmp = reversed(s[start:i])
        s[start:i] = tmp
    else:
        i += 1
print(''.join(s))