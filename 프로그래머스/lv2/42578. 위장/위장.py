def solution(clothes):
    item = []
    check = set()
    result = []
    for name,kind in clothes:
        check.add(kind)
        item.append(kind)
    
    for i in check:
        result.append(item.count(i)+1)
    
    tmp = 1
    for j in result:
        tmp *= j
    
    return tmp-1
    