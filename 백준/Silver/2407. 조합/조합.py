n,m = map(int,input().split())

fac = [i for i in range(101)]
for i in range(2,len(fac)):
    fac[i] *= fac[i-1]

result = fac[n] // (fac[m] * fac[n-m])
print(result)