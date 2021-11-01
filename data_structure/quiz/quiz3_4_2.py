def hash_func(key):
    return ord(key[0]) % 10


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class HashTable:
    def __init__(self):
        self.table = [None]*10

    def set(self, key, value):
        self.table[hash_func(key)] = value

    def get(self, key):
        return self.table[hash_func(key)]

# 상속 받아야 하는 상황
# 오버라이딩으로 구현


class ChainedHashTable(HashTable):

    def __init__(self):
        self.table = [0]*10

    def set(self, key, value):
        hash_address = hash_func(key)
        if self.table[hash_address] != 0:
            for index in range(len(self.table[hash_address])):
                if self.table[hash_address][index][0] == key:
                    self.table[hash_address][index][1] = value
                    return
            self.table[hash_address].append([key, value])
        else:
            self.table[hash_address] = [[key, value]]

# Test code


ht = ChainedHashTable()


ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)


print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
print()

# ht.set('hello2', 5)

# print(ht.get('hello'), end=' ')
# print(ht.get('hello2'), end=' ')
# print(ht.get('hello3'), end=' ')
# print(ht.get('hello4'), end=' ')

print()

print(ht.__dict__)
