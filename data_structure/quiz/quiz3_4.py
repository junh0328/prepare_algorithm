# 과제 4번 코드란


def hash_func(key):
    return ord(key[0]) % 10


class HashTable:
    def __init__(self):
        self.table = [None]*10

    def set(self, key, value):
        self.table[hash_func(key)] = value

    def get(self, key):
        return self.table[hash_func(key)]


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class ChainedHashTable(HashTable):

    def set(self, key, value):
        # 해쉬 키 생성 및 초기화
        index_key = hash(key)
        # 해쉬 주소 고유값 생성 및 초기화
        hash_address = hash_func(index_key)

        if self.table[hash_address] != 0:
            for index in range(len(self.table[hash_address])):
                if self.table[hash_address][index][0] == index_key:
                    self.table[hash_address][index][1] = value
                    return

            self.table[hash_address].append([index_key, value])
        else:
            self.table[hash_address] = [[index_key, value]]

    def get(self, key):
        index_key = hash(key)
        hash_address = hash_func(index_key)

        if self.table[hash_address] != 0:
            for index in range(len(self.table[hash_address])):
                if self.table[hash_address][index][0] == index_key:
                    return self.table[hash_address][index][1]
            return None
        else:
            return None


# Test code

ht = ChainedHashTable()

print('ht:', ht.__dict__)
# ht: {'table': [None, None, None, None, None, None, None, None, None, None]}

print()
print()

ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)

print('ht:', ht.__dict__)
# ht: {'table': [None, None, None, None, 4, None, None, None, None, None]}
# 다 같은 index 4 자리에 들어간 것으로 보임

print()
print()

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')

print()
print()

ht.set('hello2', 5)

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
