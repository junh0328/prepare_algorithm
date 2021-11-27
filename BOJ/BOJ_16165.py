# 문제 제목: 걸그룹 마스터 준석이

# https://www.acmicpc.net/problem/16165


N, M = map(int, input().split())

team_mem, mem_team = {}, {}

for i in range(N):
    team_name, mem_num = input(), int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

print('team_mem:', team_mem)
print('mem_team:', mem_team)

for i in range(M):
    name, q = input(), int(input())
    # q가 1일때 (참일 때)
    if q:
        print(mem_team[name])
    # q가 1일이 아닐 때(거짓일 때)
    else:
        for mem in sorted(team_mem[name]):
            print(mem)


# team_mem: {'twice': ['jihyo', 'dahyeon', 'mina', 'momo', 'chaeyoung', 'jeongyeon', 'tzuyu', 'sana', 'nayeon'], 'blackpink': ['jisu', 'lisa', 'rose', 'jenny'], 'redvelvet': ['wendy', 'irene', 'seulgi', 'yeri', 'joy']}
# mem_team: {'jihyo': 'twice', 'dahyeon': 'twice', 'mina': 'twice', 'momo': 'twice', 'chaeyoung': 'twice', 'jeongyeon': 'twice', 'tzuyu': 'twice', 'sana': 'twice', 'nayeon': 'twice', 'jisu': 'blackpink', 'lisa': 'blackpink', 'rose': 'blackpink', 'jenny': 'blackpink', 'wendy': 'redvelvet', 'irene': 'redvelvet', 'seulgi': 'redvelvet', 'yeri': 'redvelvet', 'joy': 'redvelvet'}


# 3 4
# twice
# 9
# jihyo
# dahyeon
# mina
# momo
# chaeyoung
# jeongyeon
# tzuyu
# sana
# nayeon
# blackpink
# 4
# jisu
# lisa
# rose
# jenny
# redvelvet
# 5
# wendy
# irene
# seulgi
# yeri
# joy
# sana
# 1
# wendy
# 1
# twice
# 0
# rose
# 1
