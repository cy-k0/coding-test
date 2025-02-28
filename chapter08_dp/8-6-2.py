# 개미전사
# 식량창고의 개수 n
# 각 식량창고의 식량 개수 k (array)
# 인접한 식량창고는 털 수 없다 (1, 2, 3, 4 -> 1을 터는 경우 2를 털 수 x)
# 얻을 수 있는 식량의 최대값 출력

n = int(input())
k = list(map(int, input().split()))

d = [0] * 100

d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n-1])
