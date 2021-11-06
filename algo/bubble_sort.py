data = [5, 1, 3, 10, 9, -1]

# 1,3,5,9,-1,10
# 1,3,5,-1,9,10
# 1,3,-1,5,9,10
# 1,-1,3,5,9,10
# -1,1,3,5,9,10

# swap이라는 true false를 반환하는 boolean 값을 어디에 놓을지 아는 것이 중요


def bubble_sort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1], data[index2]
                swap = True
        if swap == False:
            break
    return data


print(bubble_sort(data))
