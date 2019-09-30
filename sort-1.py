def solution(array, commands):
    answer = []
    for com in commands:
        i = com[0]
        j = com[1]
        k = com[2]
        sliced = array[i - 1:j]
        sliced.sort()
        pick = sliced[k - 1]
        answer.append(pick)

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

res = solution(array, commands)