def solution(bridge_length, weight, truck_weights):
    time = 0
    x = [0] * bridge_length
    truck_weights = list(truck_weights)
    s = 0
    while x:
        time += 1
        s -= x.pop(0)
        if truck_weights:
            if s + truck_weights[0] <= weight:
                s += truck_weights[0]
                x.append(truck_weights.pop(0))
            else:
                x.append(0)
    return time
