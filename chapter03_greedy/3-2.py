# 배열 크기 n
# 숫자 더하는 횟수 m
# 연속으로 쓸 수 있는 최대 수 k

n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data = data[:n]
data = sorted(data)

answer = 0

while True:
    for i in range(k):
        if m == 0:
            break
        answer += data[n-1]        
        m -= 1
    if m == 0:
        break
    answer += data[n-2]
    m -= 1

print(answer)
    

# if __name__=='__main__':
#     print('n', n)
#     print('data', data)