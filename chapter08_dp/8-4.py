# 파보나치 수열 바텀업 방식(8-2는 탑다운)

d = [0] * 100

d[1] = 1
d[2] = 1

n = 99

for i in range(3, n+1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])
