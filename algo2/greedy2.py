data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]


def solution(data_list, max_weight):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        # 가방 하나가 온전히 들어 갔을 때
        if max_weight - data[0] >= 0:
            max_weight -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        # 가방 하나가 온전히 들어 가지 못했을 때
        else:
            # 비율로 계산하여 (무게를 나눠) 넣는다
            percentage = max_weight / data[0]
            total_value += data[1] * percentage
            details.append([data[0], data[1], percentage])
            break

    return total_value, details


print(solution(data_list, 29))
