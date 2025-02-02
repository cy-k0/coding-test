# 2가지 방식으로 팩토리얼 구현

# 정석대로 구현
def factorial_iterative(n):
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer

# 재귀 함수 구현
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_iterative(5))
print(factorial_recursive(5))



