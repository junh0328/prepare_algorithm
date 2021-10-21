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

# DB 생성 & Auto Commit (반영) / Rollback (되돌리기)

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
