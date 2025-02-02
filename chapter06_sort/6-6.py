# 계수 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array)+1)

for i in range(len(array)):
    # array[0] = 7
    # count = [0, 0, 0, ... 7번째가 +1]
    count[array[i]] += 1

for i in range(len(count)):
    # i = 0
    for j in range(count[i]):
    # count[3] 몇개?
    
        print(i, end=' ')

for i in range(len(count)):
    # i = 0
    # i = 3
    for j in range(count[i]):
    # count[0] = 값
    # for j in range(2):
    # for j in range(1):
    
        print(i, end=' ')
