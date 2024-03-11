import re


def multi(num1: int, num2: int) -> int:
    return num1 * num2


def double_star(some_string: str) -> str:
    some_list = some_string.split()

    return "**".join(some_list)


def octal(num: int) -> int:

    mod_str = ""

    return num % 8


def accept_input():

    # Fix this
    pattern = '^\[.*(".*").*\]$'

    some_list = input("Input a list, or some shit: ")
    some_list = some_list.split()
    some_list2 = list(some_list)

    print(some_list)
    print(some_list2)


if __name__ == "__main__":
    num = 100

    print(multi(5, 4))
    print(double_star("Name is James"))
    print(f"Here's {num} in octal: {num:o}")
    print("Here's {} in octal: {:o}".format(num, num))
    print(f"Here's {num:.2f} with 2 decimal spaces.")

    accept_input()
