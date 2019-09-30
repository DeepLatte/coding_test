
def solution(stock, dates, supplies, k): # 테스트 케이스에서 런타임에러 발생
    answer = 0
    while 1:
        if stock >= k:
            return answer
        temp_list = []
        i = 0
        while len(dates) != i:
            if dates[i] <= stock:
                temp_list.append(dates[i])
                i += 1
            else:
                break
        temp_sup = supplies[:int(len(temp_list))]
        stock += max(temp_sup)
        idx = supplies.index(max(temp_sup))
        supplies = supplies[idx+1:]
        dates = dates[idx+1:]
        answer += 1

    return answer
stock = 4
dates = [4,10,15]
supplies = [20,5,10]
k = 30
result = 2
res = solution(stock, dates, supplies, k)
print(res)