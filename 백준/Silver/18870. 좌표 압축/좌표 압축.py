n = int(input())
a = list(map(int, input().split()))
unique = sorted(list(set(a)))
dic = dict()

for i in range(len(unique)):
    dic[unique[i]] = i

for j in a:
    print(dic[j], end=' ')