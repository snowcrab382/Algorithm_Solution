from collections import Counter

name = input()
count = Counter(name)

odd = 0
pal = ''
for key,value in sorted(count.items()):
    if value % 2 != 0:
        odd += 1
        odd_alphabet = key
    pal += key * (value//2)

if odd > 1:
    print("I'm Sorry Hansoo")
elif odd == 1:
    print(pal + odd_alphabet + pal[::-1])
else:
    print(pal + pal[::-1])