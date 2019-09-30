def solution(heights):
    answer = []
    length = len(heights)
    idx = -1
    while len(heights) > 1:
        sender = heights[idx]
        heights.pop(idx)
        if max(heights) <= sender:
            answer.extend([0])
        else:
            for i in range(-1, -1*len(heights)-1, -1):
                if heights[i] > sender:
                    answer.extend([i + length - len(answer)])
                    break
    answer.extend([0])
    answer.reverse()
    return answer


a = [3, 9, 9, 3, 5, 7, 2]
res = solution(a)
print(res)