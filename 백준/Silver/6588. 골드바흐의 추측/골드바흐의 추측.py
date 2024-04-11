import sys
input = sys.stdin.readline 

decimal = [1] * 1000001
tmp = []
for i in range(2, 1001):
    flag = True
    for j in range(1, i+1):
        if i % j == 0 and j != 1 and j != i:
            flag = False
            break
    if flag:
        tmp.append(i)
for i in tmp:
    for j in range(i*2, len(decimal), i):
        decimal[j] = 0

while True:
    even = int(input())
    if not even:
        break

    flag = False
    for i in range(3, 500001):
        if decimal[i] == 1 and decimal[even-i] == 1:
            print(f"{even} = {i} + {even-i}")
            flag = True
            break

    if not flag:
        print("Goldbach's conjecture is wrong.")