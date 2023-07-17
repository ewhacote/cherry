from heapq import heappop, heappush


def solution(book_time):
    room = []
    book_time.sort(key=lambda x: x[0])
    for book in book_time:
        check_in = 60 * int(book[0][:2]) + int(book[0][3:])
        check_out = 60 * int(book[1][:2]) + int(book[1][3:]) + 10
        if len(room) != 0 and room[0] <= check_in:
            heappop(room)
        heappush(room, check_out)
    return len(room)
