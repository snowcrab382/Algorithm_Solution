n = input().split('-')
result = []

for i in n:
    num = 0
    temp = i.split('+')
    for j in temp:
        num += int(j)
    result.append(num)
ans = result[0]
for k in result[1:]:
    ans -= k
print(ans)