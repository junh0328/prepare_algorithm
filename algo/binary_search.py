# 이진 탐색은 정렬된 배열 구조를 검색할 때 사용된다
# [0]부터 순차적으로 탐색하는 함수보다 훨씬 빠르다
# 데이터가 순차적이지 않을 경우 >>> list.sort() 메서드를 사용하여 정렬 후 사용한다

def binary_search(data, search):
    # 처음 들어온 값이, search(찾으려는 값)와 같은지 확인
    if len(data) == 1 and search == data[0]:
        return True
    if len(data) == 1 and search != data[0]:
        return False
    if len(data) == 0:
        return False

    medium = int(len(data)/2)
    if search == data[medium]:
        return True
    else:
        # search가 data[medium]의 값보다 작을 경우 (왼쪽의 반으로 이동)
        if search < data[medium]:
            return binary_search(data[:medium], search)
        else:
            return binary_search(data[medium:], search)


data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

print(binary_search(data, 30))
print(binary_search(data, 15))
