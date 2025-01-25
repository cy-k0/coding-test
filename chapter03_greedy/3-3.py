# r, c = 행, 열
# Condition 1 : 뽑을 수 있는 가장 큰 수가 답안
# Condition 2 : 카드를 뽑을 행 선택 후, 해당 행에서 가장 작은 수 뽑기

r, c = map(int, input().split())

answer = 0

for i in range(r):
    data = list(map(int, input().split()))
    data = data[:c]
    print(data)
    if answer < min(data):
        answer = min(data)

print(answer)
