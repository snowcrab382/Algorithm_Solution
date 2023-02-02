N = int(input())
N_origin = N
count = 0
while True:
    N_list= list(map(int, str(N)))
    N_list2 = list(map(int,str(sum(N_list))))
    count += 1
    N = N_list[-1]*10 + N_list2[-1]
    if N_origin == N:
        print(count)
        break