N = int(input())
a = list(map(int,input().split()))
a = list(i/max(a)*100 for i in a)
print(sum(a)/N)