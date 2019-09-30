def solution(n, lost, reserve):
    whole = list(range(1, n + 1))
    lost1 = list(lost)
    for loser in lost1:
        if loser in reserve:
            reserve.remove(loser)
            lost.remove(loser)
    for loser in lost:
        if loser - 1 in reserve:
            reserve.remove(loser - 1)
        elif loser + 1 in reserve:
            reserve.remove(loser + 1)
        else:
            whole.remove(loser)

    answer = len(whole)
    return answer


n = 5
lost = [2,3,4]
reserve = [3,4,5]

solution(n, lost, reserve)