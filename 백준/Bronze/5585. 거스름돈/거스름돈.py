money = int(input())
money = 1000 - money
l = [500,100,50,10,5,1]
count = 0
for i in l:
    count += money // i
    money %= i
print(count)