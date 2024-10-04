from collections import deque
import sys
input = sys.stdin.readline

def D(num):
    return num * 2 % 10000

def S(num):
    return (num - 1) % 10000

def L(num):
    return num // 1000 + (num % 1000) * 10

def R(num):
    return num // 10 + (num % 10) * 1000


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    q = deque([(a, "")])
    visited = [False] * 10001
    visited[a] = True

    while q:
        num, command = q.popleft()
        if num == b:
            print(command)
            break

        d = D(num)
        if not visited[d]:
            visited[d] = True
            q.append((d, command + 'D'))

        s = S(num)
        if not visited[s]:
            visited[s] = True
            q.append((s, command + 'S'))

        l = L(num)
        if not visited[l]:
            visited[l] = True
            q.append((l, command + 'L'))

        r = R(num)
        if not visited[r]:
            visited[r] = True
            q.append((r, command + 'R'))
