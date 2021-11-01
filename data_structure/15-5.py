# 충돌 해결 알고리즘
# Chaining 기법
# Open Hahshing 기법
# With SHA256

import hashlib

hash_table = list([0 for i in range(8)])


def get_key(data: str):
    hash_object = hashlib.sha256()
    hash_object.update(data.encode())
    hex_dig = hash_object.hexdigest()
    print()
    print('sha256:', int(hex_dig, 16))  # 16진수를 10진수로 변환
    return int(hex_dig, 16)


def hash_function(key):
    return key % 8


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        hash_table[hash_address].append([index_key, value])
    else:
        hash_table[hash_address] = [[index_key, value]]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            if hash_table[hash_address][index][0] == index_key:
                return hash_table[hash_address][index][1]
        return None
    else:
        return None


# print(get_key('db') % 8)
# print(get_key('da') % 8)
# print(get_key('dh') % 8)


save_data('da', '01200123123')
save_data('dh', '3333333333')

print()
print()

print('read_data("dh"):', read_data('dh'))
print('read_data("da"):', read_data('da'))

print()
print()

print('hash_table:', hash_table)

# hash_table: [
# 0, 0,
# [[77049896039817716104633086125973601665927154587286664305423403838091909979274, '01200123123'], [25902807790238191969936164090115518991880572428612380032453909518048593055890, '3333333333']],
# 0, 0, 0, 0, 0
# ]
