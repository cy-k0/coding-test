# 계수 정렬을 활용한 부품찾기
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트 만들고 인덱스에 직접 접근하여 특정 번호의 부품이 존재하는지 확인하면 됨

n = int(input())

array = [0] * 1000

for i in input().split():
    array[int(i)] = 1

m = int(input())
target_array = list(map(int, input().split()))

for x in target_array:
    if array[x] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")