T = int(input())
for i in range(T):
    count = 0
    result = input().split('X')
    for x in result:
        for y in range(1,len(x)+1):
            count += y
    print(count)