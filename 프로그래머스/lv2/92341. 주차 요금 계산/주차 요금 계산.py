import math

def solution(fees, records):
    gbtime, gbfee, danwitime, danwifee = fees[0], fees[1], fees[2], fees[3]
    a = dict()
    check = dict()
    result = []
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    a[str(i)+str(j)+str(k)+str(l)] = 0
                    check[str(i)+str(j)+str(k)+str(l)] = 0
    
    for x in records[::-1]:
        if x[-1] == 'N':
            a[x[6:10]] -= 60*int(x[:2])+int(x[3:5])
            check[x[6:10]] = True
        elif x[-1] == 'T':
            a[x[6:10]] += 60*int(x[:2])+int(x[3:5])
            check[x[6:10]] = False
            
    for y in a:
        if a[y] < 0 or (a[y] == 0 and check[y]):
            a[y] += 1439
    
    for z in a:
        if a[z] > 0:
            print(a[z])
            if a[z] <= gbtime:
                a[z] = gbfee
            else:
                if (a[z]-gbtime) % danwitime != 0:
                    a[z] = gbfee + ((a[z]-gbtime) // danwitime + 1) * danwifee
                else:
                    a[z] = gbfee + ((a[z]-gbtime) // danwitime) * danwifee
                
            result.append(a[z])
    
    return result