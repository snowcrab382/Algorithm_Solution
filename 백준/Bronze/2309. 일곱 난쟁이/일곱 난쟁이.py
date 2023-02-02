import random

a = []
for i in range(9):
    a.append(int(input()))
choice = []
while sum(choice) != 100:
    choice = random.sample(a, 7)
choice.sort()
for j in choice:
    print(j)