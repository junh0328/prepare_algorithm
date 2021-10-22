# Sectino12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now:', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime:', nowDatetime)

# sqlite3
print('sqlite3.version :', sqlite3.version)
print('sqlite3.sqlite_version: ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit (반영), isolation_level = None / Rollback (되돌리기)

conn = sqlite3.connect(
    '/Users/leejunhee/FastCampus/python_basic/resource/database.db', isolation_level=None)

# Cursor

c = conn.cursor()

print('Cursor Type:', type(c))
# print('Cursor Type:', dir(c))

# 테이블 생성(Data Type: TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
# ? (물음표)로 처리된 데이터는 뒤에 튜플 형식으로 추가해줘야 한다
c.execute("INSERT INTO users VALUES(1, 'LEE', 'junh0328@naver.com', '010-9170-1796', 'https://github.com/junh0328', ?)", (nowDatetime,))

# 정석적인 데이터 삽입구조
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
          (2, 'Park', 'Park@daum.net', '010-1111-1111', 'park.com', nowDatetime))

# Many 삽입 (많은 데이터를 한번에 삽입하기) (튜플, 리스트 형태로 삽입하기)

userList = (
    (3, 'Cho', 'cho@naver.com', '010-2222-2222', 'cho.com', nowDatetime),
    (4, 'kim', 'kim@naver.com', '010-2222-2222', 'kim.com', nowDatetime),
    (5, 'Paik', 'Paik@naver.com', '010-2222-2222', 'paik.com', nowDatetime),
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
    VALUES (?,?,?,?,?,?)", userList)

# 테이블 데이터 삭제
# rowcount를 통해 몇개의 데이터가 들어가있는지 확인할 수 있다.

# conn.execute("DELETE FROM users")
# print('users db deleted:', conn.execute(
#     "DELETE FROM users").rowcount)  # >>> users db deleted: 5

# 커밋 (DB에 추가) : isolation_level = None 일 경우 자동으로 반영한다
# conn.commit()

# 롤백 : 커밋한 데이터 되돌리기(없애기)
# conn.rollback()

# 접속 해제
conn.close()

print('conn.closed:', conn.close())
