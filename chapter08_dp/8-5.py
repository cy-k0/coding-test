# 1로 만들기
# 정수 x 가 주어지면 아래의 네가지 연산을 적절히 사용하여 정수 x를 1로 만든다
# x 가 5 로 나누어 떨어지면 5 로 나눈다
# x 가 3 으로 나누어 떨어지면 3 으로 나눈다
# x 가 2 로 나누어 떨어지면 2 로 나눈다
# x 에서 1을 뺀다
# 연산을 사용하는 횟수의 최솟값을 출력

# greedy 사용하여 풀이

x = int(input())
count = 0

while x > 1:
    if x % 5 == 0:
        x = x // 5
        count += 1
    elif (x - 1) % 5 == 0:
        x = (x - 1) // 5
        count += 2
    elif x % 3 == 0:
        x = x // 3
        count += 1
    elif (x - 1) % 3 == 0:
        x = (x - 1) // 3
        count += 2 
    elif x % 2 == 0:
        x = x // 2
        count += 1
    else:
        x = x - 1
        count += 1

print(count)