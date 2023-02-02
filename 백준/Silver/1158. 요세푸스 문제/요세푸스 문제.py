N,K = map(int,input().split())
N_list = list(i for i in range(1,N+1))
count = 0
a = []
while len(a) != N:
    for i in range(len(N_list)):
        count += 1
        if count == K:
            count = 0
            a.append(str(N_list[i]))
            N_list[i] = 0
    for j in range(N_list.count(0)):
        N_list.remove(0)
print('<'+', '.join(a)+'>')