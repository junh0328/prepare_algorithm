# SHA-1

import hashlib

data = 'text'.encode()  # encode(): byte로 바꿔준다는 의미
hash_object = hashlib.sha1()
hash_object.update(data)
# hash_object.update(b'test') 와 같이 사용도 가능
hex_dig = hash_object.hexdigest()
print('sha1:', hex_dig)
# sha1: 372ea08cab33e71c02c651dbc83a474d32c676ea

print()
print()

# SHA-256

data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)
print('sha256:', hex_dig)
# sha256: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

# 만들어진 hash 데이터를 바탕으로 원래의 값을 추론할 수 없기 때문에 안전하다
