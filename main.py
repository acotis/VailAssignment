
# Rotate an array a specified number of elements to the left. Throw an exception
# if the shift amount is negative (don't rotate the list to the right).
#
# UNDER CONSTRUCTION

def rotate_array(array, shift_amount):
    return []

# Pad out a string with spaces to achieve a specified length (used for pretty-printing
# by the test_array_rotator() method).

def pad_string(string, length):
    return string + " " * (length - len(string))

# Generate a pretty report for a single test case of the string rotation method.

def create_report(array, shift_amount, expected_output, alt_name = None):
    array_col_width = 20
    shift_col_width = 10
    test_pass_string = "\033[92mOK\033[0m"        # String "OK" in green text
    test_fail_string = "\033[91m\033[1m{}\033[0m" # Actual output in bold red text

    actual_output = rotate_array(array, shift_amount)
    test_name = str(array) if alt_name == None else alt_name

    report = ""
    report += pad_string(test_name, array_col_width)
    report += pad_string(str(shift_amount), shift_col_width)
        
    if actual_output == expected_output:
        report += test_pass_string
    else:
        report += test_fail_string.format(actual_output)

    return report

# Put in a series of calls to the array_rotator method and print a report of
# whether it gets the right answers.

def test_array_rotator():

    # "Softball" test cases for inputs the program is expected to handle normally.

    tests = [([1, 2, 3],        1,                  [2, 3, 1]),
             ([5, 5, 5, 5, 6],  4,                  [6, 5, 5, 5, 5]),
             ([5, 5, 5, 5, 6],  5,                  [5, 5, 5, 5, 6]),
             ([0, 1, 4, 5],     10,                 [4, 5, 0, 1]),
             ([1, 2, 3, 4],     0,                  [1, 2, 3, 4]),
             ([],               4,                  []),
             ([],               0,                  []),
             ([9, 8, 1],        1000000,            [8, 1, 9])]


    # todo: also create some tests that ensure an exception is raised when the
    # shift amount is negative or not an integer or when other stuff is weird

    # Run the normal tests, and pretty-print the results.

    for array, shift_amount, expected_output in tests:
        print(create_report(array, shift_amount, expected_output))

    # Run two tests on a very large input array, and pretty-print the results.
    # These tests are separated because they require special pretty-printing


    # Todo: add these "big list" tests which require special pretty-printing

    long_list = [i for i in range(100000)]
    long_list_rotate_right_one = [99999] + [i for i in range(99999)]

    print(create_report(long_list, 0,                long_list, alt_name = "<long_list>"))
    print(create_report(long_list, len(long_list)-1, long_list, alt_name = "<long_list>"))


test_array_rotator()

