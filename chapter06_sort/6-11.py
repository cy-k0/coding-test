# 성적 낮은 학생 순으로 출력

n = int(input())

array = []

for i in range(n):
    score_list = input().split()

    name, score = score_list[0], score_list[1]

    array.append((name, int(score)))

array = sorted(array,  key=lambda s: s[1])

for i in range(len(array)):
    print(array[i][0], end=' ')


# for s in range(len(array)):
#     array[s]

# def lambdafunction(s):
#     return s[1]