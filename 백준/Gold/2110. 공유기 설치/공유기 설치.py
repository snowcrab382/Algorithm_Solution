n, c = map(int,input().split())
house = sorted([int(input()) for _ in range(n)])

def binary_search(house,start,end):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        tmp = house[0]
        cnt = 1

        for i in range(1,n):
            if house[i] >= tmp + mid:
                cnt += 1
                tmp = house[i]

        if cnt >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer

print(binary_search(house, 1, house[-1] - house[0]))