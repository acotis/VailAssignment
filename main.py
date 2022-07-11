
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

    # Todo: add these "big list" tests which require special pretty-printing

    # long_list = [i for i in range(100000)]
    # long_list_rotate_right_one = [99999] + [i for i in range(99999)]
             # (long_list,        0,                  long_list),
             # (long_list         len(long_list)-1,   long_list_rotate_right_one)]

    # todo: also create some tests that ensure an exception is raised when the
    # shift amount is negative or not an integer or when other stuff is weird

    for array, shift_amount, expected_output in tests:
        actual_output = rotate_array(array, shift_amount)

        output = ""
        output += pad_string(str(array), 20)
        output += pad_string(str(shift_amount), 10)
        
        if actual_output == expected_output:
            # String "OK" printed in green text
            output += "\033[92mOK\033[0m"
        else:
            # Incorrect output printed in bold red text
            output += "\033[91m\033[1m" + str(actual_output) + "\033[0m"

        print(output)

        
test_array_rotator()
