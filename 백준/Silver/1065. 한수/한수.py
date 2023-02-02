N = int(input())
count = 0
if N < 100:
    print(N)
else:
    for i in range(100,N+1):
        if (i // 100) - (i // 10 % 10) == (i // 10 % 10) - i % 10:
            count += 1
    print(count+99)