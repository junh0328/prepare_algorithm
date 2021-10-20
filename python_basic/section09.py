# Section09
# 파일 읽기, 쓰기

# 읽기 모드 : r(read)
# 쓰기 모드(기존 파일 삭제 후 덮어 쓰기) : w(write)
# 추가 모드(파일 생성 또는 추가) : a(append)

# .. : 상대경로,
# . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제 1

from random import randint

f = open('./resource/review.txt', 'r')
content = f.read()
print(content)

print()
# f 변수에 할당된 인스턴스를 볼 수 있다
print(dir(f))

print()
# 반드시 close로 리소스를 반환해야 한다
f.close()

# 예제 2 (with 문 사용)
# with 문 사용 시, close()를 사용하지 않아도 요청이 종료된다

with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    # print(iter(c))

print()

# 예제 3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print()
print()

# 예제 4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print('>>> ', content)

    # 문서를 읽는 커서가 제일 밑으로 온 경우 더 이상 가져오지 않는다 (빈 내용을 가져온다)
    # 따라서 내용이 없다
    content = f.read()
    print('>>> ', content)

print()
print()

# 예제 5 (한 문장 단위로 읽어 올 때)
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end=' #### ')
        line = f.readline()

print()
print()

# 예제 6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end=' ****** ')

print()
print()

# 예제 7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('avg :{:6.3}'.format(sum(score)/len(score)))


print()
print()

# 파일 쓰기

# 예제 1 'w'
with open('./resource/test1.txt', 'w') as f:
    f.write('Nice man!\n')

# 예제 2 'a'
with open('./resource/test1.txt', 'a') as f:
    f.write('good man!\n')

# 예제 3

# from random import randint 랜덤 인트 만들기

with open('./resource/test2.txt', 'w') as f:
    for cnt in range(7):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제 4

# readlines : 리스트형태로 파일을 읽어오는 형태
# writelines : 리스트 -> 파일로 저장하는 형태
with open('./resource/test3.txt', 'w') as f:
    list = ['kim\n', 'park\n', 'lee\n']
    f.writelines(list)

# 예제 5

# 프린트 문으로 파일에 직접 문자열 적어주기
with open('./resource/test4.txt', 'w') as f:
    print('test Contents1!', file=f)
    print('test Contents2!', file=f)
