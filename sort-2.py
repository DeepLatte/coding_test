def solution(numbers):

    # str_numbers = list(map(lambda x: int(str(x)), numbers))
    # str_numbers = sorted(str_numbers, key=lambda x: x[0])

    def four_numb(a):
        str_a = str(a)
        str_2a = str_a + str_a + str_a + str_a
        return int(str_2a[:4]) # str 자체를 비교하면 int 쓰지 않아도됨, 첫글자 부터 비교하는 방식이므로
    sorted_numbers = sorted(numbers, key=lambda x: four_numb(x))
    answer = ''
    while len(sorted_numbers):
        a = sorted_numbers.pop()
        answer = answer + str(a)
    return answer  # str(int(''.join(numbers))) str원소들을 하나로 합칠 때

numbers = [3, 30, 34, 5, 9]

solution(numbers)