# 개미전사
# 식량창고의 개수 n
# 각 식량창고의 식량 개수 k (array)
# 인접한 식량창고는 털 수 없다 (1, 2, 3, 4 -> 1을 터는 경우 2를 털 수 x)
# 얻을 수 있는 식량의 최대값 출력

n = int(input())
k = list(map(int, input().split()))

def get_larger_sum(num, array):
    zero_from_sum = 0
    for i in range(0, num, 2):
        zero_from_sum += array[i]
    
    one_from_sum = 0
    for i in range(1, num, 2):
        one_from_sum += array[i]

    return max(zero_from_sum, one_from_sum)

print(get_larger_sum(n, k))