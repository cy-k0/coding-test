# n이 1이 될때까지 'n-1' or 'n/k' 반복 수행
# 연산 최소 횟수 구하기
# Condition 1 : 'n/k'는 나머지가 0이 될때만 사용할 수 있음 

n, k = map(int, input().split())

count = 0

while n >= k:
    if n % k != 0:
        n -= 1
        count += 1
    else:
        n //= k
        count += 1


# k보다 큰 경우는 이미 위에서 연산 끝남
while n > 1:
    n -= 1
    count += 1

print(count)

