# Section11

# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import pandas as pd
import csv  # csv 파일을 읽기 위해서는 파이썬에서 기본 제공하는 csv 패키지를 import 해야 한다

# 예제 1
# 인코딩 에러로 인한 인코드 인수 추가 https://zephyrus1111.tistory.com/39

with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.reader(f)
    # next(reader) Header (1행) 를 스킵한다

    # 확인
    print(reader)
    print(type(reader))

    print(dir(reader))
    print()

    for v in reader:
        print(v)

# 예제 2

with open('./resource/sample2.csv', 'r', encoding='euc-kr') as f:
    # reader = csv.reader(f) 없을 때 어떻게 보여지나 확인
    # delimiter=''를 통해 어떤 구분자로 구분되고 있나 적어준다
    reader = csv.reader(f, delimiter='|')
    # next(reader) Header (1행) 를 스킵한다

    # 확인
    print(reader)
    print(type(reader))

    print(dir(reader))
    print()

    for v in reader:
        print(v)

print()

# 예제 3 (Dict변환)
# Dictionary 형태로 가져오기 {'key':'value'}

with open('./resource/sample1.csv', 'r', encoding='euc-kr') as f:
    reader = csv.DictReader(f)
    for ele in reader:
        for k, v in ele.items():
            print(k, v)
        print('-----------------')

# 예제 4 (CSV 파일 쓰기)
# 순회하며 쓰기, for 문

w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open('./resource/sample3.csv', 'w', encoding='euc-kr', newline='') as f:
    # newline = '' enter가 두칸씩 들어가지 않도록 처리하겠다
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# 예제 5
# 한번에 쓰기 : writerows()

with open('./resource/sample4.csv', 'w', encoding='euc-kr', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w)

print()

# XSL, XLSX
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등이 있음
# pandas 를 주로 사용(openpyxl, xlrd)
# pandas 레퍼런스 https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html

# 해당 폴더의 가상환경 source ./activate 에서 설치해야 한다!

# pip install xlrd
# pip install openpyxl
# pip install pandas

# import pandas as pd >>> pandas 사용하기

# option
# sheetname='시트명' 또는 숫자, header = 3, skiprow = 숫자

xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인 (상위 5개)
print(xlsx.head())
print()

# 꼬리 데이터 확인 (하위 5개)
print(xlsx.tail())

# 데이터 확인
print(xlsx.shape)  # 행 , 열 >>> (20, 7)

# 엑셀 or CSV 파일로 다시 쓰기

xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
