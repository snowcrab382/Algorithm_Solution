num_16 = list(input())
dict_16 = {'A' : 10, 'B':11, 'C':12, 'D':13,'E':14, 'F': 15}
num_10 = 0

for x in dict_16:
    for y in range(len(num_16)):
        if num_16[y] == x:
            num_16[y] = dict_16[x]

for j in range(len(num_16)):
    num_10 += int(num_16[j]) * (16 ** (len(num_16) - j - 1))
print(num_10)