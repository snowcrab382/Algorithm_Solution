from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * (bridge_length))
    i,cnt,tmp = 0,0,0
    while i != len(truck_weights) and bridge:
        tmp -= bridge.popleft()
        if tmp + truck_weights[i] > weight:
            bridge.append(0)
        else:
            bridge.append(truck_weights[i])
            tmp += truck_weights[i]
            i += 1
        cnt += 1
    return cnt+bridge_length
            
            
# 0 0
# 0 7
# 7 0
# 0 4
# 4 5
# 5 0
# 0 6
# 6 0
# 0 0