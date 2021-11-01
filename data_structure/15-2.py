# 충돌 해결 알고리즘
# Chaining 기법
# Open Hahshing 기법

hash_table = list([0 for i in range(8)])

# 해쉬 키 생성


def get_key(data):
    return hash(data)

# 해쉬 함수


def hash_function(key):
    return key % 8

# save_data(data, value): 데이터 저장하기 ('dave', '01011112222')
# 1. dave라는 문자열을 바탕으로 해쉬 키를 생성한다
# 2. 해쉬키를 바탕으로 해쉬 함수에 넣어 개별 해쉬 테이블의 해쉬 주소를 생성한다
# 3. 해쉬 테이블의 해당 주소를 바탕으로 'value'를 저장한다

# 링크드 리스트에 있어서 해당 주소에는 value값만 저장되어 있으므로 뭐가 내가 찾고자하는 자료인지 헷갈릴 수 있다
# 이에 따라 이를 구분하기 위해 🔥 index_key 🔥라는 변수를 생성하였다


def save_data(data, value):
    index_key = get_key(data)
    hash_address = hash_function(index_key)
    # hash_table = list([0 for i in range(8)]) 리스트 컴프리헨션에 의해 초기값을 0으로 두었음
    # 해당 값이 0이 아니라는 뜻은 해쉬테이블 해당 주소에 value가 저장되어 있다는 의미이다
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            # key 값이 같은 게 존재할 경우
            if hash_table[hash_address][index][0] == index_key:
                hash_table[hash_address][index][1] = value
                return
        # key 값이 같은 것이 존재하지 않을 경우 지금의 key와 value를 해당 주소에 append(뒤에 추가한다)
        # [
        #    0: [[index_key],[value]],
        #    1: [[index_key],[value]],
        #    2: [[index_key],[value]],
        #    ...
        # ]
        hash_table[hash_address].append([index_key, value])
    else:
        #  if hash_table[hash_address] == 0 이라면 (비어있다면) 해쉬 테이블에 삽입한다
        hash_table[hash_address] = [[index_key, value]]


def read_data(data):
    index_key = get_key(data)
    hash_address = hash_function(index_key)

    # 0이 아니라면, 데이터가 저장되어 있다면?
    if hash_table[hash_address] != 0:
        for index in range(len(hash_table[hash_address])):
            # 배열을 순회한다
            if hash_table[hash_address][index][0] == index_key:
                # 찾고자 하는 value를 리턴한다
                return hash_table[hash_address][index][1]
        # 링크드 리스트는 있었는데 키에 해당하는 값이 없을 경우에는 없다고 리턴한다
        return None
    else:
        return None
