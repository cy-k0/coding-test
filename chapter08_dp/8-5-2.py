# 1로 만들기
# 정수 x 가 주어지면 아래의 네가지 연산을 적절히 사용하여 정수 x를 1로 만든다
# x 가 5 로 나누어 떨어지면 5 로 나눈다
# x 가 3 으로 나누어 떨어지면 3 으로 나눈다
# x 가 2 로 나누어 떨어지면 2 로 나눈다
# x 에서 1을 뺀다
# 연산을 사용하는 횟수의 최솟값을 출력

# 바텀업 방식의 다이나믹 프로그래밍 시도

x = int(input())

d = [0] * 10000

for i in range(2, x+1):
    d[i] = d[i - 1] + 1

    if d[i] % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    
    if d[i] % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    
    if d[i] % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[x])