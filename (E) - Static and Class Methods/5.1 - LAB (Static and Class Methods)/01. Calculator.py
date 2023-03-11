from functools import reduce


class Calculator:
    @staticmethod
    def add(*args) -> int:
        return reduce(lambda a, b: a + b, args)
        # result = sum(args)
        # return result


    @staticmethod
    def multiply(*args) -> int:
        return reduce(lambda a, b: a * b, args)
        # result = 1
        # for element in args:
        #     result *= element
        # return result

    @staticmethod
    def divide(*args) -> [float, Exception]:
        return reduce(lambda a, b: a / b, args)
        # result = args[0]
        # for element in args[1:]:
        #     result /= element
        # return result

    @staticmethod
    def subtract(*args) -> int:
        return reduce(lambda a, b: a - b, args)
        # result = args[0]
        # for element in args[1:]:
        #     result -= element
        # return result


# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))
