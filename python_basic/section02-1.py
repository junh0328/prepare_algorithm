# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
print('hello world!')
print("hello world!")
print("""hello world!""")
print('''hello world!''')


print()

# Separator 옵션 사용 (sep에 해당하는 문자열을 바탕으로 합쳐주겠다)

print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='')
print('2019', '02', '19')
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')

# end 옵션 사용 (끝을 내지 않겠다)
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')

print()

# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))

# index처럼 0 , 1 각 자리에 위치한 문자열을 매핑(할당)한다 >> You and Me and You
print('{0} and {1} and {0}'.format('You', 'Me'))

# 매개변수에 값을 넣어주는 형태로 더욱 직관적으로 사용할 수 있다. >> You and Me
print("{a} are {b}".format(a='You', b='Me'))

# format 함수를 쓰고 싶지 않고, 문자열 또는 정수, 실수를 나타내고 싶다면? 아래와 같은 방법으로 사용 가능하다
# %s: 문자, %d: 정수, %f: 실수
print("%s's favorite number is %d" % ('junhee', 7))

# %와 문자 또는 숫자를 나타내는 [ s, d, f ] 사이에 숫자를 넣으면, 최대 자릿수를 정해줄 수 있다
print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))

# print() 시에 'you'를 표현하고 싶은 경우 쌍이 맞거나, 이스케이프 코드를 사용할 수 있다
print("'You'")

print('\'You\'')

print('"You"')

print("""'You'""")

print('\\yout\\\n')  # 다르다

print('test')

print('\t tab 2')

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""
