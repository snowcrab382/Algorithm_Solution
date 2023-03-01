from collections import deque

def solution(cacheSize, cities):
    queue = deque()
    time = 0
    if cacheSize == 0:
        return len(cities)*5
    for i in cities:
        i = i.lower()
        if i in queue:
            time += 1
            queue.remove(i)
            queue.append(i)
        else:
            time += 5
            if len(queue) < cacheSize:
                queue.append(i)
            else:
                queue.popleft()
                queue.append(i)

    return time