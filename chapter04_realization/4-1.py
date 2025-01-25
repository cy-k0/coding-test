# 상하좌우
# 시작 지점 (0, 0)
# 이동 가능 공간 n * n
# 명령어 L, R, U, D = 왼쪽(y - 1), 오른쪽(y + 1), 위(x - 1), 아래(x + 1)
# 공간을 벗어나는 명령은 무시

n = int(input())

x, y = 1, 1
move = input().split()

# L, R, U, D
mv_str = ["L", "R", "U", "D"]
mv_x = [0, 0, -1, 1]
mv_y = [-1, 1, 0, 0]

for mv in move:
    for i in range(len(mv_str)):
        if mv == mv_str[i]:
            a = x + mv_x[i]
            b = y + mv_y[i]
    if a < x or b < y or a > n or b > n:
        continue
    
    x, y = a, b

print(x, y)