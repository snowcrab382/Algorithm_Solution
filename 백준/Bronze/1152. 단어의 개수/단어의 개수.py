sentence = list(input().split(' '))
if sentence[-1] == '':
    del sentence[-1]
if sentence[0] == '':
    del sentence[0]
print(len(sentence))