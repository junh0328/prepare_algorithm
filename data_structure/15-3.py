# Linear Probling 기법

# 폐쇄 해슁 또는 Close Hashing 기법 중 하나: 해쉬 테이블 저장공간 안에서 충돌 문제를 해결하는 기법
# 충돌이 일어난다면, 해당 hash address의 다음 address부터 맨 처음 나오는 빈 공간에 저장하는 기법
# 저장 공간 활용도를 높이기 위한 기법

hash_table = list([0 for i in range(8)])


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # 이미 hash_address에 데이터가 저장되어 있을 때
    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            # 0이 아니라면 순회 (다음 인덱스, 다음 인덱스로)
            # 비어 있다면 채워줘 (post)
            if hash_table[index] == 0:
                hash_table[index] = [index_key, value]
                return
            # key 가 동일하다면, 덮어써줘 (update)
            elif hash_table[index] == index_key:
                hash_table[index][1] = value
                return
    #
    else:
        hash_table[hash_address] = [index_key, value]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(hash_address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == index_key:
                return hash_table[index][1]
    else:
        return None


print(hash('dk'))
print(hash('da'))

print(hash('dk') % 8)
print(hash('da') % 8)
print(hash('dc') % 8)
print(hash('dd') % 8)

save_data('dk', '01200123123')
save_data('da', '3333333333')
save_data('dc', '1241414141')
read_data('da')
read_data('dc')

print('hash_table:', hash_table)

# hash_table: [0, 0, [2138854786694716122, '3333333333'], [
#    483009317306593203, '01200123123'], [9016252590445913508, '1241414141'], 0, 0, 0]
