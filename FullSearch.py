def solution(answers):
    numb_prob = len(answers)
    if numb_prob%5 is 0:
        k = int(numb_prob/5)
    else:
        k = int(numb_prob/5) + 1
    numb_1 = ([1,2,3,4,5] * k)[:numb_prob]
    numb_2 = ([2,1,2,3,2,4,2,5] * k)[:numb_prob]
    numb_3 = ([3,3,1,1,2,2,4,4,5,5] * k)[:numb_prob]

    def matching(numb, ans):
        answers = 0
        for idx, ele in enumerate(numb):
            if ele == ans[idx]:
                answers += 1
        return answers

    answer_1 = matching(numb_1, answers)
    answer_2 = matching(numb_2, answers)
    answer_3 = matching(numb_3, answers)

    answer = [answer_1, answer_2, answer_3]
    maximum = max(answer)

    return [i+1 for i, j in enumerate(answer) if j == maximum]

answer = [1,2,3,4,5]
res = solution(answer)