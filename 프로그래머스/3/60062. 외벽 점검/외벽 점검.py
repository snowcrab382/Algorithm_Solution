from itertools import permutations
from collections import deque

def solution(n, weak, dist):
    # 가장 멀리 갈 수 있는 친구 순으로
    dist.sort(reverse=True)
    
    len_weak = len(weak)
    # 원형 -> 선형으로
    weak = weak + [num+n for num in weak] 
    
    for i in range(1,len(dist)+1):
        # 거리가 먼 친구순으로 i명 선택 -> 그 친구들을 순서 섞기
        for ff in permutations(dist[:i]):
            # 점검 시작점
            for idx in range(len_weak):
                friends = deque(list(ff))
                new_weak = deque(weak[idx:idx+len_weak])

                # 점검
                while friends and new_weak:
                    # 이번에 점검할 친구가 움직일 거리
                    f = friends.popleft()
                    # 이번에 점검할 지점 위치
                    w = new_weak.popleft()
                    # 친구가 점검 끝났을 때 위치
                    current = f+w

                    # w와 current 사이에 있는 지점은 f 친구가 다 점검함
                    while new_weak and new_weak[0] <= current:
                        new_weak.popleft()
                
                # 다 점검했으면
                if len(new_weak) == 0:
                    return i
    return -1