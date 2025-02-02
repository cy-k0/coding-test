# 재귀함수 -> 함수 안에서 다시 해당 함수 호출
# Key point :  종료조건 명시

def recursive_function(i):
    if i == 10:
        print('재귀 함수 종료')
        return
    print(i, '번째 함수에서', i+1, '번째 재귀 함수를 호출')
    recursive_function(i+1)

recursive_function(1)