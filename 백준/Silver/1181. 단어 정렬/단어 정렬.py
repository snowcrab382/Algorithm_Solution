a = list([] for i in range(51))
N = int(input())
for i in range(N):
    word = input()
    if word in a[len(word)]:
        continue
    else:
        a[len(word)].append(word)
for j in a:
    j.sort()
for k in range(len(a)):
    for l in range(len(a[k])):
        print(a[k][l])