N = int(input())

count,i,result = 0,0,0

while True:
  i += 1
  result += i
  if result > N:
    break
  count += 1
print(count)