import itertools
import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
hap,min_num = 0,40000
for i in a:
    hap += sum(i)

people = list(range(n))
for i in itertools.combinations(people,n//2):
    start,link = list(set(i)),list(set(people)-set(i))
    s_count,l_count = 0,0
    for j in itertools.permutations(start,2):
        s_count += a[j[0]][j[1]]
    for k in itertools.permutations(link,2):
        l_count += a[k[0]][k[1]]
    min_num = min(abs(s_count-l_count),min_num)
print(min_num)