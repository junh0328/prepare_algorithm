def searchMatrix(matrix, target):
    arr = list()
    for index in range(len(matrix)):
        arr.extend(matrix[index])

    return searchValue(arr, target)


def searchValue(arr, target):
    if len(arr) == 1 and target == arr[0]:
        return True
    if len(arr) == 1 and target != arr[0]:
        return False
    if len(arr) == 0:
        return False

    medium = int(len(arr)/2)
    if target == arr[medium]:
        return True
    else:
        # target가 arr[medium]의 값보다 작을 경우 (왼쪽의 반으로 이동)
        if target < arr[medium]:
            return searchValue(arr[:medium], target)
        else:
            return searchValue(arr[medium:], target)


matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 13


print(searchMatrix(matrix, target))
