def funcl(*args):
    [print(i) for i in args]


def calculation(val1, val2):
    val1, val2 = val1 + val2, val1 - val2
    return val1, val2


def show_emplyee(name, salary=9000):
    print(f"Name: {name}, Salary: {salary}")


def add_this_shit(val1, val2):

    def addition(a, b):
        return a + b

    return addition(val1, val2) + 5


def recursive_add(val):
    if val != 0:
        return val + recursive_add(val - 1)

    return val


def display_student(name, age):
    print(f"Name: {name}, Age: {age}")


if __name__ == "__main__":
    print(recursive_add(15))
