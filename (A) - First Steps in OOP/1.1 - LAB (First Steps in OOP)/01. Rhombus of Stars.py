def rhombus_of_stars_function():
    size_of_rhombus = int(input())
    for count_lines in range(1, size_of_rhombus + 1):
        for empty_space in range(size_of_rhombus - count_lines):
            print(" ", end="")
        for number_of_star in range(1, count_lines):
            print("*", end=" ")
        print("*")
    for count_lines in range(size_of_rhombus - 1, 0, - 1):
        for empty_space in range(size_of_rhombus - count_lines):
            print(" ", end="")
        for number_of_star in range(1, count_lines):
            print("*", end=" ")
        print("*")


rhombus_of_stars_function()


# def print_row(current_size, current_star_count):
#     for row in range(current_size - star_count):
#         print(" ", end="")
#     for row in range(1, current_star_count):
#         print("*", end=" ")
#     print("*")
#
#
# size = int(input())
# for star_count in range(1, size + 1):
#     print_row(size, star_count)
# for star_count in range(size - 1, 0, - 1):
#     print_row(size, star_count)


# number = int(input())
# for count_stars in range(1, number + 1):
#     for empty in range(number - count_stars):
#         print(" ", end="")
#     for star in range(1, count_stars):
#         print("*", end=" ")
#     print("*")
# for count_stars in range(number - 1, 0, - 1):
#     for empty in range(number - count_stars):
#         print(" ", end="")
#     for star in range(1, count_stars):
#         print("*", end=" ")
#     print("*")
