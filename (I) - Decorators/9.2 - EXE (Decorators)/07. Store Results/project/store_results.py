class store_results:
    def __init__(self, function):   # function = func name
        self.function = function

    def __call__(self, *args):      # *args = args from func name
        with open("results.txt", "a") as file:
            func_name = self.function.__name__
            func_result = self.function(*args)
            text = f"Function '{func_name}' was called. Result: {func_result}\n"
            file.write(text)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
