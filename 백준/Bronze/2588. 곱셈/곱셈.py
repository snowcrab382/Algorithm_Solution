A = int(input())
B = int(input())

third = B % 10
second = (B // 10) % 10
first = B // 100

result = [A*third, A*second, A*first, A*first*100+A*second*10+A*third]
for i in result:
    print(i)