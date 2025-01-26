# 게임개발
# 현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 갈 곳을 정함 (북, 동, 남, 서)
# 캐릭터 바로 왼쪽 방향에 아직 가보지 않은 칸이면 한칸 전진 (왼쪽으로 도니까)
# 가본 칸이면 다시 1 수행
# 만약 네 방향이 모두 가본 방향이거나, 바다라면 멈춤
# 바다는 1 / 육지는 0

'''
4 4     4 x 4 맵
1 1 0   (1, 1) 에 북쪽을 바라보고 있는 캐릭터
1 1 1 1 
1 0 0 1
1 1 0 1
1 1 1 1 
'''

# 맵 크기 입력
map_x, map_y = map(int, input().split())

# 캐릭터 위치, 방향 입력 
x, y, d = map(int, input().split())

# 방향 정의 (북, 동, 남, 서)
direction = [0, 1, 2, 3]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 이동 방향 선택 함수
def select_direction(current_d):
  if current_d == 0:  # 북
    return 3  # 서쪽으로
  elif current_d == 1:  # 동
    return 0  # 북쪽으로
  elif current_d == 2:  # 남
    return 1  # 동쪽으로
  else:  # 서
    return 2  # 남쪽으로

# 지도 생성
game_map = []
for i in range(map_x):
  game_map.append(list(map(int, input().split())))

# 방문 영역 초기화
visited_area = []
start_area = (x, y)
visited_area.append(start_area)

# 바다 영역 방문처리
for i in range(map_x):
  for s in range(map_y):
    if game_map[i][s] == 1:
      visited_area.append((i, s))

# 방향 체크 및 이동 (시작 위치 생각해서 count 초기값 1로 설정)
count = 1
turn_count = 0
current_d = d

while True:
  new_d = select_direction(current_d)
  next_x = x + dx[new_d]
  next_y = y + dy[new_d]
  next_area = (next_x, next_y)
  
  if next_area not in visited_area:
    x, y = next_x, next_y
    visited_area.append(next_area)
    current_d = new_d
    count += 1
    # turn count 반드시 초기화
    turn_count = 0

  else:
    current_d = new_d
    turn_count += 1
  
  if turn_count == 4:
    back_x = x - dx[current_d]
    back_y = y - dy[current_d]
    back_area = (back_x, back_y)
    
    if back_area in visited_area:
      break
    else:
      x, y = back_x, back_y
      visited_area.append(back_area)
      turn_count = 0

print(count)
