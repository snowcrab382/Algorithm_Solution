x,y,w,h = map(int,input().split())
a = [w-x,h-y,x,y]
print(min(a))