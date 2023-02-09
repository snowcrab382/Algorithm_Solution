def solution(n, m):
    result = []
    def gcd(n,m):
        if n == 0:
            return m
        return gcd(m%n,n)
    
    def lcm(n,m):
        return m // gcd(n,m) * n
    
    result.append(gcd(n,m))
    result.append(lcm(n,m))
    return result