import math

N = int(input())
a = list(map(int, str(math.factorial(N))))

count = 0
for i in a[::-1]:
    if i == 0:
        count += 1
    else:
        break
print(count)