a = list(i for i in range(1,2666800) if '666' in str(i))
N = int(input())
print(a[N-1])