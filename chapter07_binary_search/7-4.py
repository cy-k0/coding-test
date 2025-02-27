# input은 시간초과 이슈 있을 수 있으므로 대용량 데이터를 입력받을 땐, sys readline사용
# 이때 rstrip()은 꼭 해줘야함
# 입력 후 엔터가 줄바꿈 기호로 입력되는데 이를 제거해야함

import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)