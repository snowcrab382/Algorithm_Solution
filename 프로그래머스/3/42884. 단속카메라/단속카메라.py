def solution(routes):
    routes.sort(key=lambda x: x[1])
    key = -30001
    cnt = 0
    
    for route in routes:
        print(route)
    	# 기준(카메라)보다 진입지점이 뒤에 있으면
        if route[0] > key:
        	# 단속이 안되기에 카메라 하나 더 필요
            cnt += 1
            # 새로운 기준은 해당 경로의 진출지점(맨끝)
            key = route[1]
            
    return cnt


