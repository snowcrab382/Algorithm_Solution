from itertools import permutations

def solution(user_id, banned_id):
    
    def isBanned(user_id, banned_id):
        if len(user_id) != len(banned_id):
            return False

        flag = True
        for i in range(len(banned_id)):
            if banned_id[i] == '*':
                continue
            if user_id[i] != banned_id[i]:
                flag = False
                break
        return flag


    answer = set()
    size = len(banned_id)

    for i in permutations(user_id, size):
        cnt = 0
        visited = [0] * size
        for u in i:
            for b in range(size):
                if not visited[b] and isBanned(u, banned_id[b]):
                    visited[b] = 1
                    cnt += 1
                    break
                    
        if cnt == size:
            tmp = list(i)
            tmp.sort()
            tmp = tuple(tmp)
            if tmp not in answer:
                answer.add(tmp)
        
    return len(answer)