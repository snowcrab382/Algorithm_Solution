def solution(dirs):
    d = {"U":(1,0),"R":(0,1),"D":(-1,0),"L":(0,-1)}
    x,y = 0,0
    a = set()
    for i in dirs:
        dx,dy = d[i]
        if -5 <= x+dx <= 5 and -5 <= y+dy <= 5:
            a.add(((x,y),(x+dx,y+dy)))
            a.add(((x+dx,y+dy),(x,y)))
            x += dx
            y += dy
    return len(a)//2

            