import numpy as np

def solution(priorities, location):

    zip_ = list(zip(priorities, np.arange(len(priorities))))
    zip_max = max(zip_)[0]

    pool = []
    idx = 0
    while len(zip_) != 0:
        temp = zip_[0]
        if temp[0] is zip_max:
            zip_.pop(0)
            pool.append(temp)
            try:
                zip_max = max(zip_)[0]
            except:
                break
        else:
            zip_.pop(0)
            zip_.append(temp)

    idx = 1
    for ele in pool:
        if ele[1] == location:
            return idx
        idx += 1

    return 0

a = [1,1, 9, 1,1,1]
# a.sort()
res = solution(a, 0)
print(res)