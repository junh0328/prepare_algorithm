coin_list = [1, 100, 50, 500]


def solution(value, coin_list):
    cnt = 0
    details = list()
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_num = value // coin
        cnt += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])

    return cnt, details


print(solution(5320, coin_list))
