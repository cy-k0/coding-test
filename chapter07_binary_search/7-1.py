# 순차탐색 찾고자 하는 문자열 인덱스 반환


def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1


input_data = input().split()
n = int(input_data[0])
target = input_data[1]
array = input().split()

print(sequential_search(n, target, array))