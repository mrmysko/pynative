def convert_list():
    # Exercise 1: Convert two lists into a dictionary
    keys = ["Ten", "Twenty", "Thirty"]
    values = [10, 20, 30]

    dictionary = {}

    dictionary.update(zip(keys, values))

    print(dictionary)


def merge_dict():
    # Exercise 2: Merge two Python dictionaries into one
    dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
    dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}

    dict1.update(dict2)
    dict3 = {**dict1, **dict2}

    print(dict1)
    print(dict3)


def print_sample():
    # Exercise 3: Print the value of key ‘history’ from the below dict
    sampleDict = {
        "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
    }

    print(sampleDict["class"]["student"]["marks"]["history"])


def default_dict():
    # Exercise 4: Initialize dictionary with default values
    employees = ["Kelly", "Emma"]
    defaults = {"designation": "Developer", "salary": 8000}

    default = dict.fromkeys(employees, defaults)

    print(default)


def extract_key():
    # Exercise 5: Create a dictionary by extracting the keys from a given dictionary

    sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]

    test = {}
    for i in keys:
        test.update({i: sample_dict[i]})

    print(test)


def del_keys():
    # Exercise 6: Delete a list of keys from a dictionary
    sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

    # Keys to remove
    keys = ["name", "salary"]

    for i in keys:
        sample_dict.pop(i)

    print(sample_dict)


def check_val():
    # Exercise 7: Check if a value exists in a dictionary
    sample_dict = {"a": 100, "b": 200, "c": 300}

    if 200 in sample_dict.values():
        print("200 is a value.")


def rename_key():
    # Exercise 8: Rename key of a dictionary
    sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

    sample_dict.update({"location": sample_dict.pop("city")})

    print(sample_dict)


def minimum_dict():
    # Exercise 9: Get the key of a minimum value from the following dictionary
    sample_dict = {"Physics": 82, "Math": 65, "history": 75}

    minimum = 70

    # for key, value in sample_dict.items():
    #    if value < minimum:
    #       print(key)

    # This somehow returns the key for the lowest key value
    print(min(sample_dict))


def change_nested():
    # Exercise 10: Change value of a key in a nested dictionary
    sample_dict = {
        "emp1": {"name": "Jhon", "salary": 7500},
        "emp2": {"name": "Emma", "salary": 8000},
        "emp3": {"name": "Brad", "salary": 500},
    }

    sample_dict["emp3"]["salary"] = 8500
    print(sample_dict)


if __name__ == "__main__":
    change_nested()
