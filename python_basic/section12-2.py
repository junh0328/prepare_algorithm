# Section12-2
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect(
    '/Users/leejunhee/FastCampus/python_basic/resource/database.db')  # 본인 DB 경로

# (마우스) 커서 바인딩 (Cursor Binding)
c = conn.cursor()

# 데이터 조회 (전체)
c.execute("SELECT * from users")

# 커서 위치가 변경
# 1개 로우 선택

# print('One row -> \n', c.fetchone())
# One row -> (1, 'LEE', 'junh0328@naver.com', '010-9170-1796', 'https://github.com/junh0328', '2021-10-22 11:48:15')

# 지정 로우 선택
# print('Three => \n', c.fetchmany(size=3))  # >>> 배열 형태로 로우 printing

# [
# (2, 'Park', 'Park@daum.net', '010-1111-1111', 'park.com', '2021-10-22 11:48:15'),
# (3, 'Cho', 'cho@naver.com', '010-2222-2222', 'cho.com', '2021-10-22 11:48:15'),
# (4, 'kim', 'kim@naver.com', '010-2222-2222', 'kim.com', '2021-10-22 11:48:15')
# ]

# 전체 로우 선택
# print('All -> \n', c.fetchall())
# 남은 데이터를 리스트 형태로 가져옴 but, 현재 db에 5개만 저장했으므로 마지막 하나를 가져오는 결과

# >>> [(5, 'Paik', 'Paik@naver.com', '010-2222-2222', 'paik.com', '2021-10-22 11:48:15')]

# 만약 커서가 마지막 로우를 가리키는데 다시 로우를 불러온다면?
# print('All -> \n', c.fetchall())

# 빈 배열을 가져온다
# >>> All -> []


# DB 순회 1

# rows = c.fetchall()
# for row in rows:
#     print('SELECT 1 >>>', row)

# DB 순회 2
# for row in c.fetchall():
#     print('SELECT2 >>>', row)

# DB 순회 3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('SELECT3 >>>', row)

# 보통 순회 2번을 많이 쓴다

print()

# WHERE Retrieve1
# 튜플 형식으로 가져오기
param1 = (3,)
c.execute('SELECT * FROM users WHERE id = ?', param1)
print('param1', c.fetchone())

# 3번 데이터는 하나이기 때문에 3번에 대한 데이터는 더 없으므로 빈 배열을 출력하게 된다
print('param1', c.fetchall())  # 데이터 없음

print()

# WHERE Retrieve2
# 정수형으로 가져오기
param2 = 4
c.execute('SELECT * FROM users WHERE id = "%s"' % param2)  # %s, %f, %d
print('param2', c.fetchone())
print('param2', c.fetchall())  # 데이터 없음

print()

# WHERE Retrieve3
# 딕셔너리로 가져오기
c.execute('SELECT * FROM users WHERE id =:Id', {"Id": 5})
print('param3', c.fetchone())
print('param3', c.fetchall())  # 데이터 없음

print()

# WHERE Retrieve4
param4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())  # 데이터 없음

print()

# WHERE Retrieve5
# c.execute("SELECT * FROM users WHERE id IN(?,?)", (3, 5))
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (3, 5))
print('param5', c.fetchall())  # 데이터 없음


print()

# WHERE Retrieve6 (딕셔너리 형태)

c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 2, "id2": 5})
print('param6', c.fetchall())  # 데이터 없음

print()

# Dump 출력
# DB 에 저장한 명령어 (SELECT, DELETE, CREATE, ...) 를 백업해두는 것
# >>> 현 폴더에서 dump.sql로 생성

with conn:
    with open('/Users/leejunhee/FastCampus/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')

# f.close(), conn.close() 함수가 with문으로 인해 작성하지 않더라도 자동으로 동작한다