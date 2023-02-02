x = int(input())
stick = [64,32,16,8,4,2,1]
count = 0

for i in stick:
    if i <= x:
        count += 1
        x -= i
    if x == 0:
        break
print(count)