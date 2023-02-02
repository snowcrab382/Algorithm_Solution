H,M = map(int,input().split())
cook = int(input())
new_alarm = H*60 + M + cook
new_Hour = new_alarm // 60
if new_Hour >= 24:
    new_Hour -= 24
new_Min = new_alarm % 60
print(new_Hour, new_Min)