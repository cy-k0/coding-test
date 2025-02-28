# 효율적인 화폐구성
# n, m => n개의 화폐 가치 입력받음, m은 만들어야하는 금액
# n종류의 화폐를 이용하여 m원을 만드는 최소 횟수
# 불가능할 경우 -1 출력

n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(int(input()))

array = sorted(array)

count = 0

while m > 0:    
    # 현재 남은 금액보다 작거나 같은 가장 큰 화폐 찾기
    largest_possible = -1

    # 역순으로 0 까지 거꾸로
    for i in range(n-1, -1, -1):
        if array[i] <= m:
            largest_possible = array[i]
            break
    
    # 만들 수 없는 경우
    if largest_possible == -1:
        count = 0
        break
    
    # 현재 가능한 제일 큰 화폐로 빼기
    m -= largest_possible
    count += 1

if count != 0:
    print(count)
else:
    print(-1)