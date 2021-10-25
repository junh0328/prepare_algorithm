# Format 형식 출력

# 튜플 형식 (,) 으로 입력해준다

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
# 4를 붙이지 않고도 사용이 가능
print("Test1: {0:5d}, Price: {1:.2f}".format(776, 6534.123))
print("Test1: {a:5d}, Price: {b:4.2f}".format(a=776, b=6534.123))

print()
print()

a = 'nice man'
b = 'good boy'
c = 'nice man   '
d = '000000000text0000000'

print(a.endswith('n'))
print(a.capitalize())
print('c:', c, end='')

# strip() >>> 뒤에오는 공백 제거
print(c.strip())

# strip('문자열') >>> 해당 문자열 제거
print(d.strip('0'))
