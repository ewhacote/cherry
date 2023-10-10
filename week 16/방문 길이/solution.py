def solution(dirs):
    answer = 0
    x = 5
    y = 5
    # 'U', 'D', 'R', 'L'
    Map = []
    move = {'U':(0,-1),'D':(0,1),'R':(1,0),'L':(-1,0)}
    for i in range(len(dirs)):
        (dy,dx) = move[dirs[i]]
        if not (0 <= x+dx and x+dx <=10 and 0<=y+dy and y+dy<=10):
            continue
        Map.append((x,y,x+dx,y+dy))
        Map.append((x+dx,y+dy,x,y))
        x = x + dx
        y = y + dy
    mapSet = set(Map)
    answer=len(mapSet)//2

    return answer