# Section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

# DB 사용을 위한 패키지 import
import sqlite3

# DB 생성(파일)

conn = sqlite3.connect(
    '/Users/leejunhee/FastCampus/python_basic/resource/database.db')

# 해당 경로애 있는 db 파일 DB Brwoser for SQLite로 열기

# Cursor 연결
c = conn.cursor()

# 데이터 수정 1 (기본적인 형태로 수정하기 SQL 문법)
# c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 2))

# 데이터 수정 2 (딕셔너리 형태로 수정하기)
# c.execute("UPDATE users SET username = :name WHERE id = :id",
#           {"name": 'goodman', "id": 3})

# # 데이터 수정 3
# c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 4))

# 중간 데이터 확인 1

for user in c.execute("SELECT * FROM users"):
    print('user1:', user)


# 데이터 삭제 1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# 데이터 삭제 2 (딕셔너리 형태로 삭제하기)
c.execute("DELETE FROM users WHERE id = :id", {"id": 3})

# 데이터 삭제 3
c.execute("DELETE FROM users WHERE id = '%s'" % (4))
# c.execute("DELETE FROM users WHERE id = '%s'" % 4) >>> 튜플이 하나일 경우에는 소괄호를 적지 않아도 된다

print()

# 중간 데이터 확인 2

for user in c.execute("SELECT * FROM users"):
    print('user2:', user)

# 테이블 전체 데이터 삭제
print("user db deleted :", conn.execute("DELETE FROM users").rowcount, " rows")

# 커밋 : DB(SQLite)에 반영하기
conn.commit()

# 접속 해제
conn.close()
