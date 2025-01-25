# 왕실의 나이트
# 나이트의 현재 좌표에 따라, 움직일 수 있는 경우의 수
# x, y = 'a ~ h', '1 ~ 8'

target = input()

x, y = target[0], int(target[1])

# x가 "a", "b", "h", "g"일 때 경우의 수를 정의
if x in ["a", "h"]:
    if y in range(3, 7):
        answer = 4
    elif y in [1, 8]:
        answer = 2
    elif y in [2, 7]: 
        answer = 3
elif x in ["b", "g"]:
    if y in range(3, 7):
        answer = 6
    elif y in [1, 8]:
        answer = 3
    elif y in [2, 7]:
        answer = 4
else:  
    # x가 "c", "d", "e", "f"인 경우
    if y in range(3, 7):
        answer = 8
    elif y in [1, 8]:
        answer = 4
    elif y in [2, 7]:
        answer = 6

print(answer)
