def solution(m, n, startX, startY, balls):
    answer = []
    points = [[-startX,startY],[startX,-startY],[m*2-startX,startY],[startX,2*n-startY]]

    for x,y in balls:
        distance = []
        for pointX, pointY in points:
            ball_dis = (x-pointX)**2+(y-pointY)**2
            start_dis = (startX-pointX)**2+(startY-pointY)**2

            if not (startX==x==pointX or startY==y==pointY) or (ball_dis > start_dis):
                distance.append(ball_dis)
        answer.append(min(distance))

    return answer