def solution():

    def integers():
        number = 0
        while True:
            number += 1
            yield number

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        numbers_list = []
        for _ in range(n):
            number = next(seq)
            numbers_list.append(number)
        return numbers_list

    return take, halves, integers


# take = solution()[0]
# halves = solution()[1]
# print(take(5, halves()))
