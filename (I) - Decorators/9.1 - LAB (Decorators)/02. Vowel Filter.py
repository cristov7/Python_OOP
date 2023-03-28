def vowel_filter(function):   # function = func name = get_letters
    def wrapper():            # args from func name
        letters_list = function()
        vowels_list = ["a", "e", "i", "o", "u"]
        filtered_list = [letter for letter in letters_list
                         if letter in vowels_list]
        return filtered_list
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


# print(get_letters())
