# stack 구현 -> 후입선출
# Key point : 배열에 append 를 사용해 원소를 추가하면 기존 배열 뒤로 붙는다는 것 / pop을 사용해 원소 삭제 시, 마지막 원소가 삭제된다는 것

# 5 - 2 - 3 - 7 - 삭제 - 1 - 4 삭제

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)