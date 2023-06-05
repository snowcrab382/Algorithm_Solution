i,start = 0,0
s = list(input())

while i < len(s):
    if s[i] == '<':
        while s[i] != '>':
            i += 1
        i += 1
    elif s[i].isalnum():
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        s[start:i] = reversed(s[start:i])
    else:
        i += 1
print(''.join(s))
