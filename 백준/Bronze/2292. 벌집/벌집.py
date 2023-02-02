N = int(input())
room = 1
num = 1
i = 0
while N > num:
    i += 1
    num += i * 6
    room += 1
print(room)