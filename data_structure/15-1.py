print(hash('Dave'))

# 1. 리스트 컴프리헨션으로 각 방이 0으로 초기화된 배열을 만든다

hash_table = list([0 for i in range(8)])

print('hash_table:', hash_table)
# hash_table: [0, 0, 0, 0, 0, 0, 0, 0]

print()
print()


def get_key(data):
    return hash(data)


def hash_function(key):
    return key % 8


def save_data(data, value):
    hash_address = hash_function(get_key(data))
    hash_table[hash_address] = value


def read_data(data):
    hash_address = hash_function(get_key(data))
    return hash_table[hash_address]


print(save_data('Dave', '0102030200'))
print(save_data('Andy', '01033232200'))

print('hash_table:', hash_table)
# hash_table: [0, 0, 0, '01033232200', 0, 0, 0, '0102030200']

print(read_data('Dave'))
# 0102030200
