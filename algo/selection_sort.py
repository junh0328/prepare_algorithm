data = [5, 3, 1, 10, 9, -1]

# 1. 주어진 데이터 중, 최솟값을 찾음
# 2. 해당 최솟값을 데이터 맨 앞에 위치한 값과 교체함
# 3. 맨 앞의 위치(인덱스)를 뺀 다음 데이터부터 동일한 방법으로 1-2번 과정을 반복함


def selection_sort(data):
    for standard in range(len(data) - 1):
        lowest = standard
        for index in range(standard+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[standard], data[lowest] = data[lowest], data[standard]
    return data


print(selection_sort(data))
