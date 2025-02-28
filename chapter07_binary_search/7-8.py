# 떡볶이 떡 만들기
# 떡의 개수 N , 요청한 떡의 길이 M
# N 개의 떡의 개별 길이가 둘째 줄
# target = 잘린 떡의 합과 같아야함


# def binary_search(array, target, start, end):
#     while start <= end:
#         total = 0
#         mid = (start + end) // 2
#         for x in array:
#             if x > mid:
#                 total += x - mid

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0

end = max(array)

result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)


