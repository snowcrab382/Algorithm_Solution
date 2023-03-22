def solution(arr):
    n = len(arr)
    result = [0,0]
    def check(x,y,n):
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j] != arr[x][y]:
                    return False
        return True
        
    def quadtree(x,y,z):
        if check(x,y,z):
            result[arr[x][y]] += 1
        else:
            n = z//2
            for i in range(2):
                for j in range(2):
                    quadtree(x+i*n,y+j*n,n)
            
    quadtree(0,0,n)
    return result        