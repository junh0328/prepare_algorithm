# 문제 제목 응계
# 문제 난이도 하
# 문제 유형: 배열, 구현
# 추천 풀이 시간: 15분
# https://www.acmicpc.net/problem/2920


def solution(arr):
    result = list()
    answer = ''

    for i in range(len(arr)):
        if(arr[i] == 'c'):
            result.append(1)
        elif(arr[i] == 'd'):
            result.append(2)
        elif(arr[i] == 'e'):
            result.append(3)
        elif(arr[i] == 'f'):
            result.append(4)
        elif(arr[i] == 'g'):
            result.append(5)
        elif(arr[i] == 'a'):
            result.append(6)
        elif(arr[i] == 'b'):
            result.append(7)
        elif(arr[i] == 'C'):
            result.append(8)
        else:
            return None

    if result == sorted(result):
        answer = 'ascending'
    elif result == sorted(result, reverse=True):
        answer = 'descending'
    else:
        answer = 'mixed'

    return answer


arr = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'C']
arr2 = ['C', 'b', 'a', 'g', 'f', 'e', 'd', 'c']
arr3 = ['C', 'd', 'a', 'g', 'f', 'e', 'b', 'c']

print(solution(arr))
print(solution(arr2))
print(solution(arr3))
