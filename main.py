
# Rotate an array a specified number of elements to the left. Throw an exception
# if the shift amount is negative (don't rotate the list to the right).

def rotate_array(array, shift_amount):

    # Make sure shift_amount is a legal value (i.e. a positive integer).

    if not isinstance(shift_amount, int):
        raise ValueError("Shift amount must be a positive integer")
    if shift_amount < 0:
        raise ValueError("Shift amount must be a positive integer")

    # Special-case the empty array since later we want to mod by the length.

    if array == []:
        return []

    # Rotate the array the specified amount.

    shift_amount = shift_amount % len(array)
    return array[shift_amount:] + array[:shift_amount]


# Pretty-printing helpers.

def pad_string(string, length):
    return string + " " * (length - len(string))

def make_string_green(string):
    return "\033[92m{}\033[0m".format(string)

def make_string_bold_red(string):
    return "\033[91m\033[1m{}\033[0m".format(string)


# Generate a pretty report for a single test case of the string rotation method.

def create_report(array, shift_amount, expected_output, alt_name = None):
    array_col_width = 20
    shift_col_width = 10

    actual_output = rotate_array(array, shift_amount)
    test_name = str(array) if alt_name == None else alt_name

    report = ""
    report += pad_string(test_name, array_col_width)
    report += pad_string(str(shift_amount), shift_col_width)
        
    if actual_output == expected_output:
        report += make_string_green("OK")
    else:
        report += make_string_bold_red(str(actual_output))

    return report


# Put in a series of calls to the array_rotator method and print a report of
# whether it gets the right answers.

def test_array_rotator():

    # "Softball" test cases for basic functionality.

    print(create_report([1, 2, 3],        1,        [2, 3, 1]))
    print(create_report([5, 5, 5, 5, 6],  4,        [6, 5, 5, 5, 5]))
    print(create_report([5, 5, 5, 5, 6],  5,        [5, 5, 5, 5, 6]))
    print(create_report([0, 1, 4, 5],     10,       [4, 5, 0, 1]))
    print(create_report([1, 2, 3, 4],     0,        [1, 2, 3, 4]))
    print(create_report([],               4,        []))
    print(create_report([],               0,        []))

    # Stress tests for long arrays and large shift amounts.

    long_list = [i for i in range(100000)]
    long_list_shift = [99999] + [i for i in range(99999)]

    print(create_report([9, 8, 1], 1000000,          [8, 1, 9]))
    print(create_report(long_list, 0,                long_list,       alt_name = "<long_list>"))
    print(create_report(long_list, len(long_list)-1, long_list_shift, alt_name = "<long_list>"))

    # Out-of-bounds tests for negative and non-integer shift amounts.

    try:
        output = rotate_array([1, 2, 3], -1)
    except ValueError:
        print(make_string_green("Negative shift amount raises ValueError."))
    except:
        print(make_string_bold_red("Negative shift amount raises wrong kind of exception."))
    else:
        print(make_string_bold_red("Negative shift amount does not raise an error."))

    try:
        output = rotate_array([1, 2, 3], 0.5)
    except ValueError:
        print(make_string_green("Non-integer shift amount raises ValueError."))
    except:
        print(make_string_bold_red("Non-integer shift amount raises wrong kind of exception."))
    else:
        print(make_string_bold_red("Non-integer shift amount does not raise an error."))


test_array_rotator()

