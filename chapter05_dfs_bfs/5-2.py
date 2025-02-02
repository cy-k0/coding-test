# queue 구현 -> 선입선출(공정한 자료구조)
# Key point : deque 라이브러리(양쪽에 모두 출입구를 가지고 있는 파이썬 자료구조), popleft()을 이용하여 1번 인덱스 원소부터 제거하기
# deque 자료구조 -> 첫, 끝 데이터에 접근하는 게 굉장히 빠르므로 삭제와 추가가 자주 일어나는 경우 사용하면 좋음

# 5 - 2 - 3 - 7 - 삭제 - 1 - 4 - 삭제
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

queue.reverse()

print(queue)
