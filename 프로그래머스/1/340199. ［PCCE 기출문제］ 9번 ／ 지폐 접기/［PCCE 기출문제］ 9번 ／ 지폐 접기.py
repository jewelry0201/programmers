def fold_count(wallet, bill):
    count = 0
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        if bill[0] >= bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        count += 1
    return count

def solution(wallet, bill):
    # 두 방향으로 접기
    fold_normal = fold_count(wallet, bill[:])  # 그대로의 방향
    fold_rotated = fold_count(wallet, bill[::-1])  # 90도 회전 방향

    # 최소 접기 횟수를 반환
    return min(fold_normal, fold_rotated)

# 테스트 케이스
wallet = [50, 50]
bill = [100, 241]

result = solution(wallet, bill)
print(result)  # 예상 출력: 4
