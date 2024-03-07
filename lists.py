def rev_list(lst: list):

    lst.reverse()
    return lst


def concat_index(list1: list, list2: list):

    zipped3 = [x + y for x, y in zip(list1, list2)]
    return zipped3


def squared(lst: list):
    squared = [x**2 for x in lst]
    return squared


def concat_loop(list1: list, list2: list):
    concatted = [x + y for x in list1 for y in list2]
    return concatted


def ex5_lists(list1: list, list2: list):
    list2.reverse()
    some_list = [(x, y) for x, y in zip(list1, list2)]
    [print(x, y) for x, y in some_list]

    # for x, y in zip(list1, list2[::-1]):
    #    print(x, y)


def rem_empty(lst: list):

    def gone(x):
        if len(x) == 0:
            return False
        return True

    filtered = filter(gone, lst)
    for i in filtered:
        print(i)

    # res = list(filter(None, lst))
    # print(res)


def appappaapp(lst: list):

    for i in lst:
        if isinstance(i, list):
            appappaapp(i)

        if i == 6000:
            lst.insert(lst.index(i) + 1, 7000)

    return lst


def alpha_list(lst: list):

    for i in lst:
        if isinstance(i, list):
            alpha_list(i)
        elif ord(i) + 1 == ord("h"):
            lst.extend(["h", "i", "j"])

    return lst


def repl_value(lst: list, value1, value2):

    lst.insert(lst.index(value1), value2)
    lst.remove(value1)

    return lst


def rem_all(lst: list, val):
    for i in lst:
        if i == val:
            lst.remove(i)
            # del lst[lst.index(i)]

    return lst

    # return [i for i in lst if i != val]


if __name__ == "__main__":
    print(rev_list([100, 200, 300, 400, 500]))
    print(concat_index([1, 2, 3], [4, 5, 6]))
    print(squared([1, 2, 3, 4, 5]))
    print(concat_loop(["Hello ", "take "], ["Dear", "Sir"]))
    ex5_lists([10, 20, 30, 40], [100, 200, 300, 400])
    rem_empty(["Mike", "", "Emma", "Kelly", "", "Brad"])
    print(appappaapp([10, 20, [300, 400, [5000, 6000], 500], 30, 40]))
    print(alpha_list(["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]))
    print(repl_value([5, 10, 15, 20, 25, 50, 20], 20, 200))
    print(rem_all([5, 20, 15, 20, 25, 50, 20], 20))
