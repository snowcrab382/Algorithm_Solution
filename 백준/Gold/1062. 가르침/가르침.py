from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

def solve(n, k):
    required = {"a","n","t","i","c"}
    uniqueList = []
    uniqueSet = set()
    cnt = 0
    for _ in range(n):
        cur = input().strip()
        curSet = set(cur)
        curSetLen = len(curSet)
        if curSetLen > k:
            continue

        if curSetLen == 5:
            cnt += 1
            continue

        curUnique = curSet - required
        uniqueList.append(curUnique)
        uniqueSet.update(curUnique)

    if k < 5:
        return 0

    if len(uniqueList) == 0:
        return cnt

    if len(uniqueSet) <= k - 5:
        return cnt + len(uniqueList)

    maxCnt = 0
    for c in combinations(uniqueSet, k-5):
        caseSet = set(c)
        tmpAns = 0
        for uniqueWord in uniqueList:
            if caseSet.issuperset(uniqueWord):
                tmpAns += 1
        maxCnt = max(maxCnt, tmpAns)

    cnt += maxCnt
    return cnt

print(solve(n, k))