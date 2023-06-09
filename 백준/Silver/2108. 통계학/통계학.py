from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
a = sorted([int(input()) for _ in range(n)])

mode = []
b = dict(Counter(a))
b_max = max(b.values())
for i in b:
  if b[i] == b_max:
    mode.append(i)

if len(sorted(mode)) > 1:
  mode_val = mode[1]
else:
  mode_val = mode[0]

print(round(sum(a)/n))
print(a[n//2])
print(mode_val)
print(a[-1]-a[0])