# 선택 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    # print(array[i], array[min_index])
    array[i], array[min_index] = array[min_index], array[i] # 스와프

    # print(array[i], array[min_index])


print(array)