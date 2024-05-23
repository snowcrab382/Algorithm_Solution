n, m = map(int,input().split())
known = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & known:
            known = known.union(party)

result = 0
for party in parties:
    if party & known:
        continue
    result += 1
print(result)