n = int(input())
a = list(map(int,input().split()))
LIS = [a[0]]

def binary_search(e):
    start = 0
    end = len(LIS) - 1

    while start <= end:
        mid = (start + end) // 2

        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(n):
    if a[i] > LIS[-1]:
        LIS.append(a[i])
    else:
        idx = binary_search(a[i])
        LIS[idx] = a[i]
        
print(len(LIS))