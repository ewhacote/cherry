def solution(record):
    users = {}
    result = []

    for r in record:
        user = r.split()
        if (user[0] == "Enter" or user[0] == "Chage"):
            users[user[1]] = user[2]

    for r in record:
        user = r.split()
        if user[0] == "Enter":
            result.append(users[user[1]]+"님이 들어왔습니다.")
        elif user[0] == "Leave":
            result.append(users[user[1]] + "님이 나갔습니다.")

    return result