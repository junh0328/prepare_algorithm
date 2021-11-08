# 순차 탐색
# list.prototype.indexOf() 메서드와 동일한 기능
# 직접 만들어 본다고 생각하면 편할듯
# 있을 경우 해당 인덱스를 반환
# 없을 경우 -1 반환

def indexOf(data, search):
    for index in range(len(data)):
        if search == data[index]:
            return index
    return -1


li = [10, 3, 5, 1, 14, 11, 6]

print(indexOf(li, 3))
print(indexOf(li, 7))
