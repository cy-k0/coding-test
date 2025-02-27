# 부품찾기
# N 개의 물품 보유, [0, 1, 2, ... , N]
# 고객이 찾는 M 개의 물품 확인 [5, 7, 9]
# 보유하고 있는 물품에 대해 yes, 아닌 물품에 대해 no 출력

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 가게 부품 개수 및 보유 상품
n = int(input())
array = list(map(int, input().split()))

# 손님이 찾는 물품 개수
m = int(input())
target_array = list(map(int, input().split()))

for i in target_array:
    result = binary_search(array, i, 0, n - 1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
