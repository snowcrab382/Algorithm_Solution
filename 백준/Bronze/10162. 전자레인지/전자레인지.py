T = int(input())
count_a=0
count_b=0
count_c=0
while T != 0:
    if T >= 300:
        T -= 300
        count_a += 1
    else:
        if T >= 60:
            T -= 60
            count_b += 1
        else:
            if T >= 10:
                T -= 10
                count_c += 1
            else:
                break

if 0 < T < 10:
    print(-1)
else:
    print(count_a, count_b, count_c, end= ' ')