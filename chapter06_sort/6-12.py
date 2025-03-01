# 두 배열의 원소교체
# n = 배열 길이
# k = 교체 가능한 횟수

n, k = map(int, input().split())

arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))

# for i in range(k):
#     x = arr_1.index(min(arr_1))
#     y = arr_2.index(max(arr_2))
#     arr_1[x], arr_2[y] = arr_2[y], arr_1[x]


# 정렬 사용하여 풀기

arr_1 = sorted(arr_1)
arr_2 = sorted(arr_2, reverse=True)

for i in range(k):
    if arr_1[i] < arr_2[i]:
        arr_1[i], arr_2[i] = arr_2[i], arr_1[i]

print(sum(arr_1))
