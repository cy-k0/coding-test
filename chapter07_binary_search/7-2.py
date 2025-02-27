# 이진탐색 : 반으로 쪼개면서 탐색하기 (배열 내부 데이터가 정렬되어있다고 하면 효율적)

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


# n : 원소의 개수, target : 찾고자 하는 문자열
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("찾는 원소가 배열 내에 존재하지 않습니다")
# 몇번째 숫자인지 출력해야하므로 idx + 1
else:
    print(result + 1)