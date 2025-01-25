# 500원 100원 50원 10원이 무한히 존재한다고 가정
# 거스름돈이 N원일 때, 거슬러줘야 할 동전의 최소 개수를 구하라

def solution(n):
    count = 0
    
    coins = [500, 100, 50, 10]

    for c in coins:
        count += n // c
        n %= c
    
    return count


if __name__ == "__main__":
    n = int(input("거스름돈 : "))
    print(f"동전 최소 개수 : {solution(n)}")
