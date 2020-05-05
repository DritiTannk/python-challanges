"""
Given an string in roman no format (s)  your task is to convert it to integer .

Example:
Input
2
V
III
Output
5
3
"""


def roman_conversion(number):
    """ This function will convert the roman number to integer number. """

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  # Roman values dictionary.
    sum = 0  # It calculates the integer value

    for item in number:
        if (roman_dict.get(item)):
            print('Integer Value Of {0} Is: {1}'.format(item, roman_dict[item]))  # prints the roman value of each item.
            sum += roman_dict[item]

    return sum


if __name__ == '__main__':
    user_num = input("Enter Your Roman Number: ").upper()
    if user_num != '':
        result = roman_conversion(user_num)  # calling function.

        if result == 0:
            print(" The \'{}\' is not a Roman Number.".format(user_num))  # when user input is invalid.
        else:
             print("\n The Integer Value of '{0}' Roman Number Is: {1} ".format(user_num, result))

    else:
        print("\n *** Empty Values are not Accepted *** ")


