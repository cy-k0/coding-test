# 시각
# 정수 n : '00시 00분 00초 ~ n시 59분 59초' 까지 3이 들어가는 시각 모두 카운트
# 000000 ~ nn5959

n = int(input())

count = 0

for i in range(n+1):
    for m in range(60):
        for s in range(60):
            if "3" in str(i) + str(m) + str(s):
                count += 1
print(count)
 
