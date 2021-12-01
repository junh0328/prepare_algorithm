S = input()

# 등호를 나타날 때
tmp, answer, check = "", "", False

for i in S:
    # case 1: 공백
    if i == ' ':
        # 등호가 닫혀있을 경우
        if not check:
            answer += tmp[::-1] + " "
            tmp = ""
        # 등호가 열려있을 경우
        else:
            answer += " "

    # case 2: 등호
    elif i == '<':
        check = True
        answer += tmp[::-1] + "<"
        tmp = ""
    elif i == '>':
        check = False
        answer += ">"

    # 알파벳 또는 숫자
    else:
        if check:
            answer += i
        else:
            tmp += i

answer += tmp[::-1]
print(answer)
